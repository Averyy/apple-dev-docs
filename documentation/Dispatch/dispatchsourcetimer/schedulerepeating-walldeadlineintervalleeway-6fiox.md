# scheduleRepeating(wallDeadline:interval:leeway:)

**Framework**: Dispatch  
**Kind**: method

Schedules a repeating timer with the specified time, repeat interval, and leeway values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift ?+

## Declaration

```swift
func scheduleRepeating(wallDeadline: DispatchWallTime, interval: Double, leeway: DispatchTimeInterval = .nanoseconds(0))
```

#### Discussion

The system may defer the deliver of timer events to improve power consumption and system performance. The first time the timer fires, the maximum allowable delay is equal to the value in the `leeway` parameter. For subsequent firings, the timer fires at `wallDeadline + (n * repeating)`, and the maximum delay is equal to `min(leeway, repeating/2)`—that is, the smaller of either the `leeway` value or half the value in the `repeating` parameter.

The system may fire a timer sooner than the value in the `wallDeadline` parameter. If you created the timer with the [`strict`](dispatchsource/timerflags/strict.md) flag, the system makes every effort to observe the provided `leeway` value, even if it is smaller than the current lower limit.

Calling this method on a cancelled dispatch source has no effect.

## Parameters

- `wallDeadline`: The time at which to execute the dispatch source’s event handler.
- `interval`: The repeat interval for the timer, specified as a DispatchTimeInterval value. Specify DispatchTimeInterval.never if you want the timer to fire only once.
- `leeway`: The maximum amount of time after   by which the system may delay the delivery of the timer event.

## See Also

- [func scheduleOneshot(deadline: DispatchTime, leeway: DispatchTimeInterval)](dispatchsourcetimer/scheduleoneshot(deadline:leeway:).md)
  Schedules a timer to fire once with the specified deadline and leeway values.
- [func scheduleOneshot(wallDeadline: DispatchWallTime, leeway: DispatchTimeInterval)](dispatchsourcetimer/scheduleoneshot(walldeadline:leeway:).md)
  Schedules a timer to fire once with the specified deadline and leeway values.
- [func scheduleRepeating(deadline: DispatchTime, interval: DispatchTimeInterval, leeway: DispatchTimeInterval)](dispatchsourcetimer/schedulerepeating(deadline:interval:leeway:)-3k199.md)
  Schedules a repeating timer with the specified deadline, repeat interval, and leeway values.
- [func scheduleRepeating(deadline: DispatchTime, interval: Double, leeway: DispatchTimeInterval)](dispatchsourcetimer/schedulerepeating(deadline:interval:leeway:)-4wtot.md)
  Schedules a repeating timer with the specified deadline, repeat interval, and leeway values.
- [func scheduleRepeating(wallDeadline: DispatchWallTime, interval: DispatchTimeInterval, leeway: DispatchTimeInterval)](dispatchsourcetimer/schedulerepeating(walldeadline:interval:leeway:)-942p7.md)
  Schedules a repeating timer with the specified time, repeat interval, and leeway values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourcetimer/schedulerepeating(walldeadline:interval:leeway:)-6fiox)*