# kIOTimerClockMonotonicRaw

**Framework**: DriverKit  
**Kind**: case

A clock type that increments monotonically, and is unaffected by frequency or time adjustmets.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kIOTimerClockMonotonicRaw
```

#### Discussion

This constant is the type of clock obtained by passing `CLOCK_UPTIME_RAW` to `clock_gettime_nsec_np(_:)`. It’s equivalent to a value from `mach_absolute_time()`, but in nanoseconds.

## See Also

- [kIOTimerClockUptimeRaw](kiotimerclockuptimeraw.md)
  A clock type that increments monotonically, but does not increment when the system is asleep.
- [kIOTimerClockRealTime](kiotimerclockrealtime.md)
  The system’s real time, expressed as the amount of time since the Epoch.
- [kIOTimerClockWallTime](kiotimerclockwalltime.md)
  The system’s wall-clock time, expressed as the amount of time since the Epoch.
- [kIOTimerClockMachAbsoluteTime](kiotimerclockmachabsolutetime.md)
  A clock type representing the numer of ticks since the last reboot.
- [kIOTimerClockMachContinuousTime](kiotimerclockmachcontinuoustime.md)
  A clock type representing the number of ticks since the last reboot, including when the computer is asleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/kiotimerclockmonotonicraw)*