# kIOTimerClockMachContinuousTime

**Framework**: DriverKit  
**Kind**: case

A clock type representing the number of ticks since the last reboot, including when the computer is asleep.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kIOTimerClockMachContinuousTime
```

#### Discussion

This constant is a clock type whose value is from `mach_continuous_time()` in tick units.

## See Also

- [kIOTimerClockUptimeRaw](kiotimerclockuptimeraw.md)
  A clock type that increments monotonically, but does not increment when the system is asleep.
- [kIOTimerClockMonotonicRaw](kiotimerclockmonotonicraw.md)
  A clock type that increments monotonically, and is unaffected by frequency or time adjustmets.
- [kIOTimerClockRealTime](kiotimerclockrealtime.md)
  The system’s real time, expressed as the amount of time since the Epoch.
- [kIOTimerClockWallTime](kiotimerclockwalltime.md)
  The system’s wall-clock time, expressed as the amount of time since the Epoch.
- [kIOTimerClockMachAbsoluteTime](kiotimerclockmachabsolutetime.md)
  A clock type representing the numer of ticks since the last reboot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/kiotimerclockmachcontinuoustime)*