# mSMPTETime

**Framework**: Core Audio Types  
**Kind**: property

The SMPTE time (see [`SMPTETime`](smptetime.md)).

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var mSMPTETime: SMPTETime
```

## See Also

- [var mFlags: AudioTimeStampFlags](audiotimestamp/mflags.md)
  A set of flags indicating which representations of the time are valid; see `Audio Time Stamp Flags` and `Audio Time Stamp Flag Combination Constant`.
- [var mHostTime: UInt64](audiotimestamp/mhosttime.md)
  The host machine’s time base (see `CoreAudio/HostTime.h`).
- [var mRateScalar: Float64](audiotimestamp/mratescalar.md)
  The ratio of actual host ticks per sample frame to the nominal host ticks per sample frame.
- [var mReserved: UInt32](audiotimestamp/mreserved.md)
  Pads the structure out to force an even 8-byte alignment.
- [var mSampleTime: Float64](audiotimestamp/msampletime.md)
  The absolute sample frame time.
- [var mWordClockTime: UInt64](audiotimestamp/mwordclocktime.md)
  The word clock time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiotimestamp/msmptetime)*