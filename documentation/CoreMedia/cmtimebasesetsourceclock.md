# CMTimebaseSetSourceClock(_:_:)

**Framework**: Core Media  
**Kind**: func

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

## See Also

- [func CMTimebaseGetTime(CMTimebase) -> CMTime](cmtimebasegettime(_:).md)
  Returns the current time from a timebase.
- [func CMTimebaseGetTimeWithTimeScale(CMTimebase, timescale: CMTimeScale, method: CMTimeRoundingMethod) -> CMTime](cmtimebasegettimewithtimescale(_:timescale:method:).md)
  Returns the current time from a timebase in the specified timescale.
- [func CMTimebaseGetTimeAndRate(CMTimebase, timeOut: UnsafeMutablePointer<CMTime>?, rateOut: UnsafeMutablePointer<Float64>?) -> OSStatus](cmtimebasegettimeandrate(_:timeout:rateout:).md)
  Returns the current time and rate of a timebase.
- [func CMTimebaseSetTime(CMTimebase, time: CMTime) -> OSStatus](cmtimebasesettime(_:time:).md)
  Sets the current time of a timebase.
- [func CMTimebaseSetSourceTimebase(CMTimebase, CMTimebase) -> OSStatus](cmtimebasesetsourcetimebase(_:_:).md)
  Sets the source timebase of a timebase.
- [func CMTimebaseSetAnchorTime(CMTimebase, timebaseTime: CMTime, immediateSourceTime: CMTime) -> OSStatus](cmtimebasesetanchortime(_:timebasetime:immediatesourcetime:).md)
  Sets the time of a timebase at a particular host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasesetsourceclock(_:_:))*