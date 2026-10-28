# CMTimebaseGetTimeAndRate(_:timeOut:rateOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the current time and rate of a timebase.

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
func CMTimebaseGetTimeAndRate(_ timebase: CMTimebase, timeOut: UnsafeMutablePointer<CMTime>?, rateOut: UnsafeMutablePointer<Float64>?) -> OSStatus
```

```c
extern OSStatus CMTimebaseGetTimeAndRate(CMTimebaseRef timebase, CMTime *timeOut, Float64 *rateOut);
```

## Discussion

You can use this function to take a consistent snapshot of the two values, avoiding possible inconsistencies due to external changes between retrieval of time and rate.

## See Also

### Getting and Setting Time
- [func CMTimebaseGetTime(CMTimebase) -> CMTime](./cmtimebasegettime%28_%29.md)
  Returns the current time from a timebase.
- [func CMTimebaseGetTimeWithTimeScale(CMTimebase, timescale: CMTimeScale, method: CMTimeRoundingMethod) -> CMTime](./cmtimebasegettimewithtimescale%28_,timescale,method%29.md)
  Returns the current time from a timebase in the specified timescale.
- [func CMTimebaseSetTime(CMTimebase, time: CMTime) -> OSStatus](./cmtimebasesettime%28_,time%29.md)
  Sets the current time of a timebase.
- [func CMTimebaseSetSourceClock(CMTimebase, CMClock) -> OSStatus](./cmtimebasesetsourceclock%28_,_%29.md)
  Sets the source clock of a timebase.
- [func CMTimebaseSetSourceTimebase(CMTimebase, CMTimebase) -> OSStatus](./cmtimebasesetsourcetimebase%28_,_%29.md)
  Sets the source timebase of a timebase.
- [func CMTimebaseSetAnchorTime(CMTimebase, timebaseTime: CMTime, immediateSourceTime: CMTime) -> OSStatus](./cmtimebasesetanchortime%28_,timebasetime,immediatesourcetime%29.md)
  Sets the time of a timebase at a particular host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasegettimeandrate(_:timeout:rateout:))*