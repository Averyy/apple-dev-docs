# AVAudio3DMixingRenderingAlgorithm.stereoPassThrough

**Framework**: AVFAudio  
**Kind**: case

An algorithm to use when the source data doesn’t need localization.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case stereoPassThrough
```

#### Discussion

This takes mono and stereo input and passes it to channels 1 and 2 without localization. If the input and output `AudioChannelLayout` differ, mixing happens according to the [`kAudioFormatProperty_MatrixMixMap`](https://developer.apple.com/documentation/AudioToolbox/kAudioFormatProperty_MatrixMixMap) property of the layouts.

## See Also

- [AVAudio3DMixingRenderingAlgorithm.auto](avaudio3dmixingrenderingalgorithm/auto.md)
  Automatically selects the highest-quality rendering algorithm available for the current playback hardware.
- [AVAudio3DMixingRenderingAlgorithm.equalPowerPanning](avaudio3dmixingrenderingalgorithm/equalpowerpanning.md)
  An algorithm that pans the data of the mixer bus into a stereo field.
- [AVAudio3DMixingRenderingAlgorithm.HRTF](avaudio3dmixingrenderingalgorithm/hrtf.md)
  A high-quality algorithm that uses filtering to emulate 3D space in headphones.
- [AVAudio3DMixingRenderingAlgorithm.HRTFHQ](avaudio3dmixingrenderingalgorithm/hrtfhq.md)
  A higher-quality head-related transfer function rendering algorithm.
- [AVAudio3DMixingRenderingAlgorithm.soundField](avaudio3dmixingrenderingalgorithm/soundfield.md)
  An algorithm that renders to multichannel hardware.
- [AVAudio3DMixingRenderingAlgorithm.sphericalHead](avaudio3dmixingrenderingalgorithm/sphericalhead.md)
  An algorithm that emulates 3D space in headphones by simulating interaural time delays and other spatial cues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixingrenderingalgorithm/stereopassthrough)*