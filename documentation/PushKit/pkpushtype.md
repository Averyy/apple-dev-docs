# PKPushType

**Framework**: PushKit  
**Kind**: struct  
**Role**: Structure

Constants reflecting the push types you want to support.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct PKPushType
```

```c
typedef NSString * PKPushType;
```

## Topics

### Notification Types
- [static let complication: PKPushType](./pkpushtype/complication.md)
  A push type for watchOS complications.
- [static let fileProvider: PKPushType](./pkpushtype/fileprovider.md)
  A push type for file provider updates.
- [static let voIP: PKPushType](./pkpushtype/voip.md)
  A push type for Voice-over-IP (VoIP) call invitations.
### Initializers
- [init(rawValue: String)](./pkpushtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Push Types
- [Responding to VoIP Notifications from PushKit](./responding-to-voip-notifications-from-pushkit.md)
  Receive incoming Voice-over-IP (VoIP) push notifications and use them to display the system call interface to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushtype)*