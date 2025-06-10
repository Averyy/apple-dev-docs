# CVTimeStampFlags

**Framework**: Core Video  
**Kind**: struct

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
struct CVTimeStampFlags
```

## Topics

### Constants
- [static var bottomField: CVTimeStampFlags](cvtimestampflags/bottomfield.md)
  The timestamp represents the bottom lines of an interlaced image.
- [static var hostTimeValid: CVTimeStampFlags](cvtimestampflags/hosttimevalid.md)
  The value in the host time field is valid.
- [static var isInterlaced: CVTimeStampFlags](cvtimestampflags/isinterlaced.md)
  A convenience constant indicating that the timestamp is for an interlaced image.
- [static var rateScalarValid: CVTimeStampFlags](cvtimestampflags/ratescalarvalid.md)
  The value in the rate scalar field is valid.
- [static var smpteTimeValid: CVTimeStampFlags](cvtimestampflags/smptetimevalid.md)
  The value in the SMPTE time field is valid.
- [static var topField: CVTimeStampFlags](cvtimestampflags/topfield.md)
  The timestamp represents the top lines of an interlaced image.
- [static var videoHostTimeValid: CVTimeStampFlags](cvtimestampflags/videohosttimevalid.md)
  A convenience constant indicating that both the video time and host time fields are valid.
- [static var videoRefreshPeriodValid: CVTimeStampFlags](cvtimestampflags/videorefreshperiodvalid.md)
  The value in the video refresh period field is valid.
- [static var videoTimeValid: CVTimeStampFlags](cvtimestampflags/videotimevalid.md)
  The value in the video time field is valid.
### Initializers
- [init(rawValue: UInt64)](cvtimestampflags/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [enum CVSMPTETimeType](cvsmptetimetype.md)
- [struct CVSMPTETimeFlags](cvsmptetimeflags.md)
- [struct CVTimeFlags](cvtimeflags.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvtimestampflags)*