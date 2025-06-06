# default()

**Framework**: Foundation  
**Kind**: method

Returns the default distributed notification center, representing the local notification center for the computer.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class func `default`() -> DistributedNotificationCenter
```

#### Return Value

Default distributed notification center for the computer.

#### Discussion

This method calls [`forType(_:)`](distributednotificationcenter/fortype(_:).md) with an argument of `NSLocalNotificationCenterType`.

## See Also

- [Notification Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Introduction/introNotifications.html#//apple_ref/doc/uid/10000043i)
- [class func forType(DistributedNotificationCenter.CenterType) -> DistributedNotificationCenter](distributednotificationcenter/fortype(_:).md)
  Returns the distributed notification center for a particular notification center type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/default())*