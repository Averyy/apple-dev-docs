# RunLoop.SchedulerTimeType.Stride

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [init(TimeInterval)](./stride/init%28_%29.md)
  Creates a run loop scheduler time interval from the given time interval.
- [init?<T>(exactly: T)](./stride/init%28exactly%29.md)
  Creates a run loop scheduler time interval from a binary integer type.
- [init(floatLiteral: TimeInterval)](./stride/init%28floatliteral%29.md)
  Creates a run loop scheduler time interval from a floating-point seconds value.
- [init(integerLiteral: TimeInterval)](./stride/init%28integerliteral%29.md)
  Creates a run loop scheduler time interval from an integer seconds value.
### Converting to Seconds
- [static func microseconds(Int) -> RunLoop.SchedulerTimeType.Stride](./stride/microseconds%28_%29.md)
  Converts the specified number of microseconds into an instance of this scheduler time type.
- [static func milliseconds(Int) -> RunLoop.SchedulerTimeType.Stride](./stride/milliseconds%28_%29.md)
  Converts the specified number of milliseconds into an instance of this scheduler time type.
- [static func nanoseconds(Int) -> RunLoop.SchedulerTimeType.Stride](./stride/nanoseconds%28_%29.md)
  Converts the specified number of nanoseconds into an instance of this scheduler time type.
- [static func seconds(Double) -> RunLoop.SchedulerTimeType.Stride](./stride/seconds%28_%29-4kk8j.md)
  Converts the specified number of seconds, as a floating-point value, into an instance of this scheduler time type.
- [static func seconds(Int) -> RunLoop.SchedulerTimeType.Stride](./stride/seconds%28_%29-48wwk.md)
  Converts the specified number of seconds into an instance of this scheduler time type.
### Inspecting Stride Properties
- [var magnitude: TimeInterval](./stride/magnitude.md)
  The value of this time interval in seconds.
- [var timeInterval: TimeInterval](./stride/timeinterval.md)
  The value of this time interval in seconds.
### Operators
- [static func * (RunLoop.SchedulerTimeType.Stride, RunLoop.SchedulerTimeType.Stride) -> RunLoop.SchedulerTimeType.Stride](./stride/star%28_,_%29.md)
  Returns the result of multiplying the values of the two arguments.
- [static func *= (inout RunLoop.SchedulerTimeType.Stride, RunLoop.SchedulerTimeType.Stride)](./stride/stareq%28_,_%29.md)
  Multiplies the values of the two arguments, and assigns the result to the first argument.
- [static func + (RunLoop.SchedulerTimeType.Stride, RunLoop.SchedulerTimeType.Stride) -> RunLoop.SchedulerTimeType.Stride](./stride/plus%28_,_%29.md)
  Returns the result of adding the values of the two arguments.
- [static func += (inout RunLoop.SchedulerTimeType.Stride, RunLoop.SchedulerTimeType.Stride)](./stride/pluseq%28_,_%29.md)
  Adds the values of the two arguments, and assigns the result to the first argument.
- [static func - (RunLoop.SchedulerTimeType.Stride, RunLoop.SchedulerTimeType.Stride) -> RunLoop.SchedulerTimeType.Stride](./stride/minus%28_,_%29.md)
  Returns the result of subtracting the second stride from the first.
- [static func -= (inout RunLoop.SchedulerTimeType.Stride, RunLoop.SchedulerTimeType.Stride)](./stride/minuseq%28_,_%29.md)
  Subtracts the second stride from the first and assigns the result to the first.
- [static func < (RunLoop.SchedulerTimeType.Stride, RunLoop.SchedulerTimeType.Stride) -> Bool](./stride/op%28_,_%29.md)
  Returns a Boolean value indicating whether the first stride is less than the second.

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

### Working with Scheduler Time Intervals
- [func advanced(by: RunLoop.SchedulerTimeType.Stride) -> RunLoop.SchedulerTimeType](./advanced%28by%29.md)
  Returns a run loop scheduler time calculated by advancing this instance’s time by the given interval.
- [func distance(to: RunLoop.SchedulerTimeType) -> RunLoop.SchedulerTimeType.Stride](./distance%28to%29.md)
  Returns the distance to another run loop scheduler time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/schedulertimetype/stride)*