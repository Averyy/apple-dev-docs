# AVAudioMixInputParametersTrackID

**Framework**: AVFoundation  
**Kind**: enum

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum AVAudioMixInputParametersTrackID
```

#### Overview

Special value for the trackID property of AVAudioMixInputParameters.

Indicates that the specified input parameters should be applied to the mix of all audio tracks rather than to a single specific audio track. This is particularly useful for setting up volume ramps or an audio tap for streaming playback.

## Topics

### Creating a track identifier
- [init?(rawValue: CMPersistentTrackID)](avaudiomixinputparameterstrackid/init(rawvalue:).md)
### Track identifiers
- [AVAudioMixInputParametersTrackID.mixID](avaudiomixinputparameterstrackid/mixid.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVAudioMix](avaudiomix.md)
  An object that manages the input parameters for mixing audio tracks.
- [class AVAudioMixInputParameters](avaudiomixinputparameters.md)
  An object that represents the parameters that you apply when adding an audio track to a mix.
- [class AVMutableAudioMix](avmutableaudiomix.md)
  An object that manages the input parameters for mixing audio tracks.
- [class AVMutableAudioMixInputParameters](avmutableaudiomixinputparameters.md)
  The parameters you use when adding an audio track to a mix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameterstrackid)*