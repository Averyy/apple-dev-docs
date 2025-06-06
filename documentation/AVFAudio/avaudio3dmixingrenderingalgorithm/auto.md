# AVAudio3DMixingRenderingAlgorithm.auto

**Framework**: AVFAudio  
**Kind**: case

Automatically selects the highest-quality rendering algorithm available for the current playback hardware.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case auto
```

#### Discussion

This selects the highest-quality rendering algorithm available for the current playback hardware.

The algorithm may not be identical to other existing algorithms. It may change in the future as new algorithms emerge.

When in manual rendering mode or wired output, you may need to set the [`outputType`](avaudioenvironmentnode/outputtype.md) on [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md). Multichannel rendering requires setting a channel layout on an [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md) output.

## See Also

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
- [AVAudio3DMixingRenderingAlgorithm.stereoPassThrough](avaudio3dmixingrenderingalgorithm/stereopassthrough.md)
  An algorithm to use when the source data doesn’t need localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixingrenderingalgorithm/auto)*