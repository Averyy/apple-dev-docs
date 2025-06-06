# CMClockConvertHostTimeToSystemUnits(_:)

**Framework**: Core Media  
**Kind**: func

Converts a host time from a core media time structure to the host time’s native units.

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
func CMClockConvertHostTimeToSystemUnits(_ hostTime: CMTime) -> UInt64
```

#### Discussion

This function performs a scale conversion, not a clock conversion. It can be more accurate than [`CMTimeConvertScale(_:timescale:method:)`](cmtimeconvertscale(_:timescale:method:).md) because the system units may have a non-integer timescale.

In macOS, this function converts to the units of `mach_absolute_time`.

## Parameters

- `hostTime`: The host time to convert.

## See Also

- [func CMClockGetTime(CMClock) -> CMTime](cmclockgettime(_:).md)
  Returns the current time from a clock.
- [func CMClockGetAnchorTime(CMClock, clockTimeOut: UnsafeMutablePointer<CMTime>, referenceClockTimeOut: UnsafeMutablePointer<CMTime>) -> OSStatus](cmclockgetanchortime(_:clocktimeout:referenceclocktimeout:).md)
  Returns the current time from a clock and the matching time from the clock’s reference clock.
- [func CMClockMakeHostTimeFromSystemUnits(UInt64) -> CMTime](cmclockmakehosttimefromsystemunits(_:).md)
  Converts a host time from native units to a core media time structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclockconverthosttimetosystemunits(_:))*