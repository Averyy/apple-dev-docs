# CMClockGetAnchorTime(_:clockTimeOut:referenceClockTimeOut:)

**Framework**: Core Media  
**Kind**: func

Returns the current time from a clock and the matching time from the clock’s reference clock.

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
func CMClockGetAnchorTime(_ clock: CMClock, clockTimeOut: UnsafeMutablePointer<CMTime>, referenceClockTimeOut: UnsafeMutablePointer<CMTime>) -> OSStatus
```

#### Discussion

To make practical use of this, you may need to know what the clock’s reference clock is.

## Parameters

- `clock`: The clock to retrieve the current time from.
- `clockTimeOut`: On output, points to the current time.
- `referenceClockTimeOut`: On output, points to the reference clock time.

## See Also

- [func CMClockGetTime(CMClock) -> CMTime](cmclockgettime(_:).md)
  Returns the current time from a clock.
- [func CMClockConvertHostTimeToSystemUnits(CMTime) -> UInt64](cmclockconverthosttimetosystemunits(_:).md)
  Converts a host time from a core media time structure to the host time’s native units.
- [func CMClockMakeHostTimeFromSystemUnits(UInt64) -> CMTime](cmclockmakehosttimefromsystemunits(_:).md)
  Converts a host time from native units to a core media time structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclockgetanchortime(_:clocktimeout:referenceclocktimeout:))*