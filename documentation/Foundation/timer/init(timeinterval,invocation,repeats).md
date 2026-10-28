# init(timeInterval:invocation:repeats:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a timer object with the specified invocation object.

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
init(timeInterval ti: TimeInterval, invocation: NSInvocation, repeats yesOrNo: Bool)
```

```objc
+ (NSTimer *) timerWithTimeInterval:(NSTimeInterval) ti invocation:(NSInvocation *) invocation repeats:(BOOL) yesOrNo;
```

## Return Value

A new `NSTimer` object, configured according to the specified parameters.

## Discussion

You must add the new timer to a run loop, using [`add(_:forMode:)`](../runloop/add%28_,formode%29-392ag.md). Then, after `ti` have elapsed, the timer fires, invoking `invocation`. (If the timer is configured to repeat, there is no need to subsequently re-add the timer to the run loop.)

## Parameters

- `ti`: The number of seconds between firings of the timer. If `ti` is less than or equal to `0.0`, this method chooses the nonnegative value of `0.0001` seconds instead.
- `invocation`: The invocation to use when the timer fires. The timer instructs the invocation object to maintain a strong reference to its arguments.
- `yesOrNo`: If [`true`](../../Swift/true.md), the timer will repeatedly reschedule itself until invalidated. If [`false`](../../Swift/false.md), the timer will be invalidated after it fires.

## See Also

### Creating a Timer
- [class func scheduledTimer(withTimeInterval: TimeInterval, repeats: Bool, block: (Timer) -> Void) -> Timer](./scheduledtimer%28withtimeinterval,repeats,block%29.md)
  Creates a timer and schedules it on the current run loop in the default mode.
- [class func scheduledTimer(timeInterval: TimeInterval, target: Any, selector: Selector, userInfo: Any?, repeats: Bool) -> Timer](./scheduledtimer%28timeinterval,target,selector,userinfo,repeats%29.md)
  Creates a timer and schedules it on the current run loop in the default mode.
- [class func scheduledTimer(timeInterval: TimeInterval, invocation: NSInvocation, repeats: Bool) -> Timer](./scheduledtimer%28timeinterval,invocation,repeats%29.md)
  Creates a new timer and schedules it on the current run loop in the default mode.
- [init(timeInterval: TimeInterval, repeats: Bool, block: (Timer) -> Void)](./init%28timeinterval,repeats,block%29.md)
  Initializes a timer object with the specified time interval and block.
- [init(timeInterval: TimeInterval, target: Any, selector: Selector, userInfo: Any?, repeats: Bool)](./init%28timeinterval,target,selector,userinfo,repeats%29.md)
  Initializes a timer object with the specified object and selector.
- [convenience init(fire: Date, interval: TimeInterval, repeats: Bool, block: (Timer) -> Void)](./init%28fire,interval,repeats,block%29.md)
  Initializes a timer for the specified date and time interval with the specified block.
- [init(fireAt: Date, interval: TimeInterval, target: Any, selector: Selector, userInfo: Any?, repeats: Bool)](./init%28fireat,interval,target,selector,userinfo,repeats%29.md)
  Initializes a timer using the specified object and selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/init(timeinterval:invocation:repeats:))*