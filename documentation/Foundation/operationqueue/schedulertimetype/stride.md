# OperationQueue.SchedulerTimeType.Stride

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [var timeInterval: TimeInterval](./stride/timeinterval.md)
  The value of this time interval, in seconds.
- [var magnitude: TimeInterval](./stride/magnitude.md)
  The value of this time interval, in seconds.
### Creating Scheduler Time Strides
- [init(TimeInterval)](./stride/init%28_%29.md)
  Creates a stride using the specified time interval.
- [init?<T>(exactly: T)](./stride/init%28exactly%29.md)
  Creates a stride using the specified integer, if it can be represented exactly.
- [init(floatLiteral: TimeInterval)](./stride/init%28floatliteral%29.md)
  Creates a stride using the specified floating-point value.
- [init(integerLiteral: TimeInterval)](./stride/init%28integerliteral%29.md)
  Creates a stride using the specified integer value.

## Relationships

### Conforms To
- [AdditiveArithmetic](../../../Swift/additivearithmetic.md)
- [Comparable](../../../Swift/comparable.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [ExpressibleByFloatLiteral](../../../Swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../../../Swift/expressiblebyintegerliteral.md)
- [Numeric](../../../Swift/numeric.md)
- [SchedulerTimeIntervalConvertible](../../../Combine/schedulertimeintervalconvertible.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)
- [SignedNumeric](../../../Swift/signednumeric.md)

## See Also

### Managing Scheduler Time Type Properties
- [var date: Date](./date.md)
  The date this type represents.
- [func advanced(by: OperationQueue.SchedulerTimeType.Stride) -> OperationQueue.SchedulerTimeType](./advanced%28by%29.md)
  Calculates an operation queue scheduler time by advancing the scheduler time type’s date by the given interval.
- [func distance(to: OperationQueue.SchedulerTimeType) -> OperationQueue.SchedulerTimeType.Stride](./distance%28to%29.md)
  The distance to another operation queue scheduler time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/schedulertimetype/stride)*