# AudioTimeStampFlags

**Framework**: Core Audio Types  
**Kind**: struct

A structure that represents flags for a timestamp.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct AudioTimeStampFlags
```

## Topics

### Initializers
- [init(rawValue: UInt32)](audiotimestampflags/init(rawvalue:).md)
  Creates a flag with an unsigned-integer value.
### Type Properties
- [static var hostTimeValid: AudioTimeStampFlags](audiotimestampflags/hosttimevalid.md)
  A flag that indicates that the host time is valid.
- [static var rateScalarValid: AudioTimeStampFlags](audiotimestampflags/ratescalarvalid.md)
  A flag that indicates that the rate scalar is valid.
- [static var sampleHostTimeValid: AudioTimeStampFlags](audiotimestampflags/samplehosttimevalid.md)
  A flag that indicates that the sample frame time and the host time are valid.
- [static var sampleTimeValid: AudioTimeStampFlags](audiotimestampflags/sampletimevalid.md)
  A flag that indicates that the sample frame time is valid.
- [static var smpteTimeValid: AudioTimeStampFlags](audiotimestampflags/smptetimevalid.md)
  A flag that indicates that the SMPTE time is valid.
- [static var wordClockTimeValid: AudioTimeStampFlags](audiotimestampflags/wordclocktimevalid.md)
  A flag that indicates that the word clock time is valid.

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

- [struct AudioTimeStamp](audiotimestamp.md)
  A structure that represents a timestamp value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiotimestampflags)*