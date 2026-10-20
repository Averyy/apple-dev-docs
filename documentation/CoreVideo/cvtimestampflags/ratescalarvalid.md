# rateScalarValid

**Framework**: Core Video  
**Kind**: property  
**Role**: Type Property

The value in the rate scalar field is valid.

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
static var rateScalarValid: CVTimeStampFlags { get }
```

```c
kCVTimeStampRateScalarValid
```

## See Also

### Constants
- [static var bottomField: CVTimeStampFlags](./bottomfield.md)
  The timestamp represents the bottom lines of an interlaced image.
- [static var hostTimeValid: CVTimeStampFlags](./hosttimevalid.md)
  The value in the host time field is valid.
- [static var isInterlaced: CVTimeStampFlags](./isinterlaced.md)
  A convenience constant indicating that the timestamp is for an interlaced image.
- [static var smpteTimeValid: CVTimeStampFlags](./smptetimevalid.md)
  The value in the SMPTE time field is valid.
- [static var topField: CVTimeStampFlags](./topfield.md)
  The timestamp represents the top lines of an interlaced image.
- [static var videoHostTimeValid: CVTimeStampFlags](./videohosttimevalid.md)
  A convenience constant indicating that both the video time and host time fields are valid.
- [static var videoRefreshPeriodValid: CVTimeStampFlags](./videorefreshperiodvalid.md)
  The value in the video refresh period field is valid.
- [static var videoTimeValid: CVTimeStampFlags](./videotimevalid.md)
  The value in the video time field is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvtimestampflags/ratescalarvalid)*