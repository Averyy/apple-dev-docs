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
- [Comparable](../Swift/Comparable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [Strideable](../Swift/Strideable.md)

## See Also

- [OperationQueue.SchedulerOptions](operationqueue/scheduleroptions.md)
  A type that defines options the operation queue accepts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/schedulertimetype)*