# AVAudio3DMixingRenderingAlgorithm.soundField

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

An algorithm that renders to multichannel hardware.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case soundField
```

```c
AVAudio3DMixingRenderingAlgorithmSoundField
```

#### Discussion

This takes data the system renders with [`AVAudio3DMixingRenderingAlgorithm.soundField`](./soundfield.md) and distributes it among all of the output channels with a weighting toward the location of the sound. This algorithm is very effective for ambient sounds. Those sounds may derive from a specific location, but they fill the listener’s entire space.

## See Also

### Choosing a rendering algorithm
- [AVAudio3DMixingRenderingAlgorithm.auto](./auto.md)
  Automatically selects the highest-quality rendering algorithm available for the current playback hardware.
- [AVAudio3DMixingRenderingAlgorithm.equalPowerPanning](./equalpowerpanning.md)
  An algorithm that pans the data of the mixer bus into a stereo field.
- [AVAudio3DMixingRenderingAlgorithm.HRTF](./hrtf.md)
  A high-quality algorithm that uses filtering to emulate 3D space in headphones.
- [AVAudio3DMixingRenderingAlgorithm.HRTFHQ](./hrtfhq.md)
  A higher-quality head-related transfer function rendering algorithm.
- [AVAudio3DMixingRenderingAlgorithm.sphericalHead](./sphericalhead.md)
  An algorithm that emulates 3D space in headphones by simulating interaural time delays and other spatial cues.
- [AVAudio3DMixingRenderingAlgorithm.stereoPassThrough](./stereopassthrough.md)
  An algorithm to use when the source data doesn’t need localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixingrenderingalgorithm/soundfield)*