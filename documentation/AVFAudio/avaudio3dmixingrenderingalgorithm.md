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

### Rendering Algorithms
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
### Initializers
- [init?(rawValue: Int)](avaudio3dmixingrenderingalgorithm/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVAudioEnvironmentNode](avaudioenvironmentnode.md)
  An object that simulates a 3D audio environment.
- [class AVAudioEnvironmentDistanceAttenuationParameters](avaudioenvironmentdistanceattenuationparameters.md)
  An object that specifies the amount of attenuation distance, the gradual loss in audio intensity, and other characteristics.
- [class AVAudioEnvironmentReverbParameters](avaudioenvironmentreverbparameters.md)
  A class that encapsulates the parameters that you use to control the reverb of the environment node class.
- [protocol AVAudio3DMixing](avaudio3dmixing.md)
  A collection of properties that define 3D mixing properties.
- [struct AVAudio3DPoint](avaudio3dpoint.md)
  A structure that represents a point in 3D space.
- [struct AVAudio3DVectorOrientation](avaudio3dvectororientation.md)
  A structure that represents two orthogonal vectors that describe the orientation of the listener in 3D space.
- [struct AVAudio3DAngularOrientation](avaudio3dangularorientation.md)
  A structure that represents the angular orientation of the listener in 3D space.
- [enum AVAudio3DMixingSourceMode](avaudio3dmixingsourcemode.md)
  The source modes for the input bus of the audio environment node.
- [enum AVAudioEnvironmentOutputType](avaudioenvironmentoutputtype.md)
  The output types for using with the automatic 3D mixing rendering algorithm.
- [enum AVAudio3DMixingPointSourceInHeadMode](avaudio3dmixingpointsourceinheadmode.md)
  The in-head modes for a point source.
- [typealias AVAudio3DVector](avaudio3dvector.md)
  A structure that represents a vector in 3D space, in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixingrenderingalgorithm)*