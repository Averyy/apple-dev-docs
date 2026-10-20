# ImmediateScheduler.SchedulerTimeType.Stride

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

The increment by which the immediate scheduler counts time.

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

### Creating Scheduler Time Strides
- [init(Int)](./stride/init%28_%29.md)
  Creates an immediate scheduler time interval from the given time interval.
- [init?<T>(exactly: T)](./stride/init%28exactly%29.md)
  Creates an immediate scheduler time interval from a binary integer type.
- [init(floatLiteral: Double)](./stride/init%28floatliteral%29.md)
  Creates an immediate scheduler time interval from a floating-point seconds value.
- [init(integerLiteral: Int)](./stride/init%28integerliteral%29.md)
  Creates an immediate scheduler time interval from an integer seconds value.
### Creating Scheduler Time Strides from Seconds
- [static func microseconds(Int) -> ImmediateScheduler.SchedulerTimeType.Stride](./stride/microseconds%28_%29.md)
  Converts the specified number of microseconds into an instance of this scheduler time type.
- [static func milliseconds(Int) -> ImmediateScheduler.SchedulerTimeType.Stride](./stride/milliseconds%28_%29.md)
  Converts the specified number of milliseconds into an instance of this scheduler time type.
- [static func nanoseconds(Int) -> ImmediateScheduler.SchedulerTimeType.Stride](./stride/nanoseconds%28_%29.md)
  Converts the specified number of nanoseconds into an instance of this scheduler time type.
- [static func seconds(Double) -> ImmediateScheduler.SchedulerTimeType.Stride](./stride/seconds%28_%29-8lm65.md)
  Converts the specified number of seconds, as a floating-point value, into an instance of this scheduler time type.
- [static func seconds(Int) -> ImmediateScheduler.SchedulerTimeType.Stride](./stride/seconds%28_%29-9uwki.md)
  Converts the specified number of seconds into an instance of this scheduler time type.
### Declaring Timekeeping Types
- [ImmediateScheduler.SchedulerTimeType.Stride.FloatLiteralType](./stride/floatliteraltype.md)
  The type used when evaluating floating-point literals.
- [ImmediateScheduler.SchedulerTimeType.Stride.IntegerLiteralType](./stride/integerliteraltype.md)
  The type used when evaluating integer literals.
- [ImmediateScheduler.SchedulerTimeType.Stride.Magnitude](./stride/magnitude-swift.typealias.md)
  The type used for expressing the stride’s magnitude.
### Expressing Scheduler Time Strides as Seconds
- [var magnitude: Int](./stride/magnitude-swift.property.md)
  The value of this time interval in seconds.

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
- [SchedulerTimeIntervalConvertible](../../schedulertimeintervalconvertible.md)
- [SignedNumeric](../../../Swift/signednumeric.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype/stride)*