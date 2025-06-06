# isValid

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the timer is currently valid.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isValid: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver is still capable of firing or [`false`](https://developer.apple.com/documentation/swift/false) if the timer has been invalidated and is no longer capable of firing.

## See Also

- [var fireDate: Date](timer/firedate.md)
  The date at which the timer will fire.
- [var timeInterval: TimeInterval](timer/timeinterval.md)
  The timer’s time interval, in seconds.
- [var userInfo: Any?](timer/userinfo.md)
  The receiver’s `userInfo` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/isvalid)*