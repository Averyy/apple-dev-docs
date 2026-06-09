# messageHandler(_:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Handles decrypted messages received from the paired accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
func messageHandler(_ message: TransportMessage)
```

#### Discussion

The system calls this method when your accessory sends data to the data provider extension. For Bluetooth transport, the accessory sends data through your transport extension using [`sendMessageToDataProvider(_:)`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportSession/sendMessageToDataProvider(_:)). For internet transport, the accessory routes data to the device through APNs using [`pushToken`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportSession/pushToken). In either case, the system delivers decrypted messages to this method regardless of the transport type.

#### Process Notification Responses

Parse the message to determine the response type (notification dismissal, action selection, or text input). Create a [`NotificationResponse`](notificationresponse.md) instance and send it to the system using [`sendResponse(_:)`](notificationsforwarding/accessorynotificationssession/sendresponse(_:).md):

```swift
func messageHandler(_ message: AccessoryMessage) {
    for payload in message.payloads {
        let parsedResponse = parseResponse(payload.data)
        
        let response = NotificationResponse(
            sourceIdentifier: parsedResponse.sourceID,
            notificationIdentifier: parsedResponse.notificationID,
            actionIdentifier: parsedResponse.actionID,
            userText: parsedResponse.userText
        )
        
        Task {
            try await session?.sendResponse(response)
        }
    }
}
```

## Parameters

- `message`: The decrypted message payload from the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/messagehandler(_:))*