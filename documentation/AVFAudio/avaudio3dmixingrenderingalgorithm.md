# AVAudio3DMixingRenderingAlgorithm

**Framework**: AVFAudio  
**Kind**: enum

The types of rendering algorithms available per input bus of the environment node.

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
enum AVAudio3DMixingRenderingAlgorithm
```

#### Overview

The rendering algorithms differ in quality and CPU cost. [`AVAudio3DMixingRenderingAlgorithm.equalPowerPanning`](avaudio3dmixingrenderingalgorithm/equalpowerpanning.md) is the simplest panning algorithm and the least expensive computationally.

When rendering to multichannel hardware, most of the rendering algorithms only render to channels 1 and 2, excluding [`AVAudio3DMixingRenderingAlgorithm.soundField`](avaudio3dmixingrenderingalgorithm/soundfield.md) and [`AVAudio3DMixingRenderingAlgorithm.auto`](avaudio3dmixingrenderingalgorithm/auto.md).

## Topics

### Creating a rendering algorithm
- [init?(rawValue: Int)](avaudio3dmixingrenderingalgorithm/init(rawvalue:).md)
### Choosing a rendering algorithm
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
- [AVAudio3DMixingRenderingAlgorithm.stereoPassThrough](avaudio3dmixingrenderingalgorithm/stereopassthrough.md)
  An algorithm to use when the source data doesn’t need localization.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var renderingAlgorithm: AVAudio3DMixingRenderingAlgorithm](avaudio3dmixing/renderingalgorithm.md)
  The type of rendering algorithm the mixer uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixingrenderingalgorithm)*