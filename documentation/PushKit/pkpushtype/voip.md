# voIP

**Framework**: PushKit  
**Kind**: property  
**Role**: Type Property

A push type for Voice-over-IP (VoIP) call invitations.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static let voIP: PKPushType
```

```c
extern PKPushType const PKPushTypeVoIP;
```

#### Discussion

Use this type of notification to initiate live voice calls over the network. Apps receiving VoIP push notifications must report the call quickly to CallKit, so it can alert the user to the presence of the incoming call. For apps linked against the iOS 13 SDK or later, the system terminates your app if you fail to report these notifications to CallKit. If your app repeatedly fails to report VoIP notifications to CallKit, the system stops launching your app for VoIP push notifications.

Don’t use this type of notification for anything other than initiating VoIP calls. If you don’t want to post the CallKit call interface, handle notifications with the [User Notifications](../../UserNotifications/UserNotifications.md) framework instead of PushKit. When sending encrypted content, use a Notification Service Extension to decrypt that content before displaying it to the user. You can also use a Notification Content Extension to display a custom interface for your app’s notifications. For more information, see [Modifying content in newly delivered notifications](../../UserNotifications/modifying-content-in-newly-delivered-notifications.md) and [Customizing the Appearance of Notifications](../../UserNotificationsUI/customizing-the-appearance-of-notifications.md).

## See Also

### Notification Types
- [static let complication: PKPushType](./complication.md)
  A push type for watchOS complications.
- [static let fileProvider: PKPushType](./fileprovider.md)
  A push type for file provider updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushtype/voip)*