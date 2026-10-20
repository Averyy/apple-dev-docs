# delegate

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Specifies the notification center delegate.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
unowned(unsafe) var delegate: (any NSUserNotificationCenterDelegate)? { get set }
```

```objc
@property (assign, nullable) id<NSUserNotificationCenterDelegate> delegate;
```

#### Discussion

The delegate must conform to the [`NSUserNotificationCenterDelegate`](../nsusernotificationcenterdelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/delegate)*