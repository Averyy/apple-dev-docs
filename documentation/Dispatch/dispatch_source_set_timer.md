# dispatch_source_set_timer

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Sets a start time, interval, and leeway value for a timer source.

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
extern void dispatch_source_set_timer(dispatch_source_t source, dispatch_time_t start, uint64_t interval, uint64_t leeway);
```

## Discussion

Your application can call this function multiple times on the same dispatch timer source object to reset the time interval for the timer source as necessary.

The `start` time parameter also determines which clock is used for the timer. If the start time is [`DISPATCH_TIME_NOW`](./dispatch_time_now.md) or is created with [`dispatch_time`](./dispatch_time.md), the timer is based on `mach_absolute_time`. Otherwise, if the start time of the timer is created with [`dispatch_walltime`](./dispatch_walltime.md), the timer is based on `gettimeofday`(3).

The `leeway` parameter is a hint from the application as to the amount of time, in nanoseconds, up to which the system can defer the timer to align with other system activity for improved system performance or power consumption. For example, an application might perform a periodic task every 5 minutes, with a leeway of up to 30 seconds. Note that some latency is to be expected for all timers, even when a leeway value of zero is specified.

Calling this function has no effect if the timer source has already been canceled.

## Parameters

- `start`: The start time of the timer. See [`dispatch_time`](./dispatch_time.md) and [`dispatch_walltime`](./dispatch_walltime.md) for more information.
- `interval`: The nanosecond interval for the timer.
- `leeway`: The amount of time, in nanoseconds, that the system can defer the timer.

## See Also

### Managing Timer Parameters
- [dispatch_source_timer_flags_t](./dispatch_source_timer_flags_t.md)
  Flags to use when configuring a timer dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_source_set_timer)*