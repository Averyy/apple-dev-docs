# CMTimebaseGetTimeAndRate(_:timeOut:rateOut:)

**Framework**: Core Media  
**Kind**: func

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

#### Discussion

You can use this function to take a consistent snapshot of the two values, avoiding possible inconsistencies due to external changes between retrieval of time and rate.

## See Also

- [func CMTimebaseGetTime(CMTimebase) -> CMTime](cmtimebasegettime(_:).md)
  Returns the current time from a timebase.
- [func CMTimebaseGetTimeWithTimeScale(CMTimebase, timescale: CMTimeScale, method: CMTimeRoundingMethod) -> CMTime](cmtimebasegettimewithtimescale(_:timescale:method:).md)
  Returns the current time from a timebase in the specified timescale.
- [func CMTimebaseSetTime(CMTimebase, time: CMTime) -> OSStatus](cmtimebasesettime(_:time:).md)
  Sets the current time of a timebase.
- [func CMTimebaseSetSourceClock(CMTimebase, CMClock) -> OSStatus](cmtimebasesetsourceclock(_:_:).md)
  Sets the source clock of a timebase.
- [func CMTimebaseSetSourceTimebase(CMTimebase, CMTimebase) -> OSStatus](cmtimebasesetsourcetimebase(_:_:).md)
  Sets the source timebase of a timebase.
- [func CMTimebaseSetAnchorTime(CMTimebase, timebaseTime: CMTime, immediateSourceTime: CMTime) -> OSStatus](cmtimebasesetanchortime(_:timebasetime:immediatesourcetime:).md)
  Sets the time of a timebase at a particular host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasegettimeandrate(_:timeout:rateout:))*