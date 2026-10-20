# scheduledTimer(timeInterval:invocation:repeats:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a new timer and schedules it on the current run loop in the default mode.

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
class func scheduledTimer(timeInterval ti: TimeInterval, invocation: NSInvocation, repeats yesOrNo: Bool) -> Timer
```

```objc
+ (NSTimer *) scheduledTimerWithTimeInterval:(NSTimeInterval) ti invocation:(NSInvocation *) invocation repeats:(BOOL) yesOrNo;
```

#### Return Value

A new `NSTimer` object, configured according to the specified parameters.

#### Discussion

After `ti` seconds have elapsed, the timer fires, invoking `invocation`.

## Parameters

- `ti`: The number of seconds between firings of the timer. If `ti` is less than or equal to `0.0`, this method chooses the nonnegative value of `0.0001` seconds instead.
- `invocation`: The invocation to use when the timer fires. The invocation object maintains a strong reference to its arguments until the timer is invalidated.
- `yesOrNo`: If [`true`](../../Swift/true.md), the timer will repeatedly reschedule itself until invalidated. If [`false`](../../Swift/false.md), the timer will be invalidated after it fires.

## See Also

### Related Documentation
- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [Timer Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Timers/Timers.html#//apple_ref/doc/uid/10000061i)
### Creating a Timer
- [class func scheduledTimer(withTimeInterval: TimeInterval, repeats: Bool, block: (Timer) -> Void) -> Timer](./scheduledtimer%28withtimeinterval,repeats,block%29.md)
  Creates a timer and schedules it on the current run loop in the default mode.
- [class func scheduledTimer(timeInterval: TimeInterval, target: Any, selector: Selector, userInfo: Any?, repeats: Bool) -> Timer](./scheduledtimer%28timeinterval,target,selector,userinfo,repeats%29.md)
  Creates a timer and schedules it on the current run loop in the default mode.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/scheduledtimer(timeinterval:invocation:repeats:))*