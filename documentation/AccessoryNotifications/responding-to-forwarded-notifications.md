# Responding to forwarded notifications

**Framework**: Accessory Notifications

Enable people to interact with notifications on your accessory and convey their responses to iOS.

#### Overview

When someone interacts with a notification on your accessory, send the interaction to iOS as a response: your accessory acts as a relay for the person’s action. The response lets the system perform the same follow-up actions as when someone interacts with a notification on their iPhone. This process relies on the same data provider and transport extensions you implement to forward notifications to your accessory; for more information, see [`Receiving iOS notifications on an accessory`](https://developer.apple.com/documentation/accessorytransportextension/receiving-ios-notifications-on-an-accessory).

A response describes the interaction a person makes with a notification, for example, dismissing it, marking an email as read, or inputting text as a quick reply to a message.

Your accessory encrypts the response data for safe transmission and sends it back to iOS using the [`Accessory Notifications`](AccessoryNotifications.md) framework. The transmission method, or transport type, that the response uses might differ from that of the forwarded notification:

- For Bluetooth sessions, the accessory sends the encrypted data to your transport extension, which forwards it to the data provider using [`sendMessageToDataProvider(_:)`](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/sendmessagetodataprovider(_:)).
- For internet sessions, the accessory instead sends the encrypted data to your server, which routes the data to the device through APNs. The [`pushToken`](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/pushtoken) value from the forwarded notification bypasses the transport extension while ensuring that the response routes to the correct device.

The system decrypts the response data and delivers it to your data provider extension through the [`messageHandler(_:)`](notificationsforwarding/accessorynotificationshandler/messagehandler(_:).md) method. Your extension parses the response details, creates a [`NotificationResponse`](notificationresponse.md), and calls [`sendResponse(_:)`](notificationsforwarding/accessorynotificationssession/sendresponse(_:).md) to deliver the response to the system.

#### Define the Data Format of the Response

First, define a binary format for response data in the data provider extension for your accessory. Choose a format that includes these fields:

- Notification identifier (which matches the response to the notification)
- Source identifier (the app’s bundle ID)
- Action identifier (the action that the person took)
- Person-provided text (for text input responses)

The following code demonstrates an example binary format by serializing the response fields into length-prefixed binary data.

```swift
func serializeResponse(notificationIdentifier: String,
                      sourceIdentifier: String,
                      actionIdentifier: String,
                      userText: String?) -> Data {
    var data = Data()
    
    // Add length-prefixed strings.
    data.append(notificationIdentifier.lengthPrefixedUTF8())
    data.append(sourceIdentifier.lengthPrefixedUTF8())
    data.append(actionIdentifier.lengthPrefixedUTF8())
    
    if let userText = userText {
        data.append(userText.lengthPrefixedUTF8())
    }
    
    return data
}
```

#### Encrypt Response Data on Your Accessory

When someone interacts with a notification on your accessory, encrypt the response data using keys your accessory establishes during the key exchange process (see [`AccessoryTransportSecurity`](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsecurity)). The derivation differs by transport type: Bluetooth sessions export a fresh secret from the HPKE recipient for every response, while internet sessions reuse the outgoing Symmetric Key Ratchet that your accessory initializes once during key exchange.

For Bluetooth sessions, include `AccessoryToHost` in the secret’s context, and export the secret from the same `HPKE.Recipient` your accessory creates during key exchange; there’s no separate HPKE sender for this direction. Derive the context from the protocol information and the transport message’s [`sessionID`](https://developer.apple.com/documentation/accessorytransportextension/transportmessage/sessionid):

```swift
// On the accessory, encrypt the response using the recipient established  
//  during key exchange.
let featureID = sessionID /* Of the transport message. */
let context = Data("\(protocolInfo)-AccessoryToHost-\(featureID)".utf8)

let secret = try recipient.exportSecret(context: context, outputByteCount: 32)

// Create the response data with the interaction details.
let responseData = serializeResponse(
    notificationIdentifier: notificationID,
    sourceIdentifier: sourceID,
    actionIdentifier: actionID,
    userText: userText
)

// Encrypt the response data using AES-GCM.
let sealedBox = try AES.GCM.seal(responseData, using: secret)

// Concatenate the initialization vector, ciphertext, and authentication tag.
let encryptedResponse = sealedBox.combined
```

For internet sessions, encrypt the response using the outgoing ratchet instead of a freshly exported secret. Your accessory initializes the ratchet from the `accessoryToHostSecret` when it completes key exchange, and advances the ratchet with every response. Perform a ratchet step to derive the current message key and the next chain key, using the same `ratchetStep(chainKey:messageIndex:)` derivation that the ratchet uses to decrypt incoming messages:

```swift
// On the accessory, encrypt the response using the outgoing ratchet
//  established during key exchange.
let (messageKey, nextChainKey) = ratchetStep(
    chainKey: outgoingChainKey,
    messageIndex: outgoingMessageIndex
)

// Create the response data with the interaction details.
let responseData = serializeResponse(
    notificationIdentifier: notificationID,
    sourceIdentifier: sourceID,
    actionIdentifier: actionID,
    userText: userText
)

// Encrypt the response data using AES-GCM.
let sealedBox = try AES.GCM.seal(responseData, using: messageKey)

// Concatenate the initialization vector, ciphertext, and authentication tag.
let encryptedResponse = sealedBox.combined
```

Advance the chain key and message index and then persist them before sending the response:

```swift
outgoingChainKey = nextChainKey
outgoingMessageIndex += 1
saveRatchetState()
```

By persisting the chain key and message index first, it ensures that a crash that might occur between the time of persistence and transmission prevents the accessory from reusing the message key for a later message.

To keep the message directions in sync, persist `outgoingChainKey` and `outgoingMessageIndex` together as a single unit, separately from the incoming ratchet’s persisted state. Persist the state before your accessory transmits the response. Since the ratchet derives keys deterministically, recovering from a crash and resending a message with the same `outgoingChainKey` and `outgoingMessageIndex` derives and reuses the same message key, which undermines the ratchet’s forward secrecy guarantee.

Include the ratchet’s `keyID` and `messageIndex` alongside `encryptedResponse` when you send the response. The system uses the ID and index to determine the ratchet instance and step to use for decryption.

#### Send the Response Through Bluetooth

For Bluetooth sessions, send the encrypted response to your transport extension over the active connection:

```swift
// On the accessory, send response via Bluetooth.
sendViaBluetoothToTransportExtension(encryptedResponse, sessionID: sessionID)
```

The `sendViaBluetoothToTransportExtension(_:sessionID:)` method represents the data your accessory sends; your accessory implements this function itself, since the framework doesn’t provide it.

#### Receive and Decrypt Responses in Your Transport Extension

For Bluetooth sessions, the response completes its transmission at your transport extension for decryption by the system. Your [`AccessoryTransportAppExtension`](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportappextension) receives the encrypted response data from your accessory via Bluetooth. Forward the encrypted data to the data provider extension:

```swift
// Receive the accessory reply in your `AccessoryTransportAppExtension`.
func didReceiveDataFromAccessory(_ encryptedData: Data, sessionID: UUID) {
    let message = TransportMessage(sessionID: sessionID, data: encryptedData)
    
    do {
        try transportSession.sendMessageToDataProvider(message)
    } catch {
        // Handle error.
    }
}
```

The system decrypts the message using the `AccessoryToHost` direction keys before delivering the message to your data provider extension.

#### Send the Response Through the Internet

Internet sessions require you to route responses through an APNs server that you deploy. Pass the [`pushToken`](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/pushtoken) value that your accessory receives alongside the notification, along with the encrypted response data, to your server to route the response through APNs:

```swift
// On accessory: for internet sessions, route the response through APNs instead.
sendViaAPNs(encryptedResponse, pushToken: pushToken, sessionID: sessionID)
```

The `sendViaAPNs(_:pushToken:sessionID:)` method represents the data that your accessory sends; your accessory implements this code. Your server pushes the data to APNs using its own APN provider credentials. The forwarded [`pushToken`](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/pushtoken) ensures that the data in the response reaches the correct device. On the push request, include the `apns-push-type` header with a value of `accessory`. Set the `apns-topic` to your companion app’s bundle ID suffixed with `.push-type.accessory`, as in the following example:

```http
apns-push-type: accessory
apns-topic: <your companion app's bundle ID>.push-type.accessory
apns-id: <an optional UUID to track the push request>
```

Send the encrypted response, the session identifier, and the ratchet’s `keyID` and `messageIndex` as a JSON payload in the push request’s `aps` dictionary. The system uses the key ID and message index to identify the ratchet instance and step that decrypts the response:

```json
{
    "aps": {
        "encryptedData": "<base64-encoded encryptedResponse>",
        "sessionIdentifier": "<sessionID>",
        "keyID": "<base64-encoded keyID>",
        "messageIndex": "<outgoingMessageIndex>"
    }
}
```

Internet sessions skip the transport extension step entirely; the system decrypts the response and delivers it to your data provider extension for processing.

For more information about constructing and sending the push request, see [`Sending notification requests to APNs`](https://developer.apple.com/documentation/usernotifications/sending-notification-requests-to-apns).

#### Process Responses in Your Data Provider Extension

Once the system decrypts the response, it hands the data to your data provider extension to reconstruct into a message the system can act on. Your data provider extension receives the decrypted response through the [`messageHandler(_:)`](notificationsforwarding/accessorynotificationshandler/messagehandler(_:).md) method. Parse the response data using your custom format, then create a [`NotificationResponse`](notificationresponse.md) and call [`sendResponse(_:)`](notificationsforwarding/accessorynotificationssession/sendresponse(_:).md) to deliver it to the system:

```swift
func messageHandler(_ message: AccessoryMessage) {
    for payload in message.payloads {
        // Parse the decrypted response data.
        let responseData = payload.data
        let parsedResponse = parseResponse(responseData)
        
        // Create a notification response.
        let notificationResponse = NotificationResponse(
            sourceIdentifier: parsedResponse.sourceID,
            notificationIdentifier: parsedResponse.notificationID,
            actionIdentifier: parsedResponse.actionID,
            userText: parsedResponse.userText
        )
        
        // Send the response to the system.
        Task {
            try await session?.sendResponse(notificationResponse)
        }
    }
}
```

The `parseResponse(_:)` method represents the custom deserialization format you choose for your accessory’s response data encoding:

```swift
func parseResponse(_ data: Data) -> ParsedResponse {
    // The format of `data` needs to match the format that the accessory uses.
}
```

Call `sendResponse(_:)` to complete the notification response. The system then processes the notification reponse in the same manner, regardless of the device that sent it.

#### Handle Different Response Types

Notification response objects represent different interactions that a person performs in response to a notification. Each interaction corresponds to an entry in the notification’s [`actions`](accessorynotification/actions.md) array. For example, when someone dismisses a notification on your accessory, find the action with the type [`AccessoryNotification.Action.ActionType.dismiss`](accessorynotification/action/actiontype/dismiss.md), then initialize a [`NotificationResponse`](notificationresponse.md) instance from its identifiers:

```swift
guard let dismissAction = notification.actions.first(where: { $0.type == .dismiss }) else {
    return // There's no dismiss action available for the notification.
}

let response = NotificationResponse(
    sourceIdentifier: notification.identifier.sourceIdentifier,
    notificationIdentifier: notification.identifier.notificationIdentifier,
    actionIdentifier: dismissAction.identifier,
    userText: nil
)
```

When someone taps an action on the notification instead, follow the same pattern using the tapped action:

```swift
let response = NotificationResponse(
    sourceIdentifier: notification.identifier.sourceIdentifier,
    notificationIdentifier: notification.identifier.notificationIdentifier,
    actionIdentifier: tappedAction.identifier,  // From the accessory notification's actions array.
    userText: nil
)
```

For notifications that support [`AccessoryNotification.Action.ActionType.textInput(placeholder:)`](accessorynotification/action/actiontype/textinput(placeholder:).md), include the text that the person provides in the response:

```swift
let response = NotificationResponse(
    sourceIdentifier: notification.identifier.sourceIdentifier,
    notificationIdentifier: notification.identifier.notificationIdentifier,
    actionIdentifier: textInputAction.identifier,
    userText: userProvidedText
)
```

## See Also

- [struct NotificationResponse](notificationresponse.md)
  A structure that represents a person’s response to a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/responding-to-forwarded-notifications)*