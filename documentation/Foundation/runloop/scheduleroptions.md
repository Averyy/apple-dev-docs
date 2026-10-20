# RunLoop.SchedulerOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A set of options that affect the operation of the run loop scheduler.

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
struct SchedulerOptions
```

#### Overview

The run loop doesn’t support any scheduler options.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Scheduling Combine Publishers
- [func schedule(options: RunLoop.SchedulerOptions?, () -> Void)](./schedule%28options,_%29.md)
  Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [func schedule(after: RunLoop.SchedulerTimeType, tolerance: RunLoop.SchedulerTimeType.Stride, options: RunLoop.SchedulerOptions?, () -> Void)](./schedule%28after,tolerance,options,_%29.md)
  Performs the action at some time after the specified date, using the specified tolerance and options.
- [func schedule(after: RunLoop.SchedulerTimeType, interval: RunLoop.SchedulerTimeType.Stride, tolerance: RunLoop.SchedulerTimeType.Stride, options: RunLoop.SchedulerOptions?, () -> Void) -> any Cancellable](./schedule%28after,interval,tolerance,options,_%29.md)
  Performs the action at some time after the specified date, at the specified frequency, using the specified tolerance and options.
- [var minimumTolerance: RunLoop.SchedulerTimeType.Stride](./minimumtolerance.md)
  The minimum tolerance the run loop scheduler allows.
- [var now: RunLoop.SchedulerTimeType](./now.md)
  The run loop scheduler’s definition of the current moment in time.
- [RunLoop.SchedulerTimeType](./schedulertimetype.md)
  The scheduler time type that the run loop uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/scheduleroptions)*