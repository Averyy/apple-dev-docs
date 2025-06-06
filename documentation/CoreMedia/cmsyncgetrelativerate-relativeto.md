# CMSyncGetRelativeRate(_:relativeTo:)

**Framework**: Core Media  
**Kind**: func

Returns the relative rate of one timebase or clock relative to another timebase or clock.

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
func CMSyncGetRelativeRate(_ ofClockOrTimebase: CMClockOrTimebase, relativeTo relativeToClockOrTimebase: CMClockOrTimebase) -> Float64
```

#### Discussion

If both have a common host, the function syncs the clock or timebase based on the rates in the common tree rooted in that host.

If they have different host clocks (or are both clocks), this calculation takes into account the measured drift between the two clocks, using host time as a pivot. The rate of a moving timebase relative to a stopped timebase is a NaN. Calling `CMTimebaseGetEffectiveRate(timebase)` is equivalent to calling `CMSyncGetRelativeRate(timebase, CMTimebaseGetUltimateMasterClock(timebase)`).

## See Also

- [func CMSyncGetTime(CMClockOrTimebase) -> CMTime](cmsyncgettime(_:).md)
  Returns the time from a clock or timebase.
- [func CMSyncGetRelativeRateAndAnchorTime(CMClockOrTimebase, relativeTo: CMClockOrTimebase, relativeRateOut: UnsafeMutablePointer<Float64>?, anchorTimeOut: UnsafeMutablePointer<CMTime>?, relativeToAnchorTimeOut: UnsafeMutablePointer<CMTime>?) -> OSStatus](cmsyncgetrelativerateandanchortime(_:relativeto:relativerateout:anchortimeout:relativetoanchortimeout:).md)
  Returns the relative rate of one timebase or clock relative to another timebase or clock and the times of each timebase or clock at which the relative rate went into effect.
- [func CMSyncConvertTime(CMTime, from: CMClockOrTimebase, to: CMClockOrTimebase) -> CMTime](cmsyncconverttime(_:from:to:).md)
  Converts a time from one timebase or clock to another timebase or clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsyncgetrelativerate(_:relativeto:))*