# AVAudioMixInputParametersTrackID

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Special value for the trackID property of AVAudioMixInputParameters.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum AVAudioMixInputParametersTrackID
```

```c
enum AVAudioMixInputParametersTrackID : CMPersistentTrackID;
```

## Topics

### Creating a track identifier
- [init?(rawValue: CMPersistentTrackID)](./avaudiomixinputparameterstrackid/init%28rawvalue%29.md)
### Track identifiers
- [AVAudioMixInputParametersTrackID.mixID](./avaudiomixinputparameterstrackid/mixid.md)
  Indicates that the specified input parameters should be applied to the mix of all audio tracks rather than to a single specific audio track. This is particularly useful for setting up volume ramps or an audio tap for streaming playback.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Mixing
- [class AVAudioMix](./avaudiomix.md)
  An object that manages the input parameters for mixing audio tracks.
- [class AVAudioMixInputParameters](./avaudiomixinputparameters.md)
  An object that represents the parameters that you apply when adding an audio track to a mix.
- [class AVMutableAudioMix](./avmutableaudiomix.md)
  An object that manages the input parameters for mixing audio tracks.
- [class AVMutableAudioMixInputParameters](./avmutableaudiomixinputparameters.md)
  The parameters you use when adding an audio track to a mix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameterstrackid)*