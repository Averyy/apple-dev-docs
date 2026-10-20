# schedule(after:interval:tolerance:_:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Performs the action at some time after the specified date, at the specified frequency, taking into account tolerance if possible.

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
func schedule(after date: Self.SchedulerTimeType, interval: Self.SchedulerTimeType.Stride, tolerance: Self.SchedulerTimeType.Stride, _ action: @escaping () -> Void) -> any Cancellable
```

#### Discussion

The immediate scheduler ignores `date` and performs the action immediately.

## See Also

### Scheduling actions
- [func schedule(() -> Void)](./schedule%28_%29.md)
  Performs the action at the next possible opportunity, without options.
- [func schedule(after: Self.SchedulerTimeType, () -> Void)](./schedule%28after,_%29.md)
  Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [func schedule(after: Self.SchedulerTimeType, interval: Self.SchedulerTimeType.Stride, () -> Void) -> any Cancellable](./schedule%28after,interval,_%29.md)
  Performs the action at some time after the specified date, at the specified frequency, using minimum tolerance possible for this Scheduler.
- [func schedule(after: Self.SchedulerTimeType, interval: Self.SchedulerTimeType.Stride, tolerance: Self.SchedulerTimeType.Stride, options: Self.SchedulerOptions?, () -> Void) -> any Cancellable](./schedule%28after,interval,tolerance,options,_%29.md)
  Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [func schedule(after: Self.SchedulerTimeType, tolerance: Self.SchedulerTimeType.Stride, () -> Void)](./schedule%28after,tolerance,_%29.md)
  Performs the action at some time after the specified date.
- [func schedule(after: Self.SchedulerTimeType, tolerance: Self.SchedulerTimeType.Stride, options: Self.SchedulerOptions?, () -> Void)](./schedule%28after,tolerance,options,_%29.md)
  Performs the action at some time after the specified date.
- [func schedule(options: Self.SchedulerOptions?, () -> Void)](./schedule%28options,_%29.md)
  Performs the action at the next possible opportunity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/scheduler/schedule(after:interval:tolerance:_:))*