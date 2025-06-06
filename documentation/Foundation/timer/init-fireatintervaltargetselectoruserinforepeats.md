# init(fireAt:interval:target:selector:userInfo:repeats:)

**Framework**: Foundation  
**Kind**: init

Initializes a timer using the specified object and selector.

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
init(fireAt date: Date, interval ti: TimeInterval, target t: Any, selector s: Selector, userInfo ui: Any?, repeats rep: Bool)
```

#### Return Value

The receiver, initialized such that, when added to a run loop, it will fire at `date` and then, if `repeats` is [`true`](https://developer.apple.com/documentation/swift/true), every `ti` after that.

#### Discussion

You must add the new timer to a run loop, using [`add(_:forMode:)`](runloop/add(_:formode:)-392ag.md). Upon firing, the timer sends the message `aSelector` to `target`. (If the timer is configured to repeat, there is no need to subsequently re-add the timer to the run loop.)

## Parameters

- `date`: The time at which the timer should first fire.
- `ti`: For a repeating timer, this parameter contains the number of seconds between firings of the timer. If   is less than or equal to  , this method chooses the nonnegative value of   seconds instead.
- `t`: The object to which to send the message specified by   when the timer fires. The timer maintains a strong reference to this object until it (the timer) is invalidated.
- `s`: The selector should have the following signature:   (including a colon to indicate that the method takes an argument). The timer passes itself as the argument, thus the method would adopt the following pattern:
- `ui`: Custom user info for the timer. The timer maintains a strong reference to this object until it (the timer) is invalidated. This parameter may be  .
- `rep`: If  , the timer will repeatedly reschedule itself until invalidated. If  , the timer will be invalidated after it fires.

## See Also

- [class func scheduledTimer(withTimeInterval: TimeInterval, repeats: Bool, block: (Timer) -> Void) -> Timer](timer/scheduledtimer(withtimeinterval:repeats:block:).md)
  Creates a timer and schedules it on the current run loop in the default mode.
- [class func scheduledTimer(timeInterval: TimeInterval, target: Any, selector: Selector, userInfo: Any?, repeats: Bool) -> Timer](timer/scheduledtimer(timeinterval:target:selector:userinfo:repeats:).md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/init(fireat:interval:target:selector:userinfo:repeats:))*