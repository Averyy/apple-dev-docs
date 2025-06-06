# CMTimebaseSetAnchorTime(_:timebaseTime:immediateSourceTime:)

**Framework**: Core Media  
**Kind**: func

Sets the time of a timebase at a particular host time.

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
func CMTimebaseSetAnchorTime(_ timebase: CMTimebase, timebaseTime: CMTime, immediateSourceTime: CMTime) -> OSStatus
```

#### Discussion

The system interpolates `CMTimebaseGetTime`’s results from the anchor time.

`CMTimebaseSetTime(timebase, time)` is equivalent to calling `CMTimebaseSetAnchorTime(timebase, time, CMSyncGetTime(CMTimebaseCopySource(timebase)))`.

## See Also

- [func CMTimebaseGetTime(CMTimebase) -> CMTime](cmtimebasegettime(_:).md)
  Returns the current time from a timebase.
- [func CMTimebaseGetTimeWithTimeScale(CMTimebase, timescale: CMTimeScale, method: CMTimeRoundingMethod) -> CMTime](cmtimebasegettimewithtimescale(_:timescale:method:).md)
  Returns the current time from a timebase in the specified timescale.
- [func CMTimebaseGetTimeAndRate(CMTimebase, timeOut: UnsafeMutablePointer<CMTime>?, rateOut: UnsafeMutablePointer<Float64>?) -> OSStatus](cmtimebasegettimeandrate(_:timeout:rateout:).md)
  Returns the current time and rate of a timebase.
- [func CMTimebaseSetTime(CMTimebase, time: CMTime) -> OSStatus](cmtimebasesettime(_:time:).md)
  Sets the current time of a timebase.
- [func CMTimebaseSetSourceClock(CMTimebase, CMClock) -> OSStatus](cmtimebasesetsourceclock(_:_:).md)
  Sets the source clock of a timebase.
- [func CMTimebaseSetSourceTimebase(CMTimebase, CMTimebase) -> OSStatus](cmtimebasesetsourcetimebase(_:_:).md)
  Sets the source timebase of a timebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasesetanchortime(_:timebasetime:immediatesourcetime:))*