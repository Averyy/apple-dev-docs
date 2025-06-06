# init(mSampleTime:mHostTime:mRateScalar:mWordClockTime:mSMPTETime:mFlags:mReserved:)

**Framework**: Core Audio Types  
**Kind**: init

Creates an audio time stamp.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(mSampleTime: Float64, mHostTime: UInt64, mRateScalar: Float64, mWordClockTime: UInt64, mSMPTETime: SMPTETime, mFlags: AudioTimeStampFlags, mReserved: UInt32)
```

## See Also

- [init()](audiotimestamp/init.md)
  Creates an empty audio timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiotimestamp/init(msampletime:mhosttime:mratescalar:mwordclocktime:msmptetime:mflags:mreserved:))*