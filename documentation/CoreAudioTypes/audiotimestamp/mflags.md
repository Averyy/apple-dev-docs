# mFlags

**Framework**: Core Audio Types  
**Kind**: property  
**Role**: Instance Property

A set of flags indicating which representations of the time are valid; see `Audio Time Stamp Flags` and `Audio Time Stamp Flag Combination Constant`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var mFlags: AudioTimeStampFlags
```

```c
AudioTimeStampFlags mFlags;
```

## See Also

### Accessing the Data
- [var mHostTime: UInt64](./mhosttime.md)
  The host machine’s time base (see `CoreAudio/HostTime.h`).
- [var mRateScalar: Float64](./mratescalar.md)
  The ratio of actual host ticks per sample frame to the nominal host ticks per sample frame.
- [var mReserved: UInt32](./mreserved.md)
  Pads the structure out to force an even 8-byte alignment.
- [var mSMPTETime: SMPTETime](./msmptetime.md)
  The SMPTE time (see [`SMPTETime`](../smptetime.md)).
- [var mSampleTime: Float64](./msampletime.md)
  The absolute sample frame time.
- [var mWordClockTime: UInt64](./mwordclocktime.md)
  The word clock time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiotimestamp/mflags)*