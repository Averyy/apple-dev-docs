# scheduledTimer(withTimeInterval:repeats:block:)

**Framework**: Foundation  
**Kind**: method

Creates a timer and schedules it on the current run loop in the default mode.

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
class func scheduledTimer(withTimeInterval interval: TimeInterval, repeats: Bool, block: @escaping (Timer) -> Void) -> Timer
```

#### Return Value

A new `NSTimer` object, configured according to the specified parameters.

#### Discussion

After `interval` seconds have elapsed, the timer fires, executing `block`.

## Parameters

- `interval`: The number of seconds between firings of the timer. If   is less than or equal to  , this method chooses the nonnegative value of   seconds instead.
- `repeats`: If  , the timer will repeatedly reschedule itself until invalidated. If  , the timer will be invalidated after it fires.
- `block`: The block takes a single   parameter and has no return value.

## See Also

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
- [init(fireAt: Date, interval: TimeInterval, target: Any, selector: Selector, userInfo: Any?, repeats: Bool)](timer/init(fireat:interval:target:selector:userinfo:repeats:).md)
  Initializes a timer using the specified object and selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/scheduledtimer(withtimeinterval:repeats:block:))*