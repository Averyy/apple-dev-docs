# CMTimebaseSetTime(_:time:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Sets the current time of a timebase.

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
func CMTimebaseSetTime(_ timebase: CMTimebase, time: CMTime) -> OSStatus
```

```c
extern OSStatus CMTimebaseSetTime(CMTimebaseRef timebase, CMTime time);
```

## See Also

### Getting and Setting Time
- [func CMTimebaseGetTime(CMTimebase) -> CMTime](./cmtimebasegettime%28_%29.md)
  Returns the current time from a timebase.
- [func CMTimebaseGetTimeWithTimeScale(CMTimebase, timescale: CMTimeScale, method: CMTimeRoundingMethod) -> CMTime](./cmtimebasegettimewithtimescale%28_,timescale,method%29.md)
  Returns the current time from a timebase in the specified timescale.
- [func CMTimebaseGetTimeAndRate(CMTimebase, timeOut: UnsafeMutablePointer<CMTime>?, rateOut: UnsafeMutablePointer<Float64>?) -> OSStatus](./cmtimebasegettimeandrate%28_,timeout,rateout%29.md)
  Returns the current time and rate of a timebase.
- [func CMTimebaseSetSourceClock(CMTimebase, CMClock) -> OSStatus](./cmtimebasesetsourceclock%28_,_%29.md)
  Sets the source clock of a timebase.
- [func CMTimebaseSetSourceTimebase(CMTimebase, CMTimebase) -> OSStatus](./cmtimebasesetsourcetimebase%28_,_%29.md)
  Sets the source timebase of a timebase.
- [func CMTimebaseSetAnchorTime(CMTimebase, timebaseTime: CMTime, immediateSourceTime: CMTime) -> OSStatus](./cmtimebasesetanchortime%28_,timebasetime,immediatesourcetime%29.md)
  Sets the time of a timebase at a particular host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasesettime(_:time:))*