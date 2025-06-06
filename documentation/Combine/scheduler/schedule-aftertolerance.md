# schedule(after:tolerance:_:)

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
func schedule(after date: Self.SchedulerTimeType, tolerance: Self.SchedulerTimeType.Stride, _ action: @escaping () -> Void)
```

#### Discussion

The immediate scheduler ignores `date` and performs the action immediately.

## See Also

- [func schedule(() -> Void)](scheduler/schedule(_:).md)
  Performs the action at the next possible opportunity, without options.
- [func schedule(after: Self.SchedulerTimeType, () -> Void)](scheduler/schedule(after:_:).md)
  Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [func schedule(after: Self.SchedulerTimeType, interval: Self.SchedulerTimeType.Stride, () -> Void) -> any Cancellable](scheduler/schedule(after:interval:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, using minimum tolerance possible for this Scheduler.
- [func schedule(after: Self.SchedulerTimeType, interval: Self.SchedulerTimeType.Stride, tolerance: Self.SchedulerTimeType.Stride, () -> Void) -> any Cancellable](scheduler/schedule(after:interval:tolerance:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, taking into account tolerance if possible.
- [func schedule(after: Self.SchedulerTimeType, interval: Self.SchedulerTimeType.Stride, tolerance: Self.SchedulerTimeType.Stride, options: Self.SchedulerOptions?, () -> Void) -> any Cancellable](scheduler/schedule(after:interval:tolerance:options:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [func schedule(after: Self.SchedulerTimeType, tolerance: Self.SchedulerTimeType.Stride, options: Self.SchedulerOptions?, () -> Void)](scheduler/schedule(after:tolerance:options:_:).md)
  Performs the action at some time after the specified date.
- [func schedule(options: Self.SchedulerOptions?, () -> Void)](scheduler/schedule(options:_:).md)
  Performs the action at the next possible opportunity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/scheduler/schedule(after:tolerance:_:))*