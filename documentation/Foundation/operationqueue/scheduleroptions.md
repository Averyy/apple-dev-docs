# OperationQueue.SchedulerOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that defines options the operation queue accepts.

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

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Scheduling Operations
- [func schedule(after: OperationQueue.SchedulerTimeType, tolerance: OperationQueue.SchedulerTimeType.Stride, options: OperationQueue.SchedulerOptions?, () -> Void)](./schedule%28after,tolerance,options,_%29.md)
  Performs the action at some time after the specified date, optionally taking into account tolerance if possible.
- [func schedule(after: OperationQueue.SchedulerTimeType, interval: OperationQueue.SchedulerTimeType.Stride, tolerance: OperationQueue.SchedulerTimeType.Stride, options: OperationQueue.SchedulerOptions?, () -> Void) -> any Cancellable](./schedule%28after,interval,tolerance,options,_%29.md)
  Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [func schedule(options: OperationQueue.SchedulerOptions?, () -> Void)](./schedule%28options,_%29.md)
  Performs the action at the next possible opportunity.
- [var now: OperationQueue.SchedulerTimeType](./now.md)
  The operation queue’s definition of the current moment in time.
- [var minimumTolerance: OperationQueue.SchedulerTimeType.Stride](./minimumtolerance.md)
  The minimum tolerance the dispatch queue scheduler allows.
- [OperationQueue.SchedulerTimeType](./schedulertimetype.md)
  The scheduler time type the operation queue uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/scheduleroptions)*