# AVAudio3DVectorOrientation

**Framework**: AVFAudio  
**Kind**: struct

A structure that represents two orthogonal vectors that describe the orientation of the listener in 3D space.

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
struct AVAudio3DVectorOrientation
```

#### Overview

Two orthogonal vectors describe the orientation of the listener. The forward vector points in the direction the listener faces. The up vector is orthogonal to the forward vector and points upward from the listener’s head.

## Topics

### Creating a Vector Orientation
- [init()](avaudio3dvectororientation/init.md)
  Creates a 3D vector orientation instance.
- [init(forward: AVAudio3DVector, up: AVAudio3DVector)](avaudio3dvectororientation/init(forward:up:).md)
  Creates a 3D vector orientation instance using the forward and up vectors you specify.
- [func AVAudioMake3DVectorOrientation(AVAudio3DVector, AVAudio3DVector) -> AVAudio3DVectorOrientation](avaudiomake3dvectororientation(_:_:).md)
  Creates a 3D vector orientation instance using the forward and up vectors you specify.
### Getting Vector Orientation Properties
- [var forward: AVAudio3DVector](avaudio3dvectororientation/forward.md)
  The forward vector points in the direction that the listener faces.
- [var up: AVAudio3DVector](avaudio3dvectororientation/up.md)
  The up vector is orthogonal to the forward vector and points upward from the listener’s head.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
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
- [struct AVAudio3DAngularOrientation](avaudio3dangularorientation.md)
  A structure that represents the angular orientation of the listener in 3D space.
- [enum AVAudio3DMixingSourceMode](avaudio3dmixingsourcemode.md)
  The source modes for the input bus of the audio environment node.
- [enum AVAudio3DMixingRenderingAlgorithm](avaudio3dmixingrenderingalgorithm.md)
  The types of rendering algorithms available per input bus of the environment node.
- [enum AVAudioEnvironmentOutputType](avaudioenvironmentoutputtype.md)
  The output types for using with the automatic 3D mixing rendering algorithm.
- [enum AVAudio3DMixingPointSourceInHeadMode](avaudio3dmixingpointsourceinheadmode.md)
  The in-head modes for a point source.
- [typealias AVAudio3DVector](avaudio3dvector.md)
  A structure that represents a vector in 3D space, in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dvectororientation)*