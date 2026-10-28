# scheduledTimer(withTimeInterval:repeats:block:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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
class func scheduledTimer(withTimeInterval interval: TimeInterval, repeats: Bool, block: @escaping @Sendable (Timer) -> Void) -> Timer
```

```objc
+ (NSTimer *) scheduledTimerWithTimeInterval:(NSTimeInterval) interval repeats:(BOOL) repeats block:(void (^)(NSTimer *timer)) block;
```

## Return Value

A new `NSTimer` object, configured according to the specified parameters.

## Discussion

After `interval` seconds have elapsed, the timer fires, executing `block`.

## Parameters

- `interval`: The number of seconds between firings of the timer. If `interval` is less than or equal to `0.0`, this method chooses the nonnegative value of `0.0001` seconds instead.
- `repeats`: If `true`, the timer will repeatedly reschedule itself until invalidated. If `false`, the timer will be invalidated after it fires.
- `block`: A block to be executed when the timer fires.

  The block takes a single `NSTimer` parameter and has no return value.

## See Also

### Creating a Timer
- [class func scheduledTimer(timeInterval: TimeInterval, target: Any, selector: Selector, userInfo: Any?, repeats: Bool) -> Timer](./scheduledtimer%28timeinterval,target,selector,userinfo,repeats%29.md)
  Creates a timer and schedules it on the current run loop in the default mode.
- [class func scheduledTimer(timeInterval: TimeInterval, invocation: NSInvocation, repeats: Bool) -> Timer](./scheduledtimer%28timeinterval,invocation,repeats%29.md)
  Creates a new timer and schedules it on the current run loop in the default mode.
- [init(timeInterval: TimeInterval, repeats: Bool, block: (Timer) -> Void)](./init%28timeinterval,repeats,block%29.md)
  Initializes a timer object with the specified time interval and block.
- [init(timeInterval: TimeInterval, target: Any, selector: Selector, userInfo: Any?, repeats: Bool)](./init%28timeinterval,target,selector,userinfo,repeats%29.md)
  Initializes a timer object with the specified object and selector.
- [init(timeInterval: TimeInterval, invocation: NSInvocation, repeats: Bool)](./init%28timeinterval,invocation,repeats%29.md)
  Initializes a timer object with the specified invocation object.
- [convenience init(fire: Date, interval: TimeInterval, repeats: Bool, block: (Timer) -> Void)](./init%28fire,interval,repeats,block%29.md)
  Initializes a timer for the specified date and time interval with the specified block.
- [init(fireAt: Date, interval: TimeInterval, target: Any, selector: Selector, userInfo: Any?, repeats: Bool)](./init%28fireat,interval,target,selector,userinfo,repeats%29.md)
  Initializes a timer using the specified object and selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/scheduledtimer(withtimeinterval:repeats:block:))*