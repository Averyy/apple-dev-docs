# Scheduler Implementations

**Framework**: Foundation  
**Role**: API Collection

## Topics

### Structures
- [RunLoop.SchedulerOptions](./scheduleroptions.md)
  A set of options that affect the operation of the run loop scheduler.
- [RunLoop.SchedulerTimeType](./schedulertimetype.md)
  The scheduler time type that the run loop uses.
### Instance Properties
- [var minimumTolerance: RunLoop.SchedulerTimeType.Stride](./minimumtolerance.md)
  The minimum tolerance the run loop scheduler allows.
- [var now: RunLoop.SchedulerTimeType](./now.md)
  The run loop scheduler’s definition of the current moment in time.
### Instance Methods
- [func schedule(after: RunLoop.SchedulerTimeType, interval: RunLoop.SchedulerTimeType.Stride, tolerance: RunLoop.SchedulerTimeType.Stride, options: RunLoop.SchedulerOptions?, () -> Void) -> any Cancellable](./schedule%28after,interval,tolerance,options,_%29.md)
  Performs the action at some time after the specified date, at the specified frequency, using the specified tolerance and options.
- [func schedule(after: RunLoop.SchedulerTimeType, tolerance: RunLoop.SchedulerTimeType.Stride, options: RunLoop.SchedulerOptions?, () -> Void)](./schedule%28after,tolerance,options,_%29.md)
  Performs the action at some time after the specified date, using the specified tolerance and options.
- [func schedule(options: RunLoop.SchedulerOptions?, () -> Void)](./schedule%28options,_%29.md)
  Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/scheduler-implementations)*