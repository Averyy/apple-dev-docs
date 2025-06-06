# AVAudio3DMixingPointSourceInHeadMode

**Framework**: AVFAudio  
**Kind**: enum

The in-head modes for a point source.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum AVAudio3DMixingPointSourceInHeadMode
```

#### Overview

The in-head mode that determines what happens when a [`AVAudio3DMixingSourceMode.pointSource`](avaudio3dmixingsourcemode/pointsource.md) moves inside the head of the listener. The in-head mode applies when using the [`AVAudio3DMixingRenderingAlgorithm.auto`](avaudio3dmixingrenderingalgorithm/auto.md) rendering algorithm.

## Topics

### In-Head Modes
- [AVAudio3DMixingPointSourceInHeadMode.mono](avaudio3dmixingpointsourceinheadmode/mono.md)
  The point source remains a single mono source inside the head of the listener regardless of the channels it consists of.
- [AVAudio3DMixingPointSourceInHeadMode.bypass](avaudio3dmixingpointsourceinheadmode/bypass.md)
  The point source distributes into each output channel inside the head of the listener.
### Initializers
- [init?(rawValue: Int)](avaudio3dmixingpointsourceinheadmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [enum AVAudio3DMixingRenderingAlgorithm](avaudio3dmixingrenderingalgorithm.md)
  The types of rendering algorithms available per input bus of the environment node.
- [enum AVAudioEnvironmentOutputType](avaudioenvironmentoutputtype.md)
  The output types for using with the automatic 3D mixing rendering algorithm.
- [typealias AVAudio3DVector](avaudio3dvector.md)
  A structure that represents a vector in 3D space, in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixingpointsourceinheadmode)*