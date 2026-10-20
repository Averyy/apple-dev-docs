# CMTimebaseSetSourceClock(_:_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Sets the source clock of a timebase.

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
func CMTimebaseSetSourceClock(_ timebase: CMTimebase, _ newSourceClock: CMClock) -> OSStatus
```

```c
extern OSStatus CMTimebaseSetSourceClock(CMTimebaseRef timebase, CMClockRef newSourceClock);
```

## See Also

### Getting and Setting Time
- [func CMTimebaseGetTime(CMTimebase) -> CMTime](./cmtimebasegettime%28_%29.md)
  Returns the current time from a timebase.
- [func CMTimebaseGetTimeWithTimeScale(CMTimebase, timescale: CMTimeScale, method: CMTimeRoundingMethod) -> CMTime](./cmtimebasegettimewithtimescale%28_,timescale,method%29.md)
  Returns the current time from a timebase in the specified timescale.
- [func CMTimebaseGetTimeAndRate(CMTimebase, timeOut: UnsafeMutablePointer<CMTime>?, rateOut: UnsafeMutablePointer<Float64>?) -> OSStatus](./cmtimebasegettimeandrate%28_,timeout,rateout%29.md)
  Returns the current time and rate of a timebase.
- [func CMTimebaseSetTime(CMTimebase, time: CMTime) -> OSStatus](./cmtimebasesettime%28_,time%29.md)
  Sets the current time of a timebase.
- [func CMTimebaseSetSourceTimebase(CMTimebase, CMTimebase) -> OSStatus](./cmtimebasesetsourcetimebase%28_,_%29.md)
  Sets the source timebase of a timebase.
- [func CMTimebaseSetAnchorTime(CMTimebase, timebaseTime: CMTime, immediateSourceTime: CMTime) -> OSStatus](./cmtimebasesetanchortime%28_,timebasetime,immediatesourcetime%29.md)
  Sets the time of a timebase at a particular host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasesetsourceclock(_:_:))*