# schedule(after:tolerance:options:_:)

**Framework**: Foundation  
**Kind**: method

Performs the action at some time after the specified date, using the specified tolerance and options.

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
func schedule(after date: RunLoop.SchedulerTimeType, tolerance: RunLoop.SchedulerTimeType.Stride, options: RunLoop.SchedulerOptions?, _ action: @escaping () -> Void)
```

## See Also

- [func schedule(options: RunLoop.SchedulerOptions?, () -> Void)](runloop/schedule(options:_:).md)
  Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [func schedule(after: RunLoop.SchedulerTimeType, interval: RunLoop.SchedulerTimeType.Stride, tolerance: RunLoop.SchedulerTimeType.Stride, options: RunLoop.SchedulerOptions?, () -> Void) -> any Cancellable](runloop/schedule(after:interval:tolerance:options:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, using the specified tolerance and options.
- [var minimumTolerance: RunLoop.SchedulerTimeType.Stride](runloop/minimumtolerance.md)
  The minimum tolerance the run loop scheduler allows.
- [var now: RunLoop.SchedulerTimeType](runloop/now.md)
  The run loop scheduler’s definition of the current moment in time.
- [RunLoop.SchedulerTimeType](runloop/schedulertimetype.md)
  The scheduler time type that the run loop uses.
- [RunLoop.SchedulerOptions](runloop/scheduleroptions.md)
  A set of options that affect the operation of the run loop scheduler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/schedule(after:tolerance:options:_:))*