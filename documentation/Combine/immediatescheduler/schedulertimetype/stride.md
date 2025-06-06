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
- [init(from: any Decoder) throws](immediatescheduler/schedulertimetype/stride/init(from:).md)
  Creates a new instance by decoding from the given decoder.
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
### Using Predefined Scheduler Time Strides
- [static var zero: Self](immediatescheduler/schedulertimetype/stride/zero.md)
  The zero value.
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
### Creating Ranges
- [static func ... (Self) -> PartialRangeFrom<Self>](immediatescheduler/schedulertimetype/stride/'...(_:)-3ep4j.md)
  Returns a partial range extending upward from a lower bound.
- [static func ... (Self) -> PartialRangeThrough<Self>](immediatescheduler/schedulertimetype/stride/'...(_:)-4auj9.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self, Self) -> ClosedRange<Self>](immediatescheduler/schedulertimetype/stride/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
### Performing Mathematical Operations
- [func negate()](immediatescheduler/schedulertimetype/stride/negate.md)
  Replaces this value with its additive inverse.
- [static func * (ImmediateScheduler.SchedulerTimeType.Stride, ImmediateScheduler.SchedulerTimeType.Stride) -> ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/stride/*(_:_:).md)
  Multiplies two values and produces their product.
- [static func *= (inout ImmediateScheduler.SchedulerTimeType.Stride, ImmediateScheduler.SchedulerTimeType.Stride)](immediatescheduler/schedulertimetype/stride/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable.
- [static func + (Self) -> Self](immediatescheduler/schedulertimetype/stride/+(_:).md)
  Returns the given number unchanged.
- [static func + (ImmediateScheduler.SchedulerTimeType.Stride, ImmediateScheduler.SchedulerTimeType.Stride) -> ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/stride/+(_:_:).md)
  Adds two values and produces their sum.
- [static func += (inout ImmediateScheduler.SchedulerTimeType.Stride, ImmediateScheduler.SchedulerTimeType.Stride)](immediatescheduler/schedulertimetype/stride/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable.
- [static func - (Self) -> Self](immediatescheduler/schedulertimetype/stride/-(_:).md)
  Returns the additive inverse of the specified value.
- [static func - (ImmediateScheduler.SchedulerTimeType.Stride, ImmediateScheduler.SchedulerTimeType.Stride) -> ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/stride/-(_:_:).md)
  Subtracts one value from another and produces their difference.
- [static func -= (inout ImmediateScheduler.SchedulerTimeType.Stride, ImmediateScheduler.SchedulerTimeType.Stride)](immediatescheduler/schedulertimetype/stride/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable.
### Comparing Scheduler Time Strides
- [static func != (Self, Self) -> Bool](immediatescheduler/schedulertimetype/stride/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (ImmediateScheduler.SchedulerTimeType.Stride, ImmediateScheduler.SchedulerTimeType.Stride) -> Bool](immediatescheduler/schedulertimetype/stride/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Encoding Scheduler Time Strides
- [func encode(to: any Encoder) throws](immediatescheduler/schedulertimetype/stride/encode(to:).md)
  Encodes this value into the given encoder.
### Operators
- [static func < (ImmediateScheduler.SchedulerTimeType.Stride, ImmediateScheduler.SchedulerTimeType.Stride) -> Bool](immediatescheduler/schedulertimetype/stride/_(_:_:).md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
### Default Implementations
- [AdditiveArithmetic Implementations](immediatescheduler/schedulertimetype/stride/additivearithmetic-implementations.md)
- [Comparable Implementations](immediatescheduler/schedulertimetype/stride/comparable-implementations.md)
- [Equatable Implementations](immediatescheduler/schedulertimetype/stride/equatable-implementations.md)
- [SignedNumeric Implementations](immediatescheduler/schedulertimetype/stride/signednumeric-implementations.md)

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