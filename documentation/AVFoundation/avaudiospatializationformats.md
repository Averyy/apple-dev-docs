# AVAudioSpatializationFormats

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A structure that defines the spatialization formats that a player item supports.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct AVAudioSpatializationFormats
```

```c
enum AVAudioSpatializationFormats : NSUInteger;
```

## Topics

### Spatialization formats
- [static var monoAndStereo: AVAudioSpatializationFormats](./avaudiospatializationformats/monoandstereo.md)
  A value that indicates the player item only supports mono and stereo layouts for audio spatialization.
- [static var multichannel: AVAudioSpatializationFormats](./avaudiospatializationformats/multichannel.md)
  A value that indicates the player item only supports multichannel layouts for audio spatialization.
- [static var monoStereoAndMultichannel: AVAudioSpatializationFormats](./avaudiospatializationformats/monostereoandmultichannel.md)
  A value that indicates the player item supports mono, stereo, and multichannel layouts for audio spatialization.
- [AVAudioSpatializationFormatNone](./avaudiospatializationformats/avaudiospatializationformatnone.md)
  A value that indicates the player item doesn’t support audio spatialization.
### Initializers
- [init(rawValue: UInt)](./avaudiospatializationformats/init%28rawvalue%29.md)
  Initializes a format with a string value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Configuring audio
- [var audioMix: AVAudioMix?](./avplayeritem/audiomix.md)
  The audio mix parameters to be applied during playback.
- [var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm](./avplayeritem/audiotimepitchalgorithm.md)
  The processing algorithm used to manage audio pitch for scaled audio edits.
- [var allowedAudioSpatializationFormats: AVAudioSpatializationFormats](./avplayeritem/allowedaudiospatializationformats.md)
  The source audio channel layouts the player item supports for spatialization.
- [var isAudioSpatializationAllowed: Bool](./avplayeritem/isaudiospatializationallowed.md)
  A Boolean value that indicates whether the player item allows spatialized audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avaudiospatializationformats)*