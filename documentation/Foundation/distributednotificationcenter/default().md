# default()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the default distributed notification center, representing the local notification center for the computer.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class func `default`() -> DistributedNotificationCenter
```

```objc
+ (NSDistributedNotificationCenter *) defaultCenter;
```

## Return Value

Default distributed notification center for the computer.

## Discussion

This method calls [`forType(_:)`](./fortype%28_%29.md) with an argument of `NSLocalNotificationCenterType`.

## See Also

### Related Documentation
- [Notification Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Introduction/introNotifications.html#//apple_ref/doc/uid/10000043i)
### Getting Distributed Notification Centers
- [class func forType(DistributedNotificationCenter.CenterType) -> DistributedNotificationCenter](./fortype%28_%29.md)
  Returns the distributed notification center for a particular notification center type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/default())*