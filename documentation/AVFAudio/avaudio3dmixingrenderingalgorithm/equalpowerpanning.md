# AVAudio3DMixingRenderingAlgorithm.equalPowerPanning

**Framework**: AVFAudio  
**Kind**: case

An algorithm that pans the data of the mixer bus into a stereo field.

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
case equalPowerPanning
```

#### Discussion

This is analogous to the pan knob on a mixing board channel strip.

## See Also

- [AVAudio3DMixingRenderingAlgorithm.auto](avaudio3dmixingrenderingalgorithm/auto.md)
  Automatically selects the highest-quality rendering algorithm available for the current playback hardware.
- [AVAudio3DMixingRenderingAlgorithm.HRTF](avaudio3dmixingrenderingalgorithm/hrtf.md)
  A high-quality algorithm that uses filtering to emulate 3D space in headphones.
- [AVAudio3DMixingRenderingAlgorithm.HRTFHQ](avaudio3dmixingrenderingalgorithm/hrtfhq.md)
  A higher-quality head-related transfer function rendering algorithm.
- [AVAudio3DMixingRenderingAlgorithm.soundField](avaudio3dmixingrenderingalgorithm/soundfield.md)
  An algorithm that renders to multichannel hardware.
- [AVAudio3DMixingRenderingAlgorithm.sphericalHead](avaudio3dmixingrenderingalgorithm/sphericalhead.md)
  An algorithm that emulates 3D space in headphones by simulating interaural time delays and other spatial cues.
- [AVAudio3DMixingRenderingAlgorithm.stereoPassThrough](avaudio3dmixingrenderingalgorithm/stereopassthrough.md)
  An algorithm to use when the source data doesn’t need localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixingrenderingalgorithm/equalpowerpanning)*