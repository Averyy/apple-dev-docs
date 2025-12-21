# ImmediateScheduler.SchedulerTimeType.Stride

**Framework**: Combine  
**Kind**: struct

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
- [init(Int)](immediatescheduler/schedulertimetype/stride/init(_:).md)
  Creates an immediate scheduler time interval from the given time interval.
- [init?<T>(exactly: T)](immediatescheduler/schedulertimetype/stride/init(exactly:).md)
  Creates an immediate scheduler time interval from a binary integer type.
- [init(floatLiteral: Double)](immediatescheduler/schedulertimetype/stride/init(floatliteral:).md)
  Creates an immediate scheduler time interval from a floating-point seconds value.
- [init(integerLiteral: Int)](immediatescheduler/schedulertimetype/stride/init(integerliteral:).md)
  Creates an immediate scheduler time interval from an integer seconds value.
### Creating Scheduler Time Strides from Seconds
- [static func microseconds(Int) -> ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/stride/microseconds(_:).md)
  Converts the specified number of microseconds into an instance of this scheduler time type.
- [static func milliseconds(Int) -> ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/stride/milliseconds(_:).md)
  Converts the specified number of milliseconds into an instance of this scheduler time type.
- [static func nanoseconds(Int) -> ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/stride/nanoseconds(_:).md)
  Converts the specified number of nanoseconds into an instance of this scheduler time type.
- [static func seconds(Double) -> ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/stride/seconds(_:)-8lm65.md)
  Converts the specified number of seconds, as a floating-point value, into an instance of this scheduler time type.
- [static func seconds(Int) -> ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/stride/seconds(_:)-9uwki.md)
  Converts the specified number of seconds into an instance of this scheduler time type.
### Declaring Timekeeping Types
- [ImmediateScheduler.SchedulerTimeType.Stride.FloatLiteralType](immediatescheduler/schedulertimetype/stride/floatliteraltype.md)
  The type used when evaluating floating-point literals.
- [ImmediateScheduler.SchedulerTimeType.Stride.IntegerLiteralType](immediatescheduler/schedulertimetype/stride/integerliteraltype.md)
  The type used when evaluating integer literals.
- [ImmediateScheduler.SchedulerTimeType.Stride.Magnitude](immediatescheduler/schedulertimetype/stride/magnitude-swift.typealias.md)
  The type used for expressing the stride’s magnitude.
### Expressing Scheduler Time Strides as Seconds
- [var magnitude: Int](immediatescheduler/schedulertimetype/stride/magnitude-swift.property.md)
  The value of this time interval in seconds.

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
- [SchedulerTimeIntervalConvertible](schedulertimeintervalconvertible.md)
- [SignedNumeric](../Swift/SignedNumeric.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype/stride)*