# schedule(options:_:)

**Framework**: Combine  
**Kind**: method

Performs the action at the next possible opportunity.

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
func schedule(options: ImmediateScheduler.SchedulerOptions?, _ action: @escaping () -> Void)
```

## See Also

- [func schedule(after: ImmediateScheduler.SchedulerTimeType, interval: ImmediateScheduler.SchedulerTimeType.Stride, tolerance: ImmediateScheduler.SchedulerTimeType.Stride, options: ImmediateScheduler.SchedulerOptions?, () -> Void) -> any Cancellable](immediatescheduler/schedule(after:interval:tolerance:options:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [func schedule(after: ImmediateScheduler.SchedulerTimeType, tolerance: ImmediateScheduler.SchedulerTimeType.Stride, options: ImmediateScheduler.SchedulerOptions?, () -> Void)](immediatescheduler/schedule(after:tolerance:options:_:).md)
  Performs the action at some time after the specified date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler/schedule(options:_:))*