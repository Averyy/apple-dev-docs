# scheduledTimer(timeInterval:target:selector:userInfo:repeats:)

**Framework**: Foundation  
**Kind**: method

Creates a timer and schedules it on the current run loop in the default mode.

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
class func scheduledTimer(timeInterval ti: TimeInterval, target aTarget: Any, selector aSelector: Selector, userInfo: Any?, repeats yesOrNo: Bool) -> Timer
```

#### Return Value

A new `NSTimer` object, configured according to the specified parameters.

#### Discussion

After `ti` seconds have elapsed, the timer fires, sending the message `aSelector` to `target`.

## Parameters

- `ti`: The number of seconds between firings of the timer. If   is less than or equal to  , this method chooses the nonnegative value of   seconds instead.
- `aTarget`: The object to which to send the message specified by   when the timer fires. The timer maintains a strong reference to   until it (the timer) is invalidated.
- `aSelector`: The selector should have the following signature:   (including a colon to indicate that the method takes an argument). The timer passes itself as the argument, thus the method would adopt the following pattern:
- `userInfo`: The user info for the timer. The timer maintains a strong reference to this object until it (the timer) is invalidated. This parameter may be  .
- `yesOrNo`: If  , the timer will repeatedly reschedule itself until invalidated. If  , the timer will be invalidated after it fires.

## See Also

- [class func scheduledTimer(withTimeInterval: TimeInterval, repeats: Bool, block: (Timer) -> Void) -> Timer](timer/scheduledtimer(withtimeinterval:repeats:block:).md)
  Creates a timer and schedules it on the current run loop in the default mode.
- [class func scheduledTimer(timeInterval: TimeInterval, invocation: NSInvocation, repeats: Bool) -> Timer](timer/scheduledtimer(timeinterval:invocation:repeats:).md)
  Creates a new timer and schedules it on the current run loop in the default mode.
- [init(timeInterval: TimeInterval, repeats: Bool, block: (Timer) -> Void)](timer/init(timeinterval:repeats:block:).md)
  Initializes a timer object with the specified time interval and block.
- [init(timeInterval: TimeInterval, target: Any, selector: Selector, userInfo: Any?, repeats: Bool)](timer/init(timeinterval:target:selector:userinfo:repeats:).md)
  Initializes a timer object with the specified object and selector.
- [init(timeInterval: TimeInterval, invocation: NSInvocation, repeats: Bool)](timer/init(timeinterval:invocation:repeats:).md)
  Initializes a timer object with the specified invocation object.
- [convenience init(fire: Date, interval: TimeInterval, repeats: Bool, block: (Timer) -> Void)](timer/init(fire:interval:repeats:block:).md)
  Initializes a timer for the specified date and time interval with the specified block.
- [init(fireAt: Date, interval: TimeInterval, target: Any, selector: Selector, userInfo: Any?, repeats: Bool)](timer/init(fireat:interval:target:selector:userinfo:repeats:).md)
  Initializes a timer using the specified object and selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/scheduledtimer(timeinterval:target:selector:userinfo:repeats:))*