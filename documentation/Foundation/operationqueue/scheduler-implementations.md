# Scheduler Implementations

**Framework**: Foundation  
**Role**: API Collection

## Topics

### Structures
- [OperationQueue.SchedulerOptions](./scheduleroptions.md)
  A type that defines options the operation queue accepts.
- [OperationQueue.SchedulerTimeType](./schedulertimetype.md)
  The scheduler time type the operation queue uses.
### Instance Properties
- [var minimumTolerance: OperationQueue.SchedulerTimeType.Stride](./minimumtolerance.md)
  The minimum tolerance the dispatch queue scheduler allows.
- [var now: OperationQueue.SchedulerTimeType](./now.md)
  The operation queue’s definition of the current moment in time.
### Instance Methods
- [func schedule(after: OperationQueue.SchedulerTimeType, interval: OperationQueue.SchedulerTimeType.Stride, tolerance: OperationQueue.SchedulerTimeType.Stride, options: OperationQueue.SchedulerOptions?, () -> Void) -> any Cancellable](./schedule%28after,interval,tolerance,options,_%29.md)
  Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [func schedule(after: OperationQueue.SchedulerTimeType, tolerance: OperationQueue.SchedulerTimeType.Stride, options: OperationQueue.SchedulerOptions?, () -> Void)](./schedule%28after,tolerance,options,_%29.md)
  Performs the action at some time after the specified date, optionally taking into account tolerance if possible.
- [func schedule(options: OperationQueue.SchedulerOptions?, () -> Void)](./schedule%28options,_%29.md)
  Performs the action at the next possible opportunity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/scheduler-implementations)*