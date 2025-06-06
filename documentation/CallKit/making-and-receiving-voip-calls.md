# Making and receiving VoIP calls

**Framework**: Callkit

Initiate outgoing calls with VoIP and configure your app to receive incoming calls.

#### Overview

You can handle outgoing calls in your app by providing information about the recipient and initiating the call. To receive incoming calls, you can configure your app to respond to an external VoIP notification.

##### Make Outgoing Calls

Initiate an outgoing call with a VoIP app in any of the following ways:

- Perform an interaction within the app.
- Open a link with a supported custom URL scheme.
- Begin a VoIP call using Siri.

For more information about registering and handling URLs, see [`Defining a custom URL scheme for your app`](https://developer.apple.com/documentation/Xcode/defining-a-custom-url-scheme-for-your-app). For more information about initiating a call using Siri, see the doc://com.apple.documentation/documentation/sirikit/instartcallintenthandling protocol.

To make an outgoing call, an app requests a [`CXStartCallAction`](cxstartcallaction.md) object from its [`CXCallController`](cxcallcontroller.md) object. The action consists of a UUID to uniquely identify the call and a [`CXHandle`](cxhandle.md) object to specify the recipient, as the following code example shows:

```swift
let uuid = UUID()
let handle = CXHandle(type: .emailAddress, value: "mruiz2@icloud.com")
 
let startCallAction = CXStartCallAction(call: uuid)
startCallAction.destination = handle
 
let transaction = CXTransaction(action: startCallAction)
callController.request(transaction) { error in
    if let error = error {
        print("Error requesting transaction: \(error)")
    } else {
        print("Requested transaction successfully")
    }
}
```

The `CXHandle` object specifies metadata for the outgoing call. In the example above, it uses an email address. The system on the receiving device uses this metadata to display caller information in the CallKit interface by looking for a matching contact in the recipient’s Contacts app. If the system finds a match, the CallKit interface uses the matching contact data to display the name and a photo as a poster or contact icon. If the recipient’s system can’t find a matching contact in the Contacts app and you provide a Call Directory app extension, it uses the extension to identify the caller and display rich contact information in the CallKit interface. For more information about creating a Call Directory app extension, see [`Identifying and blocking calls`](identifying-and-blocking-calls.md).

After the recipient answers the call, the system calls the provider delegate’s [`provider(_:perform:)`](cxproviderdelegate/provider(_:perform:)-2lem5.md) method. In your implementation of that method, configure an [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) and call the [`fulfill()`](cxaction/fulfill().md) method on the action object when it finishes, as in the code example below:

```swift
func provider(_ provider: CXProvider, perform action: CXAnswerCallAction) {
    // Configure the audio session.
    // ...
    action.fulfill()
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/CallKit/making-and-receiving-voip-calls)*