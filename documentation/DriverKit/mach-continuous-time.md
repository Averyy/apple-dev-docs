# mach_continuous_time

**Framework**: DriverKit  
**Kind**: func

Returns current value of a clock that increments monotonically in tick units (starting at an arbitrary point), including while the system is asleep.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
uint64_t mach_continuous_time();
```

#### Return Value

Value of mach continous time clock.

#### Discussion

Prefer to use the equivalent `clock_gettime_nsec_np(CLOCK_MONOTONIC_RAW)` in nanoseconds.

## See Also

- [mach_absolute_time](mach_absolute_time.md)
  Returns current value of a clock that increments monotonically in tick units (starting at an arbitrary point), this clock does not increment while the system is asleep.
- [mach_timebase_info](mach_timebase_info-c.func.md)
  Returns fraction to multiply a value in mach tick units with to convert it to nanoseconds.
- [mach_timebase_info_t](mach_timebase_info_t.md)
- [Time Scales](3223112-time_scales.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/mach_continuous_time)*