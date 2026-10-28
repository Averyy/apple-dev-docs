# scheduledTimer(timeInterval:target:selector:userInfo:repeats:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSTimer *) scheduledTimerWithTimeInterval:(NSTimeInterval) ti target:(id) aTarget selector:(SEL) aSelector userInfo:(id) userInfo repeats:(BOOL) yesOrNo;
```

## Return Value

A new `NSTimer` object, configured according to the specified parameters.

## Discussion

After `ti` seconds have elapsed, the timer fires, sending the message `aSelector` to `target`.

## Parameters

- `ti`: The number of seconds between firings of the timer. If `ti` is less than or equal to `0.0`, this method chooses the nonnegative value of `0.0001` seconds instead.
- `aTarget`: The object to which to send the message specified by `aSelector` when the timer fires. The timer maintains a strong reference to `target` until it (the timer) is invalidated.
- `aSelector`: The message to send to `target` when the timer fires.

  The selector should have the following signature: `timerFireMethod:` (including a colon to indicate that the method takes an argument). The timer passes itself as the argument, thus the method would adopt the following pattern:

  ```objc
  - (void)timerFireMethod:(NSTimer *)timer
  ```
- `userInfo`: The user info for the timer. The timer maintains a strong reference to this object until it (the timer) is invalidated. This parameter may be `nil`.
- `yesOrNo`: If [`true`](../../Swift/true.md), the timer will repeatedly reschedule itself until invalidated. If [`false`](../../Swift/false.md), the timer will be invalidated after it fires.

## See Also

### Creating a Timer
- [class func scheduledTimer(withTimeInterval: TimeInterval, repeats: Bool, block: (Timer) -> Void) -> Timer](./scheduledtimer%28withtimeinterval,repeats,block%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/scheduledtimer(timeinterval:target:selector:userinfo:repeats:))*