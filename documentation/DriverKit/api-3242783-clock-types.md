# Clock Types

**Framework**: DriverKit

Clock types to use when configuring a timer.

## Topics

### Timer Options
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
- [kIOTimerClockMachContinuousTime](kiotimerclockmachcontinuoustime.md)
  A clock type representing the number of ticks since the last reboot, including when the computer is asleep.

## See Also

- [WakeAtTime](iotimerdispatchsource/wakeattime.md)
  Schedules a callback from the timer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/3242783-clock_types)*