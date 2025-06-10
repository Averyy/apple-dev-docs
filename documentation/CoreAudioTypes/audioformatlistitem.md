# AudioFormatListItem

**Framework**: Core Audio Types  
**Kind**: struct

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
struct AudioFormatListItem
```

#### Overview

```None
            an AudioStreamBasicDescription
```

```None
            an AudioChannelLayoutTag
```

## Topics

### Initializers
- [init()](audioformatlistitem/init.md)
- [init(mASBD: AudioStreamBasicDescription, mChannelLayoutTag: AudioChannelLayoutTag)](audioformatlistitem/init(masbd:mchannellayouttag:).md)
### Instance Properties
- [var mASBD: AudioStreamBasicDescription](audioformatlistitem/masbd.md)
- [var mChannelLayoutTag: AudioChannelLayoutTag](audioformatlistitem/mchannellayouttag.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias AVAudioInteger](avaudiointeger.md)
  An integer type for audio operations.
- [typealias AVAudioUInteger](avaudiouinteger.md)
  An unsigned integer type for audio operations.
- [typealias AudioSessionID](audiosessionid.md)
  A unique identifier of an audio session.
- [var kAudioUnitSampleFractionBits: Int32](kaudiounitsamplefractionbits.md)
  The number of fractional bits in fixed-point samples.
- [var COREAUDIOTYPES_VERSION: Int32](coreaudiotypes_version.md)
  A value that represents the Core Audio Types version.
- [typealias AudioSampleType](audiosampletype.md)
  The canonical audio data sample type for input and output.
- [typealias AudioUnitSampleType](audiounitsampletype.md)
  The canonical audio data sample type for audio processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audioformatlistitem)*