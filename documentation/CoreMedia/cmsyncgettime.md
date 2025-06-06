# CMSyncGetTime(_:)

**Framework**: Core Media  
**Kind**: func

Returns the time from a clock or timebase.

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
func CMSyncGetTime(_ clockOrTimebase: CMClockOrTimebase) -> CMTime
```

#### Discussion

`CMSyncGetTime` calls either [`CMClockGetTime(_:)`](cmclockgettime(_:).md) or [`CMTimebaseGetTime(_:)`](cmtimebasegettime(_:).md), as appropriate.

## See Also

- [func CMSyncGetRelativeRate(CMClockOrTimebase, relativeTo: CMClockOrTimebase) -> Float64](cmsyncgetrelativerate(_:relativeto:).md)
  Returns the relative rate of one timebase or clock relative to another timebase or clock.
- [func CMSyncGetRelativeRateAndAnchorTime(CMClockOrTimebase, relativeTo: CMClockOrTimebase, relativeRateOut: UnsafeMutablePointer<Float64>?, anchorTimeOut: UnsafeMutablePointer<CMTime>?, relativeToAnchorTimeOut: UnsafeMutablePointer<CMTime>?) -> OSStatus](cmsyncgetrelativerateandanchortime(_:relativeto:relativerateout:anchortimeout:relativetoanchortimeout:).md)
  Returns the relative rate of one timebase or clock relative to another timebase or clock and the times of each timebase or clock at which the relative rate went into effect.
- [func CMSyncConvertTime(CMTime, from: CMClockOrTimebase, to: CMClockOrTimebase) -> CMTime](cmsyncconverttime(_:from:to:).md)
  Converts a time from one timebase or clock to another timebase or clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsyncgettime(_:))*