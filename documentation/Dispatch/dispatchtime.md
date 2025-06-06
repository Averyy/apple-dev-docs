# DispatchTime

**Framework**: Dispatch  
**Kind**: struct

A point in time relative to the default clock, with nanosecond precision.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct DispatchTime
```

#### Overview

On Apple platforms, the default clock is based on the Mach absolute time unit.

## Topics

### Getting Well-Known Times
- [static func now() -> DispatchTime](dispatchtime/now.md)
  Returns the current time.
- [static let distantFuture: DispatchTime](dispatchtime/distantfuture.md)
  A time in the distant future.
### Creating a Dispatch Time Object
- [init(uptimeNanoseconds: UInt64)](dispatchtime/init(uptimenanoseconds:).md)
  Creates a time relative to the amount of time the system has been running.
### Getting the Time
- [let rawValue: dispatch_time_t](dispatchtime/rawvalue.md)
  Returns the underlying time value.
- [var uptimeNanoseconds: UInt64](dispatchtime/uptimenanoseconds.md)
  Returns the number of nanoseconds since boot, excluding any time the system spent asleep.
### Modifying the Value
- [func advanced(by: DispatchTimeInterval) -> DispatchTime](dispatchtime/advanced(by:).md)
- [func distance(to: DispatchTime) -> DispatchTimeInterval](dispatchtime/distance(to:).md)
### Operator Functions
- [func + (DispatchTime, Double) -> DispatchTime](+(_:_:)-6fmcc.md)
- [func + (DispatchTime, DispatchTimeInterval) -> DispatchTime](+(_:_:)-2dcrq.md)
- [func - (DispatchTime, Double) -> DispatchTime](-(_:_:)-5l4yh.md)
- [func - (DispatchTime, DispatchTimeInterval) -> DispatchTime](-(_:_:)-8usj3.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct DispatchWallTime](dispatchwalltime.md)
  An absolute point in time according to the wall clock, with microsecond precision.
- [enum DispatchTimeInterval](dispatchtimeinterval.md)
  A number of seconds, millisconds, microseconds, or nanoseconds.
- [enum DispatchTimeoutResult](dispatchtimeoutresult.md)
  A result value indicating whether a dispatch operation finished before a specified time.
- [typealias dispatch_time_t](dispatch_time_t.md)
  An abstract representation of time.
- [var DISPATCH_WALLTIME_NOW: UInt](dispatch_walltime_now.md)
  The current time.
- [Wall Time Constants](2963138-wall-time-constants.md)
  Constants for wall time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchtime)*