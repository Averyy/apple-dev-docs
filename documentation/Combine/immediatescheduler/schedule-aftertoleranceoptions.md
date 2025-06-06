# schedule(after:tolerance:options:_:)

**Framework**: Combine  
**Kind**: method

Performs the action at some time after the specified date.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func schedule(after date: ImmediateScheduler.SchedulerTimeType, tolerance: ImmediateScheduler.SchedulerTimeType.Stride, options: ImmediateScheduler.SchedulerOptions?, _ action: @escaping () -> Void)
```

#### Discussion

The immediate scheduler ignores `date` and performs the action immediately.

## See Also

- [func schedule(() -> Void)](immediatescheduler/schedule(_:).md)
  Performs the action at the next possible opportunity, without options.
- [func schedule(after: Self.SchedulerTimeType, () -> Void)](immediatescheduler/schedule(after:_:).md)
  Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [func schedule(after: Self.SchedulerTimeType, interval: Self.SchedulerTimeType.Stride, () -> Void) -> any Cancellable](immediatescheduler/schedule(after:interval:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, using minimum tolerance possible for this Scheduler.
- [func schedule(after: Self.SchedulerTimeType, interval: Self.SchedulerTimeType.Stride, tolerance: Self.SchedulerTimeType.Stride, () -> Void) -> any Cancellable](immediatescheduler/schedule(after:interval:tolerance:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, taking into account tolerance if possible.
- [func schedule(after: ImmediateScheduler.SchedulerTimeType, interval: ImmediateScheduler.SchedulerTimeType.Stride, tolerance: ImmediateScheduler.SchedulerTimeType.Stride, options: ImmediateScheduler.SchedulerOptions?, () -> Void) -> any Cancellable](immediatescheduler/schedule(after:interval:tolerance:options:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [func schedule(after: Self.SchedulerTimeType, tolerance: Self.SchedulerTimeType.Stride, () -> Void)](immediatescheduler/schedule(after:tolerance:_:).md)
  Performs the action at some time after the specified date.
- [func schedule(options: ImmediateScheduler.SchedulerOptions?, () -> Void)](immediatescheduler/schedule(options:_:).md)
  Performs the action at the next possible opportunity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler/schedule(after:tolerance:options:_:))*