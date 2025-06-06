# userInfo

**Framework**: Foundation  
**Kind**: property

The receiver’s `userInfo` object.

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
var userInfo: Any? { get }
```

#### Discussion

Do not access this property after the timer is invalidated. Use [`isValid`](timer/isvalid.md) to test whether the timer is valid.

## See Also

- [init(timeInterval: TimeInterval, target: Any, selector: Selector, userInfo: Any?, repeats: Bool)](timer/init(timeinterval:target:selector:userinfo:repeats:).md)
  Initializes a timer object with the specified object and selector.
- [class func scheduledTimer(timeInterval: TimeInterval, target: Any, selector: Selector, userInfo: Any?, repeats: Bool) -> Timer](timer/scheduledtimer(timeinterval:target:selector:userinfo:repeats:).md)
  Creates a timer and schedules it on the current run loop in the default mode.
- [func invalidate()](timer/invalidate.md)
  Stops the timer from ever firing again and requests its removal from its run loop.
- [var isValid: Bool](timer/isvalid.md)
  A Boolean value that indicates whether the timer is currently valid.
- [var fireDate: Date](timer/firedate.md)
  The date at which the timer will fire.
- [var timeInterval: TimeInterval](timer/timeinterval.md)
  The timer’s time interval, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/userinfo)*