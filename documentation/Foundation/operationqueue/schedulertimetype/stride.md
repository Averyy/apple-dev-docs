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
- [init?<T>(exactly: T)](operationqueue/schedulertimetype/stride/init(exactly:).md)
  Creates a stride using the specified integer, if it can be represented exactly.
- [init(floatLiteral: TimeInterval)](operationqueue/schedulertimetype/stride/init(floatliteral:).md)
  Creates a stride using the specified floating-point value.
- [init(integerLiteral: TimeInterval)](operationqueue/schedulertimetype/stride/init(integerliteral:).md)
  Creates a stride using the specified integer value.

## Relationships

### Conforms To
- [AdditiveArithmetic](../swift/additivearithmetic.md)
- [Comparable](../swift/comparable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByFloatLiteral](../swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../swift/expressiblebyintegerliteral.md)
- [Numeric](../swift/numeric.md)
- [SchedulerTimeIntervalConvertible](../combine/schedulertimeintervalconvertible.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SignedNumeric](../swift/signednumeric.md)

## See Also

- [var date: Date](operationqueue/schedulertimetype/date.md)
  The date this type represents.
- [func advanced(by: OperationQueue.SchedulerTimeType.Stride) -> OperationQueue.SchedulerTimeType](operationqueue/schedulertimetype/advanced(by:).md)
  Calculates an operation queue scheduler time by advancing the scheduler time type’s date by the given interval.
- [func distance(to: OperationQueue.SchedulerTimeType) -> OperationQueue.SchedulerTimeType.Stride](operationqueue/schedulertimetype/distance(to:).md)
  The distance to another operation queue scheduler time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/schedulertimetype/stride)*