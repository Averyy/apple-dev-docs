# RunLoop.SchedulerTimeType.Stride

**Framework**: Foundation  
**Kind**: struct

The interval by which run loop times advance.

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
- [init(TimeInterval)](runloop/schedulertimetype/stride/init(_:).md)
  Creates a run loop scheduler time interval from the given time interval.
- [init?<T>(exactly: T)](runloop/schedulertimetype/stride/init(exactly:).md)
  Creates a run loop scheduler time interval from a binary integer type.
- [init(floatLiteral: TimeInterval)](runloop/schedulertimetype/stride/init(floatliteral:).md)
  Creates a run loop scheduler time interval from a floating-point seconds value.
- [init(integerLiteral: TimeInterval)](runloop/schedulertimetype/stride/init(integerliteral:).md)
  Creates a run loop scheduler time interval from an integer seconds value.
### Converting to Seconds
- [static func microseconds(Int) -> RunLoop.SchedulerTimeType.Stride](runloop/schedulertimetype/stride/microseconds(_:).md)
  Converts the specified number of microseconds into an instance of this scheduler time type.
- [static func milliseconds(Int) -> RunLoop.SchedulerTimeType.Stride](runloop/schedulertimetype/stride/milliseconds(_:).md)
  Converts the specified number of milliseconds into an instance of this scheduler time type.
- [static func nanoseconds(Int) -> RunLoop.SchedulerTimeType.Stride](runloop/schedulertimetype/stride/nanoseconds(_:).md)
  Converts the specified number of nanoseconds into an instance of this scheduler time type.
- [static func seconds(Double) -> RunLoop.SchedulerTimeType.Stride](runloop/schedulertimetype/stride/seconds(_:)-4kk8j.md)
  Converts the specified number of seconds, as a floating-point value, into an instance of this scheduler time type.
- [static func seconds(Int) -> RunLoop.SchedulerTimeType.Stride](runloop/schedulertimetype/stride/seconds(_:)-48wwk.md)
  Converts the specified number of seconds into an instance of this scheduler time type.
### Inspecting Stride Properties
- [var magnitude: TimeInterval](runloop/schedulertimetype/stride/magnitude.md)
  The value of this time interval in seconds.
- [var timeInterval: TimeInterval](runloop/schedulertimetype/stride/timeinterval.md)
  The value of this time interval in seconds.
### Operators
- [static func * (RunLoop.SchedulerTimeType.Stride, RunLoop.SchedulerTimeType.Stride) -> RunLoop.SchedulerTimeType.Stride](runloop/schedulertimetype/stride/*(_:_:).md)
  Returns the result of multiplying the values of the two arguments.
- [static func *= (inout RunLoop.SchedulerTimeType.Stride, RunLoop.SchedulerTimeType.Stride)](runloop/schedulertimetype/stride/*=(_:_:).md)
  Multiplies the values of the two arguments, and assigns the result to the first argument.
- [static func + (RunLoop.SchedulerTimeType.Stride, RunLoop.SchedulerTimeType.Stride) -> RunLoop.SchedulerTimeType.Stride](runloop/schedulertimetype/stride/+(_:_:).md)
  Returns the result of adding the values of the two arguments.
- [static func += (inout RunLoop.SchedulerTimeType.Stride, RunLoop.SchedulerTimeType.Stride)](runloop/schedulertimetype/stride/+=(_:_:).md)
  Adds the values of the two arguments, and assigns the result to the first argument.
- [static func - (RunLoop.SchedulerTimeType.Stride, RunLoop.SchedulerTimeType.Stride) -> RunLoop.SchedulerTimeType.Stride](runloop/schedulertimetype/stride/-(_:_:).md)
  Returns the result of subtracting the second stride from the first.
- [static func -= (inout RunLoop.SchedulerTimeType.Stride, RunLoop.SchedulerTimeType.Stride)](runloop/schedulertimetype/stride/-=(_:_:).md)
  Subtracts the second stride from the first and assigns the result to the first.
- [static func < (RunLoop.SchedulerTimeType.Stride, RunLoop.SchedulerTimeType.Stride) -> Bool](runloop/schedulertimetype/stride/_(_:_:).md)
  Returns a Boolean value indicating whether the first stride is less than the second.

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

- [func advanced(by: RunLoop.SchedulerTimeType.Stride) -> RunLoop.SchedulerTimeType](runloop/schedulertimetype/advanced(by:).md)
  Returns a run loop scheduler time calculated by advancing this instance’s time by the given interval.
- [func distance(to: RunLoop.SchedulerTimeType) -> RunLoop.SchedulerTimeType.Stride](runloop/schedulertimetype/distance(to:).md)
  Returns the distance to another run loop scheduler time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/schedulertimetype/stride)*