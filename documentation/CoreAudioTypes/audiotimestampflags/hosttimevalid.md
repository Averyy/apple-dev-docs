# hostTimeValid

**Framework**: Core Audio Types  
**Kind**: property  
**Role**: Type Property

A flag that indicates that the host time is valid.

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
static var hostTimeValid: AudioTimeStampFlags { get }
```

```c
kAudioTimeStampHostTimeValid
```

## See Also

### Type Properties
- [static var rateScalarValid: AudioTimeStampFlags](./ratescalarvalid.md)
  A flag that indicates that the rate scalar is valid.
- [static var sampleHostTimeValid: AudioTimeStampFlags](./samplehosttimevalid.md)
  A flag that indicates that the sample frame time and the host time are valid.
- [static var sampleTimeValid: AudioTimeStampFlags](./sampletimevalid.md)
  A flag that indicates that the sample frame time is valid.
- [static var smpteTimeValid: AudioTimeStampFlags](./smptetimevalid.md)
  A flag that indicates that the SMPTE time is valid.
- [static var wordClockTimeValid: AudioTimeStampFlags](./wordclocktimevalid.md)
  A flag that indicates that the word clock time is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiotimestampflags/hosttimevalid)*