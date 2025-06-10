# OperationQueue.SchedulerTimeType.Stride

**Framework**: Foundation  
**Kind**: struct

The interval by which operation queue times advance.

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
struct Stride
```

## Topics

### Managing Stride Properties
- [var timeInterval: TimeInterval](operationqueue/schedulertimetype/stride/timeinterval.md)
  The value of this time interval, in seconds.
- [var magnitude: TimeInterval](operationqueue/schedulertimetype/stride/magnitude.md)
  The value of this time interval, in seconds.
### Creating Scheduler Time Strides
- [init(TimeInterval)](operationqueue/schedulertimetype/stride/init(_:).md)
  Creates a stride using the specified time interval.

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/AdditiveArithmetic.md)
- [Comparable](../Swift/Comparable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
- [Numeric](../Swift/Numeric.md)
- [SchedulerTimeIntervalConvertible](../Combine/SchedulerTimeIntervalConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SignedNumeric](../Swift/SignedNumeric.md)

## See Also

- [var date: Date](operationqueue/schedulertimetype/date.md)
  The date this type represents.
- [func advanced(by: OperationQueue.SchedulerTimeType.Stride) -> OperationQueue.SchedulerTimeType](operationqueue/schedulertimetype/advanced(by:).md)
  Calculates an operation queue scheduler time by advancing the scheduler time type’s date by the given interval.
- [func distance(to: OperationQueue.SchedulerTimeType) -> OperationQueue.SchedulerTimeType.Stride](operationqueue/schedulertimetype/distance(to:).md)
  The distance to another operation queue scheduler time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/schedulertimetype/stride)*