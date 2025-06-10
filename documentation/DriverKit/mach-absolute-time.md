# mach_absolute_time

**Framework**: DriverKit  
**Kind**: func

Returns current value of a clock that increments monotonically in tick units (starting at an arbitrary point), this clock does not increment while the system is asleep.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
uint64_t mach_absolute_time();
```

#### Return Value

		Value of mach absolute time clock.

#### Discussion

Prefer to use the equivalent clock_gettime_nsec_np(CLOCK_UPTIME_RAW) in nanoseconds.

> ❗ **Important**:  This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [`Describing use of required reason API`](https://developer.apple.com/documentation/BundleResources/describing-use-of-required-reason-api).

## See Also

- [mach_continuous_time](mach_continuous_time.md)
  Returns current value of a clock that increments monotonically in tick units (starting at an arbitrary point), including while the system is asleep.
- [mach_timebase_info](mach_timebase_info-c.func.md)
  Returns fraction to multiply a value in mach tick units with to convert it to nanoseconds.
- [mach_timebase_info_t](mach_timebase_info_t.md)
- [Time Scales](3223112-time_scales.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/mach_absolute_time)*