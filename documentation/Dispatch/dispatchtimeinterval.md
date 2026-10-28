# DispatchTimeInterval

**Framework**: Dispatch  
**Kind**: enum  
**Role**: Enumeration

A number of seconds, millisconds, microseconds, or nanoseconds.

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
enum DispatchTimeInterval
```

## Overview

Use [`DispatchTimeInterval`](./dispatchtimeinterval.md) values to specify the interval at which a [`DispatchSourceTimer`](./dispatchsourcetimer.md) fires or I/O handlers are invoked for a [`DispatchIO`](./dispatchio.md) channel, as well as to increment and decrement [`DispatchTime`](./dispatchtime.md) values.

## Topics

### Enumeration Cases
- [DispatchTimeInterval.seconds(_:)](./dispatchtimeinterval/seconds%28_%29.md)
  A number of seconds.
- [DispatchTimeInterval.milliseconds(_:)](./dispatchtimeinterval/milliseconds%28_%29.md)
  A number of milliseconds.
- [DispatchTimeInterval.microseconds(_:)](./dispatchtimeinterval/microseconds%28_%29.md)
  A number of microseconds.
- [DispatchTimeInterval.nanoseconds(_:)](./dispatchtimeinterval/nanoseconds%28_%29.md)
  A number of nanoseconds.
- [DispatchTimeInterval.never](./dispatchtimeinterval/never.md)
  No interval.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Time Constructs
- [struct DispatchTime](./dispatchtime.md)
  A point in time relative to the default clock, with nanosecond precision.
- [struct DispatchWallTime](./dispatchwalltime.md)
  An absolute point in time according to the wall clock, with microsecond precision.
- [enum DispatchTimeoutResult](./dispatchtimeoutresult.md)
  A result value indicating whether a dispatch operation finished before a specified time.
- [typealias dispatch_time_t](./dispatch_time_t.md)
  An abstract representation of time.
- [var DISPATCH_WALLTIME_NOW: UInt](./dispatch_walltime_now.md)
  The current time.
- [Wall Time Constants](./api-2963138-wall-time-constants.md)
  Constants for wall time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchtimeinterval)*