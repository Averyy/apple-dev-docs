# AVAudioTimePitchAlgorithm

**Framework**: AVFoundation  
**Kind**: struct

An algorithm used to set the audio pitch as the rate changes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct AVAudioTimePitchAlgorithm
```

## Topics

### Type Properties
- [static let lowQualityZeroLatency: AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm/lowqualityzerolatency.md)
  A low-quality and very low computationally intensive pitch algorithm.
- [static let spectral: AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm/spectral.md)
  A highest-quality time pitch algorithm that’s suitable for music.
- [static let timeDomain: AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm/timedomain.md)
  A modest quality time pitch algorithm that’s suitable for voice.
- [static let varispeed: AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm/varispeed.md)
  A high-quality time pitch algorithm that doesn’t perform pitch correction.
### Initializers
- [init(rawValue: String)](avaudiotimepitchalgorithm/init(rawvalue:).md)
  Creates a new time pitch algorithm with a string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm?](avaudiomixinputparameters/audiotimepitchalgorithm.md)
  The processing algorithm used to manage audio pitch for scaled audio edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithm)*