# videoTimeScale

**Framework**: Core Video  
**Kind**: property

The scale (in units per second) of the `videoTimeScale` and `videoRefreshPeriod` fields.

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
var videoTimeScale: Int32
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvtimestamp/videotimescale)*