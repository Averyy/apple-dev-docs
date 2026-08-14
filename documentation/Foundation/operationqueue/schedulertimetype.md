# OperationQueue.SchedulerTimeType

**Framework**: Foundation  
**Kind**: struct

The scheduler time type the operation queue uses.

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
struct SchedulerTimeType
```

## Topics

### Creating Scheduler Time Types
- [init(Date)](operationqueue/schedulertimetype/init(_:).md)
  Creates an operation queue scheduler time with the given date.
### Managing Scheduler Time Type Properties
- [var date: Date](operationqueue/schedulertimetype/date.md)
  The date this type represents.
- [func advanced(by: OperationQueue.SchedulerTimeType.Stride) -> OperationQueue.SchedulerTimeType](operationqueue/schedulertimetype/advanced(by:).md)
  Calculates an operation queue scheduler time by advancing the scheduler time type’s date by the given interval.
- [func distance(to: OperationQueue.SchedulerTimeType) -> OperationQueue.SchedulerTimeType.Stride](operationqueue/schedulertimetype/distance(to:).md)
  The distance to another operation queue scheduler time.
- [OperationQueue.SchedulerTimeType.Stride](operationqueue/schedulertimetype/stride.md)
  The interval by which operation queue times advance.

## Relationships

### Conforms To
- [Comparable](../swift/comparable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Strideable](../swift/strideable.md)

## See Also

- [func schedule(after: OperationQueue.SchedulerTimeType, tolerance: OperationQueue.SchedulerTimeType.Stride, options: OperationQueue.SchedulerOptions?, () -> Void)](operationqueue/schedule(after:tolerance:options:_:).md)
  Performs the action at some time after the specified date, optionally taking into account tolerance if possible.
- [func schedule(after: OperationQueue.SchedulerTimeType, interval: OperationQueue.SchedulerTimeType.Stride, tolerance: OperationQueue.SchedulerTimeType.Stride, options: OperationQueue.SchedulerOptions?, () -> Void) -> any Cancellable](operationqueue/schedule(after:interval:tolerance:options:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [func schedule(options: OperationQueue.SchedulerOptions?, () -> Void)](operationqueue/schedule(options:_:).md)
  Performs the action at the next possible opportunity.
- [var now: OperationQueue.SchedulerTimeType](operationqueue/now.md)
  The operation queue’s definition of the current moment in time.
- [var minimumTolerance: OperationQueue.SchedulerTimeType.Stride](operationqueue/minimumtolerance.md)
  The minimum tolerance the dispatch queue scheduler allows.
- [OperationQueue.SchedulerOptions](operationqueue/scheduleroptions.md)
  A type that defines options the operation queue accepts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/schedulertimetype)*