# DispatchWallTime

**Framework**: Dispatch  
**Kind**: struct

An absolute point in time according to the wall clock, with microsecond precision.

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
struct DispatchWallTime
```

## Topics

### Getting Well-Known Times
- [static func now() -> DispatchWallTime](dispatchwalltime/now.md)
  Returns the current time.
- [static let distantFuture: DispatchWallTime](dispatchwalltime/distantfuture.md)
  A time in the distant future.
### Creating a Dispatch Wall Time Object
- [init(timespec: timespec)](dispatchwalltime/init(timespec:).md)
  Creates an absolute time for a specified value.
### Getting the Time
- [let rawValue: dispatch_time_t](dispatchwalltime/rawvalue.md)
  The underlying time value.
### Operator Functions
- [func + (DispatchWallTime, DispatchTimeInterval) -> DispatchWallTime](+(_:_:)-8ylhk.md)
- [func + (DispatchWallTime, Double) -> DispatchWallTime](+(_:_:)-8pe6k.md)
- [func - (DispatchWallTime, Double) -> DispatchWallTime](-(_:_:)-6jk71.md)
- [func - (DispatchWallTime, DispatchTimeInterval) -> DispatchWallTime](-(_:_:)-50bxr.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct DispatchTime](dispatchtime.md)
  A point in time relative to the default clock, with nanosecond precision.
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

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchwalltime)*