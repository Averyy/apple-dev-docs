# smpteTime

**Framework**: Core Video  
**Kind**: property  
**Role**: Instance Property

The SMPTE time representation of the timestamp.

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
var smpteTime: CVSMPTETime
```

```c
CVSMPTETime smpteTime;
```

## See Also

### Properties
- [var flags: UInt64](./flags.md)
  A bit field containing additional information about the timestamp.
- [var hostTime: UInt64](./hosttime.md)
  The system time measured by the timestamp.
- [var rateScalar: Double](./ratescalar.md)
  The current rate of the device as measured by the timestamps, divided by the nominal rate.
- [var reserved: UInt64](./reserved.md)
  Reserved. Do not use.
- [var version: UInt32](./version.md)
  The current `CVTimeStamp` structure is version 0. Some functions require you to specify a version when passing in a timestamp structure to be filled.
- [var videoRefreshPeriod: Int64](./videorefreshperiod.md)
- [var videoTime: Int64](./videotime.md)
  The start of a frame (or field for interlaced video).
- [var videoTimeScale: Int32](./videotimescale.md)
  The scale (in units per second) of the `videoTimeScale` and `videoRefreshPeriod` fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvtimestamp/smptetime)*