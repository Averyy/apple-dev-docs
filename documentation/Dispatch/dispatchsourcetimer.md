# DispatchSourceTimer

**Framework**: Dispatch  
**Kind**: protocol

A dispatch source that submits the event handler block based on a timer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol DispatchSourceTimer : DispatchSourceProtocol, Sendable
```

#### Overview

You do not adopt this protocol in your objects. Instead, use the [`makeTimerSource(flags:queue:)`](dispatchsource/maketimersource(flags:queue:).md) method to create an object that adopts this protocol.

## Topics

### Scheduling the Timer Trigger Conditions
- [func schedule(deadline: DispatchTime, repeating: DispatchTimeInterval, leeway: DispatchTimeInterval)](dispatchsourcetimer/schedule(deadline:repeating:leeway:)-hvhp.md)
  Schedules a timer with the specified deadline, repeat interval, and leeway values.
- [func schedule(deadline: DispatchTime, repeating: Double, leeway: DispatchTimeInterval)](dispatchsourcetimer/schedule(deadline:repeating:leeway:)-24w9r.md)
  Schedules a timer with the specified deadline, repeat interval, and leeway values.
- [func schedule(wallDeadline: DispatchWallTime, repeating: DispatchTimeInterval, leeway: DispatchTimeInterval)](dispatchsourcetimer/schedule(walldeadline:repeating:leeway:)-7c4d7.md)
  Schedules a timer with the specified time, repeat interval, and leeway values.
- [func schedule(wallDeadline: DispatchWallTime, repeating: Double, leeway: DispatchTimeInterval)](dispatchsourcetimer/schedule(walldeadline:repeating:leeway:)-21bay.md)
  Schedules a timer with the specified time, repeat interval, and leeway values.
### Deprecated
- [func scheduleOneshot(deadline: DispatchTime, leeway: DispatchTimeInterval)](dispatchsourcetimer/scheduleoneshot(deadline:leeway:).md)
  Schedules a timer to fire once with the specified deadline and leeway values.
- [func scheduleOneshot(wallDeadline: DispatchWallTime, leeway: DispatchTimeInterval)](dispatchsourcetimer/scheduleoneshot(walldeadline:leeway:).md)
  Schedules a timer to fire once with the specified deadline and leeway values.
- [func scheduleRepeating(deadline: DispatchTime, interval: DispatchTimeInterval, leeway: DispatchTimeInterval)](dispatchsourcetimer/schedulerepeating(deadline:interval:leeway:)-3k199.md)
  Schedules a repeating timer with the specified deadline, repeat interval, and leeway values.
- [func scheduleRepeating(deadline: DispatchTime, interval: Double, leeway: DispatchTimeInterval)](dispatchsourcetimer/schedulerepeating(deadline:interval:leeway:)-4wtot.md)
  Schedules a repeating timer with the specified deadline, repeat interval, and leeway values.
- [func scheduleRepeating(wallDeadline: DispatchWallTime, interval: Double, leeway: DispatchTimeInterval)](dispatchsourcetimer/schedulerepeating(walldeadline:interval:leeway:)-6fiox.md)
  Schedules a repeating timer with the specified time, repeat interval, and leeway values.
- [func scheduleRepeating(wallDeadline: DispatchWallTime, interval: DispatchTimeInterval, leeway: DispatchTimeInterval)](dispatchsourcetimer/schedulerepeating(walldeadline:interval:leeway:)-942p7.md)
  Schedules a repeating timer with the specified time, repeat interval, and leeway values.

## Relationships

### Inherits From
- [DispatchSourceProtocol](dispatchsourceprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [DispatchSource](dispatchsource.md)

## See Also

- [class func makeTimerSource(flags: DispatchSource.TimerFlags, queue: DispatchQueue?) -> any DispatchSourceTimer](dispatchsource/maketimersource(flags:queue:).md)
  Creates a new dispatch source object for monitoring timer events.
- [DispatchSource.TimerFlags](dispatchsource/timerflags.md)
  Flags to use when configuring a timer dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourcetimer)*