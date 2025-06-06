# audioTapProcessor

**Framework**: AVFoundation  
**Kind**: property

The audio processing tap associated with the track.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var audioTapProcessor: MTAudioProcessingTap? { get }
```

#### Discussion

You can use the audio tap to access the track’s audio data before it is played, read, or exported. This property is `nil` by default.

The process of setting up a tap requires the configuration of an instance of [`AVMutableAudioMixInputParameters`](avmutableaudiomixinputparameters.md). If an instance of [`AVMutableAudioMixInputParameters`](avmutableaudiomixinputparameters.md) is present in the [`inputParameters`](avaudiomix/inputparameters.md) array of an [`AVAudioMix`](avaudiomix.md), the results of mutating the [`AVMutableAudioMixInputParameters`](avmutableaudiomixinputparameters.md) while the audio mix is in use are undefined


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters/audiotapprocessor)*