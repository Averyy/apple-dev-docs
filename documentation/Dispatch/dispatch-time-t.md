# dispatch_time_t

**Framework**: Dispatch  
**Kind**: typealias

An abstract representation of time.

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
typealias dispatch_time_t = UInt64
```

## Topics

### Well-Defined Times
- [var DISPATCH_TIME_NOW: UInt64](dispatch_time_now.md)
- [var DISPATCH_TIME_FOREVER: UInt64](dispatch_time_forever.md)
### Time Multiplier Constants
- [var USEC_PER_SEC: UInt64](usec_per_sec.md)
- [var NSEC_PER_SEC: UInt64](nsec_per_sec.md)
- [var NSEC_PER_MSEC: UInt64](nsec_per_msec.md)
- [var NSEC_PER_USEC: UInt64](nsec_per_usec.md)

## See Also

- [struct DispatchTime](dispatchtime.md)
  A point in time relative to the default clock, with nanosecond precision.
- [struct DispatchWallTime](dispatchwalltime.md)
  An absolute point in time according to the wall clock, with microsecond precision.
- [enum DispatchTimeInterval](dispatchtimeinterval.md)
  A number of seconds, millisconds, microseconds, or nanoseconds.
- [enum DispatchTimeoutResult](dispatchtimeoutresult.md)
  A result value indicating whether a dispatch operation finished before a specified time.
- [var DISPATCH_WALLTIME_NOW: UInt](dispatch_walltime_now.md)
  The current time.
- [Wall Time Constants](2963138-wall-time-constants.md)
  Constants for wall time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_time_t)*