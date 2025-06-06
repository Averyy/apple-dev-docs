# schedule(wallDeadline:repeating:leeway:)

**Framework**: Dispatch  
**Kind**: method

Schedules a timer with the specified time, repeat interval, and leeway values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 4.0+

## Declaration

```swift
func schedule(wallDeadline: DispatchWallTime, repeating interval: DispatchTimeInterval = .never, leeway: DispatchTimeInterval = .nanoseconds(0))
```

#### Discussion

The system may defer the deliver of timer events to improve power consumption and system performance. The first time the timer fires, the maximum allowable delay is equal to the value in the `leeway` parameter. For subsequent firings of a repeating timer, the timer fires at `wallDeadline + (n * repeating)`, and the maximum delay is equal to `min(leeway, repeating/2)`—that is, the smaller of either the `leeway` value or half the value in the `repeating` parameter.

The system may fire a timer sooner than the value in the `wallDeadline` parameter. If you created the timer with the [`strict`](dispatchsource/timerflags/strict.md) flag, the system makes every effort to observe the provided `leeway` value, even if it is smaller than the current lower limit.

Calling this method on a cancelled dispatch source has no effect.

## Parameters

- `wallDeadline`: The time at which to execute the dispatch source’s event handler.
- `interval`: The repeat interval for the timer, specified as a   value. Specify   if you want the timer to fire only once.
- `leeway`: The maximum amount of time after   by which the system may delay the delivery of the timer event.

## See Also

- [func schedule(deadline: DispatchTime, repeating: DispatchTimeInterval, leeway: DispatchTimeInterval)](dispatchsourcetimer/schedule(deadline:repeating:leeway:)-hvhp.md)
  Schedules a timer with the specified deadline, repeat interval, and leeway values.
- [func schedule(deadline: DispatchTime, repeating: Double, leeway: DispatchTimeInterval)](dispatchsourcetimer/schedule(deadline:repeating:leeway:)-24w9r.md)
  Schedules a timer with the specified deadline, repeat interval, and leeway values.
- [func schedule(wallDeadline: DispatchWallTime, repeating: Double, leeway: DispatchTimeInterval)](dispatchsourcetimer/schedule(walldeadline:repeating:leeway:)-21bay.md)
  Schedules a timer with the specified time, repeat interval, and leeway values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourcetimer/schedule(walldeadline:repeating:leeway:)-7c4d7)*