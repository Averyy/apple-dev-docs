# CVTimeStamp

**Framework**: Core Video  
**Kind**: struct

A structure for defining a display timestamp.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct CVTimeStamp
```

#### Overview

This structure is designed to be very similar to the audio timestamp defined in the Core Audio framework except that, in CVTimeStamp, floating-point values are not used to represent the video equivalent of sample times.

## Topics

### Initializers
- [init()](cvtimestamp/init.md)
- [init(version: UInt32, videoTimeScale: Int32, videoTime: Int64, hostTime: UInt64, rateScalar: Double, videoRefreshPeriod: Int64, smpteTime: CVSMPTETime, flags: UInt64, reserved: UInt64)](cvtimestamp/init(version:videotimescale:videotime:hosttime:ratescalar:videorefreshperiod:smptetime:flags:reserved:).md)
- [init(videoTime: CVTime?, hostTime: UInt64?, rateScaler: Double?, videoRefreshPeriod: Int64?, smpteTime: CVSMPTETime?, topField: Bool, bottomField: Bool)](cvtimestamp/init(videotime:hosttime:ratescaler:videorefreshperiod:smptetime:topfield:bottomfield:).md)
  Initialize a CVTimeStamp containing specified fields. The bits corrsrponding to non-nil arguments are set in `CVTimeStamp.flags`.
### Properties
- [var flags: UInt64](cvtimestamp/flags.md)
  A bit field containing additional information about the timestamp.
- [var hostTime: UInt64](cvtimestamp/hosttime.md)
  The system time measured by the timestamp.
- [var rateScalar: Double](cvtimestamp/ratescalar.md)
  The current rate of the device as measured by the timestamps, divided by the nominal rate.
- [var reserved: UInt64](cvtimestamp/reserved.md)
  Reserved. Do not use.
- [var smpteTime: CVSMPTETime](cvtimestamp/smptetime.md)
  The SMPTE time representation of the timestamp.
- [var version: UInt32](cvtimestamp/version.md)
  The current `CVTimeStamp` structure is version 0. Some functions require you to specify a version when passing in a timestamp structure to be filled.
- [var videoRefreshPeriod: Int64](cvtimestamp/videorefreshperiod.md)
- [var videoTime: Int64](cvtimestamp/videotime.md)
  The start of a frame (or field for interlaced video).
- [var videoTimeScale: Int32](cvtimestamp/videotimescale.md)
  The scale (in units per second) of the `videoTimeScale` and `videoRefreshPeriod` fields.
### Instance Properties
- [var flagOptions: CVTimeStampFlags](cvtimestamp/flagoptions.md)
  `CVTimeStampFlags` representation of `CVTimeStamp.flags`

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvtimestamp)*