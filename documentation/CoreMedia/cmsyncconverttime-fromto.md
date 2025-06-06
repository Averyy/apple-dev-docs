# CMSyncConvertTime(_:from:to:)

**Framework**: Core Media  
**Kind**: func

Converts a time from one timebase or clock to another timebase or clock.

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
func CMSyncConvertTime(_ time: CMTime, from fromClockOrTimebase: CMClockOrTimebase, to toClockOrTimebase: CMClockOrTimebase) -> CMTime
```

#### Discussion

If both have a common host, the function syncs the clock or timebase based on the rates in the common tree rooted in that host.

If they have different host clocks (or are both clocks), this calculation also compensates for measured drift between the clocks. To convert to or from host time, pass `CMClockGetHostTimeClock`() as the appropriate argument.

## See Also

- [func CMSyncGetTime(CMClockOrTimebase) -> CMTime](cmsyncgettime(_:).md)
  Returns the time from a clock or timebase.
- [func CMSyncGetRelativeRate(CMClockOrTimebase, relativeTo: CMClockOrTimebase) -> Float64](cmsyncgetrelativerate(_:relativeto:).md)
  Returns the relative rate of one timebase or clock relative to another timebase or clock.
- [func CMSyncGetRelativeRateAndAnchorTime(CMClockOrTimebase, relativeTo: CMClockOrTimebase, relativeRateOut: UnsafeMutablePointer<Float64>?, anchorTimeOut: UnsafeMutablePointer<CMTime>?, relativeToAnchorTimeOut: UnsafeMutablePointer<CMTime>?) -> OSStatus](cmsyncgetrelativerateandanchortime(_:relativeto:relativerateout:anchortimeout:relativetoanchortimeout:).md)
  Returns the relative rate of one timebase or clock relative to another timebase or clock and the times of each timebase or clock at which the relative rate went into effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsyncconverttime(_:from:to:))*