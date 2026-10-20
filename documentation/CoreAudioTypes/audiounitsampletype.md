# AudioUnitSampleType

**Framework**: Core Audio Types  
**Kind**: typealias  
**Role**: Type Alias

The canonical audio data sample type for audio processing.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

> **Deprecated**: The concept of canonical formats is deprecated

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
typealias AudioUnitSampleType = Int32
```

*Mac Catalyst, macOS*

```swift
typealias AudioUnitSampleType = Float32
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```c
typedef SInt32 AudioUnitSampleType;
```

*Mac Catalyst, macOS*

```c
typedef Float32 AudioUnitSampleType;
```

#### Discussion

The canonical audio sample type for audio units and other audio processing in iPhone OS is noninterleaved linear PCM with 8.24-bit fixed-point samples.

## See Also

### Common Types
- [typealias AVAudioInteger](./avaudiointeger.md)
  An integer type for audio operations.
- [typealias AVAudioUInteger](./avaudiouinteger.md)
  An unsigned integer type for audio operations.
- [typealias AudioSessionID](./audiosessionid.md)
  A unique identifier of an audio session.
- [var kAudioUnitSampleFractionBits: Int32](./kaudiounitsamplefractionbits.md)
  The number of fractional bits in fixed-point samples.
- [var COREAUDIOTYPES_VERSION: Int32](./coreaudiotypes_version.md)
  A value that represents the Core Audio Types version.
- [typealias AudioSampleType](./audiosampletype.md)
  The canonical audio data sample type for input and output.
- [struct AudioFormatListItem](./audioformatlistitem.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiounitsampletype)*