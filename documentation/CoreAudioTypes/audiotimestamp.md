# AudioTimeStamp

**Framework**: Core Audio Types  
**Kind**: struct

A structure that represents a timestamp value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct AudioTimeStamp
```

## Topics

### Accessing the Data
- [var mFlags: AudioTimeStampFlags](audiotimestamp/mflags.md)
  A set of flags indicating which representations of the time are valid; see `Audio Time Stamp Flags` and `Audio Time Stamp Flag Combination Constant`.
- [var mHostTime: UInt64](audiotimestamp/mhosttime.md)
  The host machine’s time base (see `CoreAudio/HostTime.h`).
- [var mRateScalar: Float64](audiotimestamp/mratescalar.md)
  The ratio of actual host ticks per sample frame to the nominal host ticks per sample frame.
- [var mReserved: UInt32](audiotimestamp/mreserved.md)
  Pads the structure out to force an even 8-byte alignment.
- [var mSMPTETime: SMPTETime](audiotimestamp/msmptetime.md)
  The SMPTE time (see [`SMPTETime`](smptetime.md)).
- [var mSampleTime: Float64](audiotimestamp/msampletime.md)
  The absolute sample frame time.
- [var mWordClockTime: UInt64](audiotimestamp/mwordclocktime.md)
  The word clock time.
### Initializers
- [init()](audiotimestamp/init.md)
  Creates an empty audio timestamp.
- [init(mSampleTime: Float64, mHostTime: UInt64, mRateScalar: Float64, mWordClockTime: UInt64, mSMPTETime: SMPTETime, mFlags: AudioTimeStampFlags, mReserved: UInt32)](audiotimestamp/init(msampletime:mhosttime:mratescalar:mwordclocktime:msmptetime:mflags:mreserved:).md)
  Creates an audio time stamp.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AudioTimeStampFlags](audiotimestampflags.md)
  A structure that represents flags for a timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiotimestamp)*