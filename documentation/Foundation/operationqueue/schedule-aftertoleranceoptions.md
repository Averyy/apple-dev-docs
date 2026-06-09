# schedule(after:tolerance:options:_:)

**Framework**: Foundation  
**Kind**: method

Performs the action at some time after the specified date, optionally taking into account tolerance if possible.

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
func schedule(after date: OperationQueue.SchedulerTimeType, tolerance: OperationQueue.SchedulerTimeType.Stride, options: OperationQueue.SchedulerOptions?, _ action: @escaping () -> Void)
```

## See Also

- [func schedule(after: OperationQueue.SchedulerTimeType, interval: OperationQueue.SchedulerTimeType.Stride, tolerance: OperationQueue.SchedulerTimeType.Stride, options: OperationQueue.SchedulerOptions?, () -> Void) -> any Cancellable](operationqueue/schedule(after:interval:tolerance:options:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [func schedule(options: OperationQueue.SchedulerOptions?, () -> Void)](operationqueue/schedule(options:_:).md)
  Performs the action at the next possible opportunity.
- [var now: OperationQueue.SchedulerTimeType](operationqueue/now.md)
  The operation queue’s definition of the current moment in time.
- [var minimumTolerance: OperationQueue.SchedulerTimeType.Stride](operationqueue/minimumtolerance.md)
  The minimum tolerance the dispatch queue scheduler allows.
- [OperationQueue.SchedulerTimeType](operationqueue/schedulertimetype.md)
  The scheduler time type the operation queue uses.
- [OperationQueue.SchedulerOptions](operationqueue/scheduleroptions.md)
  A type that defines options the operation queue accepts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/schedule(after:tolerance:options:_:))*