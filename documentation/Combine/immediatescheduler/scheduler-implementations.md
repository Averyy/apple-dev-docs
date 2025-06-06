# Scheduler Implementations

**Framework**: Combine

## Topics

### Instance Methods
- [func schedule(() -> Void)](immediatescheduler/schedule(_:).md)
  Performs the action at the next possible opportunity, without options.
- [func schedule(after: Self.SchedulerTimeType, () -> Void)](immediatescheduler/schedule(after:_:).md)
  Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [func schedule(after: Self.SchedulerTimeType, interval: Self.SchedulerTimeType.Stride, () -> Void) -> any Cancellable](immediatescheduler/schedule(after:interval:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, using minimum tolerance possible for this Scheduler.
- [func schedule(after: Self.SchedulerTimeType, interval: Self.SchedulerTimeType.Stride, tolerance: Self.SchedulerTimeType.Stride, () -> Void) -> any Cancellable](immediatescheduler/schedule(after:interval:tolerance:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, taking into account tolerance if possible.
- [func schedule(after: Self.SchedulerTimeType, tolerance: Self.SchedulerTimeType.Stride, () -> Void)](immediatescheduler/schedule(after:tolerance:_:).md)
  Performs the action at some time after the specified date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler/scheduler-implementations)*