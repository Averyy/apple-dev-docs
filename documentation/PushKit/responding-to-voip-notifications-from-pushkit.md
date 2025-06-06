# Responding to VoIP Notifications from PushKit

**Framework**: Pushkit

Receive incoming Voice-over-IP (VoIP) push notifications and use them to display the system call interface to the user.

#### Overview

If your app provides Voice-over-IP (VoIP) phone services, you may use PushKit to handle incoming calls on user devices. PushKit provides an efficient way to manage calls that doesn’t require your app to be running to receive calls. When it detects a call for a specific user, your server sends a push notification to the user’s device with information about that call. Upon receiving the notification, the device wakes up your app and gives it time to notify the user and connect to your call service.

For apps built using the iOS 13 SDK or later, PushKit requires you to use CallKit when handling VoIP calls. CallKit ensures that apps providing call-related services on a user’s device work seamlessly together on the user’s device, and respect features like Do Not Disturb. CallKit also operates the system’s call-related UIs, including the incoming or outgoing call screens. Use CallKit to present these interfaces and manage interactions with them.

> ❗ **Important**: If you are unable to support CallKit in your app, you cannot use PushKit to handle push notifications. Instead, configure your app’s push notification support with the User Notifications framework. If you need to do work in response to an incoming notification—for example, to decrypt content—use a notification service extension to perform that work. For more information about handling notifications and implementing a notification service extension, see [`User Notifications`](https://developer.apple.com/documentation/UserNotifications).

For information about how to configure your app to app to support PushKit, see [`Supporting PushKit Notifications in Your App`](supporting-pushkit-notifications-in-your-app.md).

##### Create a Call Provider Object to Manage Calls in Your App

VoIP apps must use CallKit to present the system’s call-related interfaces. You present these interfaces using a [`CXProvider`](https://developer.apple.com/documentation/CallKit/CXProvider) object, which manages user interactions for both incoming and outgoing calls. Create a provider object early in your app’s life cycle and make it available to your app’s call-related code.

The following code example shows how to create a provider object and assign a custom delegate to it. Initialize the [`CXProvider`](https://developer.apple.com/documentation/CallKit/CXProvider) object with a configuration object containing the details about your service. Assign one of your app’s custom objects as a delegate, and use that object to respond to user actions and telephony-related changes.

```swift
// Configure the app's CallKit provider object.
let config = CXProviderConfiguration(localizedName: "VoIP Service")
config.supportsVideo = true
config.supportedHandleTypes = [.phoneNumber]
config.maximumCallsPerCallGroup = 1

// Create the provider and attach the custom delegate object
// used by the app to respond to updates.
callProvider = CXProvider(configuration: config)
callProvider?.setDelegate(callManager, queue: nil)
```

Each provider object represents a single instance of your app’s phone service and facilitates interactions with the system. Apps need only one provider object to manage phone calls for the current user. If your service allows multiple users or multiple accounts per user, you are responsible for mapping incoming calls to the appropriate user accounts.

##### Generate Push Notifications From Your Server

Your servers handle most of the call-related work required to connect users. Each time the user opens your app on a device, create a connection from that app to your server. When the user initiates a phone call, use that connection to communicate the details of the call back to your server. Your server must then try to connect the call initiator with the call recipient. If the recipient’s app is running and has an active connection with the server, communicate directly with the app using your existing connection. If the app is not running, generate a push notification to wake up the app.

Each push notification consists of a device token and a payload with the details of the call. You bundle this information into an HTTP request, which you then send to Apple Push Notification service (APNs). PushKit provides the device token that you use as the target address for the user’s device at configuration time.

When configuring the HTTP request for VoIP push notifications, always configure your requests with the following information:

- Set the value of the `apns-expiration` header field to `0`, or to only a few seconds. Doing so prevents the system from delivering the notification at a much later time.
- Include information about the incoming call to the JSON payload. For example, include the unique call identifier that your server uses to track the call. Your app can use this identifier to check in with the server later. You might also want to include information about the caller, so that you can display that information in the incoming call UI.

For information about configuring a custom server to generate push notifications, see [`Setting up a remote notification server`](https://developer.apple.com/documentation/UserNotifications/setting-up-a-remote-notification-server). For information about how to send push notifications, see [`Sending notification requests to APNs`](https://developer.apple.com/documentation/UserNotifications/sending-notification-requests-to-apns).

##### Respond to Voip Push Notifications in Your App

When one of your users initiates a phone call, your server must connect to your app on the recipient’s device. If your server doesn’t have an active network connection to the app, you can ask the app to check in by sending it a push notification. Construct the push notification request on your server and send it to APNs for delivery to the user’s device. For VoIP push notifications, the system launches or wakes your app and delivers the notification to your app’s [`PKPushRegistry`](pkpushregistry.md) object, which calls the [`pushRegistry(_:didReceiveIncomingPushWith:for:completion:)`](pkpushregistrydelegate/pushregistry(_:didreceiveincomingpushwith:for:completion:).md) method of its delegate. Use that method to display the incoming call UI and to establish a connection to your VoIP server.

The following code example shows how you might process an incoming VoIP push notification in your [`pushRegistry(_:didReceiveIncomingPushWith:for:completion:)`](pkpushregistrydelegate/pushregistry(_:didreceiveincomingpushwith:for:completion:).md) method. After extracting the call data from the notification’s payload dictionary, create a [`CXCallUpdate`](https://developer.apple.com/documentation/CallKit/CXCallUpdate) object and pass it to the [`reportNewIncomingCall(with:update:completion:)`](https://developer.apple.com/documentation/CallKit/CXProvider/reportNewIncomingCall(with:update:completion:)) method of your app’s [`CXProvider`](https://developer.apple.com/documentation/CallKit/CXProvider) object. While CallKit processes your request, establish a connection to your VoIP server in parallel; you can always notify CallKit later if you run into problems. If CallKit handles the call successfully, the completion block creates some custom data structures to manage that call within the app.

```swift
func pushRegistry(_ registry: PKPushRegistry, 
          didReceiveIncomingPushWith payload: PKPushPayload, 
          for type: PKPushType, 
          completion: @escaping () -> Void) {
   if type == .voIP {
      // Extract the call information from the push notification payload
      if let handle = payload.dictionaryPayload["handle"] as? String,
            let uuidString = payload.dictionaryPayload["callUUID"] as? String,
            let callUUID = UUID(uuidString: uuidString) {

         // Configure the call information data structures.
         let callUpdate = CXCallUpdate()
         let phoneNumber = CXHandle(type: .phoneNumber, value: handle)
         callUpdate.remoteHandle = phoneNumber
                
         // Report the call to CallKit, and let it display the call UI.
         callProvider?.reportNewIncomingCall(with: callUUID, 
                     update: callUpdate, completion: { (error) in
            if error == nil {
               // If the system allows the call to proceed, make a data record for it.
               let newCall = VoipCall(callUUID, phoneNumber: phoneNumber)
               self.callManager.addCall(newCall)
            }

            // Tell PushKit that the notification is handled.
            completion()
         })
                
         // Asynchronously register with the telephony server and 
         // process the call. Report updates to CallKit as needed.
         establishConnection(for: callUUID)
      }
   }
}

```

If the system allows your call to proceed, the [`reportNewIncomingCall(with:update:completion:)`](https://developer.apple.com/documentation/CallKit/CXProvider/reportNewIncomingCall(with:update:completion:)) method executes its completion block and CallKit displays the incoming call interface. At that point, use the delegate of your [`CXProvider`](https://developer.apple.com/documentation/CallKit/CXProvider) object to respond to user interactions with the interface. For example, use your delegate to respond when the user answers or ends the call.

> **Note**: If you didn’t put caller information in your notification’s payload, call the [`reportCall(with:updated:)`](https://developer.apple.com/documentation/CallKit/CXProvider/reportCall(with:updated:)) method of your app’s provider object to update the calling interface. You can call that method at any time to update calls. For example, call it after your app fetches updated caller information from your VoIP server.

For more information about how to handle user interactions with the call interface, see the methods of [`CXProviderDelegate`](https://developer.apple.com/documentation/CallKit/CXProviderDelegate).

##### Respond to Call Hang Ups and Failures

Many things can go wrong when connecting a VoIP call, and CallKit makes it easy to handle problems when they occur.

- If the person who initiated the call hangs up, use the network connection between your app and server to notify the app. In your app, call the [`reportCall(with:endedAt:reason:)`](https://developer.apple.com/documentation/CallKit/CXProvider/reportCall(with:endedAt:reason:)) method of its [`CXProvider`](https://developer.apple.com/documentation/CallKit/CXProvider) object, specifying [`CXCallEndedReason.remoteEnded`](https://developer.apple.com/documentation/CallKit/CXCallEndedReason/remoteEnded) as the reason for the end of the call. If the incoming call interface is onscreen, CallKit updates the interface to reflect the end of the call, and dismisses the interface.
- If the recipient of a call answers before the app establishes a connection to your server, don’t fulfill the [`CXAnswerCallAction`](https://developer.apple.com/documentation/CallKit/CXAnswerCallAction) object sent to the [`provider(_:perform:)`](https://developer.apple.com/documentation/CallKit/CXProviderDelegate/provider(_:perform:)-h4in) method of your delegate immediately. Instead, wait until you establish a connection and then fulfill the object. While it waits for your app to fulfill the request, the incoming call interface lets the user know that the call is connecting, but not yet ready.
- If your app fails to establish a connection to your server, call the [`reportCall(with:endedAt:reason:)`](https://developer.apple.com/documentation/CallKit/CXProvider/reportCall(with:endedAt:reason:)) method with the [`CXCallEndedReason.failed`](https://developer.apple.com/documentation/CallKit/CXCallEndedReason/failed) option. If the incoming call interface is currently onscreen, the system updates it to indicate a failed call.

After sending the initial push notification, don’t send additional push notifications to cancel the call or communicate new details to your app. Instead, communicate with the app directly over the network connection you established between it and your server. Using an existing network connection is generally faster than sending a push notification, and if network conditions are poor, APNs may be unable to deliver push notifications to the device anyway.

## See Also

- [struct PKPushType](pkpushtype.md)
  Constants reflecting the push types you want to support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/PushKit/responding-to-voip-notifications-from-pushkit)*