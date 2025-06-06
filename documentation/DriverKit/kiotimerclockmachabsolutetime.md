# kIOTimerClockMachAbsoluteTime

**Framework**: DriverKit  
**Kind**: case

A clock type representing the numer of ticks since the last reboot.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kIOTimerClockMachAbsoluteTime
```

#### Discussion

This constant is a clock type whose value is from `mach_absolute_time()` in tick units. This clock type does not advance when the computer is asleep.

## See Also

- [kIOTimerClockUptimeRaw](kiotimerclockuptimeraw.md)
  A clock type that increments monotonically, but does not increment when the system is asleep.
- [kIOTimerClockMonotonicRaw](kiotimerclockmonotonicraw.md)
  A clock type that increments monotonically, and is unaffected by frequency or time adjustmets.
- [kIOTimerClockRealTime](kiotimerclockrealtime.md)
  The system’s real time, expressed as the amount of time since the Epoch.
- [kIOTimerClockWallTime](kiotimerclockwalltime.md)
  The system’s wall-clock time, expressed as the amount of time since the Epoch.
- [kIOTimerClockMachContinuousTime](kiotimerclockmachcontinuoustime.md)
  A clock type representing the number of ticks since the last reboot, including when the computer is asleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/kiotimerclockmachabsolutetime)*