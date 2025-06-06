# TokenUpdateRequest

**Framework**: Devicemanagement  
**Kind**: dictionary

The request object for sending the new token details.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object TokenUpdateRequest
```

## Mentions

- [Managing Passcodes](managing-passcodes.md)

#### Discussion

The device sends an initial token update message to the server when it has installed the MDM payload. The server should send push messages to the device only after receiving the first token update message. If the device reports that it is `AwaitingConfiguration`, the MDM server is expected to send a [`Release Device from Await Configuration`](device-configured-command.md) MDM command before the device can allow the user to proceed in Setup Assistant. This gives the MDM server the opportunity to do some setup via MDM commands.

In addition to sending the initial [`Token Update`](token-update.md) message, the iOS device may now send additional [`Token Update`](token-update.md) messages to the check-in server at any time while it has a valid MDM enrollment.

The use of `PushMagic` constrains the device to a unique MDM relationship. When a user removes the MDM profile, the device should no longer listen to the former relationship, even if the user reestablishes a management relationship with the same server topic. Note that only the push topic is the same in this case; the serverʼs address could have changed. This also helps when a user restores a device from backup that contains an older relationship. The use of `PushMagic` also ensures that the server that receives the `CheckIn` message is owned by the same enterprise as the computer sending push notifications. This is important because there is no way of knowing if the push topic belongs to the owner of the checkin server. It is conceivable that Apple could revoke a push token for one party, only to have that party re-enroll people piggybacking on some other topic thatʼs actively pushing. The fact that all MDM push topics reside in the namespace com.apple.mgmt.* helps prevent this.

The `PushMagic` or `UnlockToken` fields of subsequent [`Token Update`](token-update.md) messages may be identical to those in previous messages or may be different (and may differ in size from previous values). If different, the server should update its record for the device to the new value provided by the message. Failure to do so results in the server being unable to send push notifications or perform passcode resets.

While the `UnlockToken` message can be sent multiple times by the device, it is possible it may only be sent once if `PushMagic` or `UnlockToken` values change. Implementations should not rely on repeated messages to update lost server-side data or to recover from a failure to process a previous [`Token Update`](token-update.md) message.

While the `Token Update` message can be sent multiple times by the device, it is possible that it may only be sent once if the values contained within the message never change. Implementations should not rely on repeated messages to update lost server-side data or to recover from a failure to process a previous `Token Update` message. Also note that the `UnlockToken` is optional. The absence of an `UnlockToken` in a `Token Update` message should not be treated as an invalidation of a previously received `UnlockToken`.

> **Note**:  The topic string for the MDM check-in protocol must start with `com.apple.mgmt.*` where `*` is a unique suffix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeviceManagement/tokenupdaterequest)*