# forType(_:)

**Framework**: Foundation  
**Kind**: method

Returns the distributed notification center for a particular notification center type.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class func forType(_ notificationCenterType: DistributedNotificationCenter.CenterType) -> DistributedNotificationCenter
```

#### Return Value

Distributed notification center for `notificationCenterType`.

#### Discussion

Currently only one type, `NSLocalNotificationCenterType`, is supported.

## Parameters

- `notificationCenterType`: Notification center type being inquired about.

## See Also

- [class func `default`() -> DistributedNotificationCenter](distributednotificationcenter/default.md)
  Returns the default distributed notification center, representing the local notification center for the computer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/fortype(_:))*