# mach_timebase_info

**Framework**: DriverKit  
**Kind**: func

Returns fraction to multiply a value in mach tick units with to convert it to nanoseconds.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t mach_timebase_info(mach_timebase_info_t info);
```

#### Return Value

`KERN_SUCCESS` if `info` was filled in.

## Parameters

- `info`: Timebase fraction out parameter.

## See Also

- [mach_absolute_time](mach_absolute_time.md)
  Returns current value of a clock that increments monotonically in tick units (starting at an arbitrary point), this clock does not increment while the system is asleep.
- [mach_continuous_time](mach_continuous_time.md)
  Returns current value of a clock that increments monotonically in tick units (starting at an arbitrary point), including while the system is asleep.
- [mach_timebase_info_t](mach_timebase_info_t.md)
- [Time Scales](3223112-time_scales.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/mach_timebase_info-c.func)*