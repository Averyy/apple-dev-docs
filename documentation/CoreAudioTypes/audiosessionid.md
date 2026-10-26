# AudioSessionID

**Framework**: Core Audio Types  
**Kind**: typealias  
**Role**: Type Alias

A unique identifier of an audio session.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
typealias AudioSessionID = UInt32
```

```c
typedef uint32_t AudioSessionID;
```

## See Also

### Common Types
- [typealias AVAudioInteger](./avaudiointeger.md)
  An integer type for audio operations.
- [typealias AVAudioUInteger](./avaudiouinteger.md)
  An unsigned integer type for audio operations.
- [var kAudioUnitSampleFractionBits: Int32](./kaudiounitsamplefractionbits.md)
  The number of fractional bits in fixed-point samples.
- [var COREAUDIOTYPES_VERSION: Int32](./coreaudiotypes_version.md)
  A value that represents the Core Audio Types version.
- [typealias AudioSampleType](./audiosampletype.md)
  The canonical audio data sample type for input and output.
- [typealias AudioUnitSampleType](./audiounitsampletype.md)
  The canonical audio data sample type for audio processing.
- [struct AudioFormatListItem](./audioformatlistitem.md)
- [AVAudioSessionErrorInsufficientPriority](./avaudiosessionerrorinsufficientpriority.md)
  An error code that indicates the app isn’t allowed to set the audio category because it’s in use by another app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiosessionid)*