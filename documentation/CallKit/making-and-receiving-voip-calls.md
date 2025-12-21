# Making and receiving VoIP calls

**Framework**: CallKit

Initiate outgoing calls with VoIP and configure your app to receive incoming calls.

#### Overview

You can handle outgoing calls in your app by providing information about the recipient and initiating the call. To receive incoming calls, you can configure your app to respond to an external VoIP notification.

##### Make Outgoing Calls

Initiate an outgoing call with a VoIP app in any of the following ways:

- Perform an interaction within the app.
- Open a link with a supported custom URL scheme.
- Begin a VoIP call using Siri.

For more information about registering and handling URLs, see [`Defining a custom URL scheme for your app`](https://developer.apple.com/documentation/Xcode/defining-a-custom-url-scheme-for-your-app). For more information about initiating a call using Siri, see the [`INStartCallIntentHandling`](https://developer.apple.com/documentation/Intents/INStartCallIntentHandling) protocol.

To make an outgoing call, request a [`CXStartCallAction`](cxstartcallaction.md) object. The action consists of a UUID to uniquely identify the call and a [`CXHandle`](cxhandle.md) object to specify the recipient, as shown in the following example from the [`VoIP calling with CallKit`](voip-calling-with-callkit.md) sample code project:

```swift
func startCall(handle: String, video: Bool = false) {
    let handle = CXHandle(type: .phoneNumber, value: handle)
    let startCallAction = CXStartCallAction(call: UUID(), handle: handle)

    startCallAction.isVideo = video

    let transaction = CXTransaction()
    transaction.addAction(startCallAction)

    requestTransaction(transaction)
}

private func requestTransaction(_ transaction: CXTransaction) {
    callController.request(transaction) { error in
        if let error = error {
            print("Error requesting transaction:", error.localizedDescription)
        } else {
            print("Requested transaction successfully")
        }
    }
}
```

The `CXHandle` object specifies metadata for the outgoing call. In the example above, it uses an email address. The system on the receiving device uses this metadata to display caller information in the CallKit interface by looking for a matching contact in the recipient’s Contacts app. If the system finds a match, the CallKit interface uses the matching contact data to display the name and a photo as a poster or contact icon. If the recipient’s system can’t find a matching contact in the Contacts app and you provide a Call Directory app extension, it uses the extension to identify the caller and display rich contact information in the CallKit interface. For more information about creating a Call Directory app extension, see [`Identifying and blocking calls`](identifying-and-blocking-calls.md).

After you request to start a VoIP call using a [`CXTransaction`](cxtransaction.md), you need to wait for confirmation from the system to actually start the call. After you requested a call as shown in the example above, the system calls your provider delegate’s [`provider(_:perform:)`](cxproviderdelegate/provider(_:perform:)-2lem5.md) method to let you know that it accepted the [`CXTransaction`](cxtransaction.md) you created and that you can start your VoIP session. In your implementation of the [`provider(_:perform:)`](cxproviderdelegate/provider(_:perform:)-2lem5.md) callback method, configure an [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) and call the [`fulfill()`](cxaction/fulfill().md) method on the action object when it finishes, as shown in the following code snippet from the [`VoIP calling with CallKit`](voip-calling-with-callkit.md) sample code project:

```swift
func provider(_ provider: CXProvider, perform action: CXStartCallAction) {
    // Create and configure an instance of SpeakerboxCall to represent the new outgoing call.
    let call = SpeakerboxCall(uuid: action.callUUID, isOutgoing: true)
    call.handle = action.handle.value

    /*
     Configure the audio session but do not start call audio here.
     Call audio should not be started until the audio session is activated by the system,
     after having its priority elevated.
     */
    configureAudioSession()

    /*
     Set callbacks for significant events in the call's lifecycle,
     so that the CXProvider can be updated to reflect the updated state.
     */
    call.hasStartedConnectingDidChange = { [weak self] in
        self?.provider.reportOutgoingCall(with: call.uuid, startedConnectingAt: call.connectingDate)
    }
    call.hasConnectedDidChange = {[weak self] in
        self?.provider.reportOutgoingCall(with: call.uuid, connectedAt: call.connectDate)
    }

    // Trigger the call to be started via the underlying network service.
    call.startSpeakerboxCall { success in
        if success {
            // Signal to the system that the action was successfully performed.
            action.fulfill()

            // Add the new outgoing call to the app's list of calls.
            self.callManager.addCall(call)
        } else {
            // Signal to the system that the action was unable to be performed.
            action.fail()
        }
    }
}
```

##### Receive Incoming Calls

To configure your app to receive incoming calls, first create a [`CXProvider`](cxprovider.md) object and store it for global access. An app reports an incoming call to the provider in response to an external notification, such as a VoIP push notification from [`PushKit`](https://developer.apple.com/documentation/PushKit), with the [`pushRegistry(_:didReceiveIncomingPushWith:for:completion:)`](https://developer.apple.com/documentation/PushKit/PKPushRegistryDelegate/pushRegistry(_:didReceiveIncomingPushWith:for:completion:)) and [`pushRegistry(_:didReceiveIncomingPushWith:for:completion:)`](https://developer.apple.com/documentation/PushKit/PKPushRegistryDelegate/pushRegistry(_:didReceiveIncomingPushWith:for:completion:)) callbacks.

> **Note**:  For more information about VoIP push notifications and PushKit, see [`Supporting PushKit Notifications in Your App`](https://developer.apple.com/documentation/PushKit/supporting-pushkit-notifications-in-your-app).

Using the information from the external notification in the callback, the app creates a UUID and a [`CXCallUpdate`](cxcallupdate.md) object to uniquely identify the call and the caller. Then it passes them both to the provider using the [`reportNewIncomingCall(with:update:completion:)`](cxprovider/reportnewincomingcall(with:update:completion:).md) method to report the incoming call.

```swift
if let uuidString = payload.dictionaryPayload["UUID"] as? String,
    let identifier = payload.dictionaryPayload["identifier"] as? String,
    let uuid = UUID(uuidString: uuidString)
{
    let update = CXCallUpdate()    
    update.callerIdentifier = identifier
    
    provider.reportNewIncomingCall(with: uuid, update: update) { error in
        // Add your implementation to report the call.
        // ...
    }
}
```

After the call connects, the system calls the [`provider(_:perform:)`](cxproviderdelegate/provider(_:perform:)-2lem5.md) method of the provider delegate. In your implementation, the delegate is responsible for configuring an [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) to initiate the audio for a call and calling [`fulfill()`](cxaction/fulfill().md) on the action when it finishes.

```swift
func provider(_ provider: CXProvider, perform action: CXAnswerCallAction) {
    // Configure the audio session.
    // ...
    action.fulfill()
}
```

## See Also

- [class CXProvider](cxprovider.md)
  An object that represents a telephony provider.
- [protocol CXProviderDelegate](cxproviderdelegate.md)
  A collection of methods that a telephony provider object calls.
- [class CXProviderConfiguration](cxproviderconfiguration.md)
  An encapsulation of the configuration of a provider object.
- [VoIP calling with CallKit](voip-calling-with-callkit.md)
  Use the CallKit framework to integrate native VoIP calling.
- [Preparing your app to be the default calling app](preparing-your-app-to-be-the-default-calling-app.md)
  Configure your CallKit or LiveCommunicationKit app so people can set it as the default calling app on their device.
- [CallKit updates](../Updates/CallKit.md)
  Learn about important changes to CallKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/making-and-receiving-voip-calls)*