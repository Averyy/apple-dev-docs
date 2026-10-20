# NSUserNotification.ActivationType

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

These constants describe how the user notification was activated.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
enum ActivationType
```

```c
enum NSUserNotificationActivationType : NSInteger;
```

## Topics

### Constants
- [NSUserNotification.ActivationType.none](./activationtype-swift.enum/none.md)
  The user did not interact with the notification alert.
- [NSUserNotification.ActivationType.contentsClicked](./activationtype-swift.enum/contentsclicked.md)
  The user clicked on the contents of the notification alert.
- [NSUserNotification.ActivationType.actionButtonClicked](./activationtype-swift.enum/actionbuttonclicked.md)
  The user clicked on the action button of the notification alert.
- [NSUserNotification.ActivationType.replied](./activationtype-swift.enum/replied.md)
  The user replied to the notification.
- [NSUserNotification.ActivationType.additionalActionClicked](./activationtype-swift.enum/additionalactionclicked.md)
  The user clicked on the additional action button of the notification alert.
### Initializers
- [init?(rawValue: Int)](./activationtype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [let NSUserNotificationDefaultSoundName: String](../nsusernotificationdefaultsoundname.md)
  The default notification sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/activationtype-swift.enum)*