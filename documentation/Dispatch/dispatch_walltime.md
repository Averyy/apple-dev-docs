# dispatch_walltime

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Creates a `dispatch_time_t` using an absolute time according to the wall clock.

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
extern dispatch_time_t dispatch_walltime(const struct timespec *when, int64_t delta);
```

## Return Value

A new [`dispatch_time_t`](./dispatch_time_t.md).

## Discussion

The wall clock is based on `gettimeofday(_:_:)`.

## Parameters

- `when`: A `struct timespec` to add time to. If `NULL` is passed, then this function uses the result of `gettimeofday`.
- `delta`: Nanoseconds to add.

## See Also

### Time Constructs
- [dispatch_time](./dispatch_time.md)
  Creates a `dispatch_time_t` relative to the default clock or modifies an existing `dispatch_time_t`.
- [typealias dispatch_time_t](./dispatch_time_t.md)
  An abstract representation of time.
- [var DISPATCH_WALLTIME_NOW: UInt](./dispatch_walltime_now.md)
  The current time.
- [Wall Time Constants](./api-2963138-wall-time-constants.md)
  Constants for wall time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_walltime)*