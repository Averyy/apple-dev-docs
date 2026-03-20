# pushRegistry(_:didReceiveIncomingVoIPPushWith:metadata:withCompletionHandler:)

**Framework**: PushKit  
**Kind**: method

The system calls this method when it receives a VoIP push notification. Use this method to extract data from the notification’s payload and to report a VoIP call using CallKit or LiveCommunicationKit.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
optional func pushRegistry(_ registry: PKPushRegistry, didReceiveIncomingVoIPPushWith payload: PKPushPayload, metadata: PKVoIPPushMetadata) async
```

#### Discussion

The `metadata` parameter contains additional information about the VoIP payload. For example, If the `mustReport` metadata property is set to `YES` your app is required to report an incoming VoIP call or conversation using one of the following methods:

#### Callkit

[`reportNewIncomingCall(with:update:completion:)`](https://developer.apple.com/documentation/CallKit/CXProvider/reportNewIncomingCall(with:update:completion:))

#### Livecommunicationkit

[`reportNewIncomingConversation(uuid:update:)`](https://developer.apple.com/documentation/LiveCommunicationKit/ConversationManager/reportNewIncomingConversation(uuid:update:))

When you call either of these methods, the system displays the standard incoming call interface to the user unless an error occurs. For example, the system reports an error if the user enabled Do Not Disturb. You may establish a connection to your VoIP server in parallel to reporting the incoming call to the system.

If you fail to report a call or conversation to CallKit/LiveCommunicationKit and the metadata’s `mustReport` parameter is set to `YES`, the system will terminate your app. Repeatedly failing to report calls may cause the system to stop delivering any more VoIP push notifications to your app.

If the metadata’s `mustReport` parameter is set to `NO` you are not required to report a call or conversation to CallKit/LiveCommunicationKit. Scenarios that result in `mustReport` set to `NO` include: * Your app is running in the foreground * Your app already has an active call/conversation * The VoIP push notification was received by the device after an extended period of time due to network conditions.

If you are a VoIP developer you should prefer this delegate method over the`pushRegistry:didReceiveIncomingPushWithPayload:forType: withCompletionHandler:` method so that you can use the `metadata` parameter to ignore VoIP push notifications where `mustReport` is set to `NO` and do not need to be reported.

If you want to initiate a VoIP call without using CallKit, register for push notifications using the User Notifications framework instead of PushKit. For more information, see [`User Notifications`](https://developer.apple.com/documentation/UserNotifications).

## Parameters

- `registry`: The [`PKPushRegistry`](pkpushregistry.md) instance responsible for the delegate callback.
- `payload`: The push payload sent by a developer via APNs server API.
- `metadata`: An object containing metadata about the VoIP push payload, such as the `mustReport` boolean indicating whether your app is required to report a call/conversation to CallKit/LiveCommunicationKit for this push.
- `completion`: The notification’s completion handler. Execute this block when you finish processing the notification


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate/pushregistry(_:didreceiveincomingvoippushwith:metadata:withcompletionhandler:))*