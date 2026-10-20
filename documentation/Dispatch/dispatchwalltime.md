# DispatchWallTime

**Framework**: Dispatch  
**Kind**: struct  
**Role**: Structure

An absolute point in time according to the wall clock, with microsecond precision.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct DispatchWallTime
```

## Topics

### Getting Well-Known Times
- [static func now() -> DispatchWallTime](./dispatchwalltime/now%28%29.md)
  Returns the current time.
- [static let distantFuture: DispatchWallTime](./dispatchwalltime/distantfuture.md)
  A time in the distant future.
### Creating a Dispatch Wall Time Object
- [init(timespec: timespec)](./dispatchwalltime/init%28timespec%29.md)
  Creates an absolute time for a specified value.
### Getting the Time
- [let rawValue: dispatch_time_t](./dispatchwalltime/rawvalue.md)
  The underlying time value.
### Operator Functions
- [func + (DispatchWallTime, DispatchTimeInterval) -> DispatchWallTime](./plus%28_,_%29-8ylhk.md)
- [func + (DispatchWallTime, Double) -> DispatchWallTime](./plus%28_,_%29-8pe6k.md)
- [func - (DispatchWallTime, Double) -> DispatchWallTime](./minus%28_,_%29-6jk71.md)
- [func - (DispatchWallTime, DispatchTimeInterval) -> DispatchWallTime](./minus%28_,_%29-50bxr.md)

## Relationships

### Conforms To
- [Comparable](../Swift/comparable.md)
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Time Constructs
- [struct DispatchTime](./dispatchtime.md)
  A point in time relative to the default clock, with nanosecond precision.
- [enum DispatchTimeInterval](./dispatchtimeinterval.md)
  A number of seconds, millisconds, microseconds, or nanoseconds.
- [enum DispatchTimeoutResult](./dispatchtimeoutresult.md)
  A result value indicating whether a dispatch operation finished before a specified time.
- [typealias dispatch_time_t](./dispatch_time_t.md)
  An abstract representation of time.
- [var DISPATCH_WALLTIME_NOW: UInt](./dispatch_walltime_now.md)
  The current time.
- [Wall Time Constants](./api-2963138-wall-time-constants.md)
  Constants for wall time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchwalltime)*