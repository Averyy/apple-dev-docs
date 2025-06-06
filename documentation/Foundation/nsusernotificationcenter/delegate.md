# delegate

**Framework**: Foundation  
**Kind**: property

Specifies the notification center delegate.

**Availability**:
- macOS 10.8+

## Declaration

```swift
unowned(unsafe) var delegate: (any NSUserNotificationCenterDelegate)? { get set }
```

#### Discussion

The delegate must conform to the [`NSUserNotificationCenterDelegate`](nsusernotificationcenterdelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/delegate)*