# dispatch_time

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Creates a `dispatch_time_t` relative to the default clock or modifies an existing `dispatch_time_t`.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern dispatch_time_t dispatch_time(dispatch_time_t when, int64_t delta);
```

## Return Value

A new [`dispatch_time_t`](./dispatch_time_t.md).

## Discussion

The default clock is based on [`mach_absolute_time`](../kernel/api-1462446-mach_absolute_time.md).

## Parameters

- `when`: The [`dispatch_function_t`](./dispatch_function_t.md) value to use as the basis for a new value. Pass [`DISPATCH_TIME_NOW`](./dispatch_time_now.md) to create a new time value relative to now.
- `delta`: The number of nanoseconds to add to the time in the `when` parameter.

## See Also

### Time Constructs
- [dispatch_walltime](./dispatch_walltime.md)
  Creates a `dispatch_time_t` using an absolute time according to the wall clock.
- [typealias dispatch_time_t](./dispatch_time_t.md)
  An abstract representation of time.
- [var DISPATCH_WALLTIME_NOW: UInt](./dispatch_walltime_now.md)
  The current time.
- [Wall Time Constants](./api-2963138-wall-time-constants.md)
  Constants for wall time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_time)*