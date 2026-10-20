# CMClockMakeHostTimeFromSystemUnits(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Converts a host time from native units to a core media time structure.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMClockMakeHostTimeFromSystemUnits(_ hostTime: UInt64) -> CMTime
```

```c
extern CMTime CMClockMakeHostTimeFromSystemUnits(uint64_t hostTime);
```

#### Discussion

The return value has a large integer timescale (for example, nanoseconds). This function handles situations where the host time’s native units use a non-integer timescale.

In macOS, this function converts from the units of `mach_absolute_time`.

## Parameters

- `hostTime`: The host time, in native units, to convert.

## See Also

### Accessing and Converting Time
- [func CMClockGetTime(CMClock) -> CMTime](./cmclockgettime%28_%29.md)
  Returns the current time from a clock.
- [func CMClockGetAnchorTime(CMClock, clockTimeOut: UnsafeMutablePointer<CMTime>, referenceClockTimeOut: UnsafeMutablePointer<CMTime>) -> OSStatus](./cmclockgetanchortime%28_,clocktimeout,referenceclocktimeout%29.md)
  Returns the current time from a clock and the matching time from the clock’s reference clock.
- [func CMClockConvertHostTimeToSystemUnits(CMTime) -> UInt64](./cmclockconverthosttimetosystemunits%28_%29.md)
  Converts a host time from a core media time structure to the host time’s native units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclockmakehosttimefromsystemunits(_:))*