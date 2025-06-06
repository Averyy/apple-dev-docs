# init(fire:interval:repeats:block:)

**Framework**: Foundation  
**Kind**: init

Initializes a timer for the specified date and time interval with the specified block.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(fire date: Date, interval: TimeInterval, repeats: Bool, block: @escaping (Timer) -> Void)
```

#### Return Value

A new [`Timer`](timer.md) object, configured according to the specified parameters.

#### Discussion

You must add the new timer to a run loop, using [`add(_:forMode:)`](runloop/add(_:formode:)-392ag.md). Upon firing, after `interval` seconds have elapsed, the timer fires, executing `block`. (If the timer is configured to repeat, you don’t need to add the timer to the run loop again.)

## Parameters

- `date`: The time at which the timer should first fire.
- `interval`: For a repeating timer, this parameter contains the number of seconds between firings of the timer. If   is less than or equal to  , this method chooses the nonnegative value of   seconds instead.
- `repeats`: If  , the timer will repeatedly reschedule itself until invalidated. If  , the timer will be invalidated after it fires.
- `block`: A block to be executed when the timer fires. The block takes a single   parameter and has no return value.

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
- [init(fireAt: Date, interval: TimeInterval, target: Any, selector: Selector, userInfo: Any?, repeats: Bool)](timer/init(fireat:interval:target:selector:userinfo:repeats:).md)
  Initializes a timer using the specified object and selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/init(fire:interval:repeats:block:))*