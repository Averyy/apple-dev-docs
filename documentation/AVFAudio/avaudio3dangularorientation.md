# AVAudio3DAngularOrientation

**Framework**: AVFAudio  
**Kind**: struct

A structure that represents the angular orientation of the listener in 3D space.

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
struct AVAudio3DAngularOrientation
```

#### Overview

This represents the three angles that describe the orientation of a listener’s head — yaw, pitch, and roll.

## Topics

### Creating an Angular Orientation
- [init()](avaudio3dangularorientation/init.md)
  Creates an angular orientation.
- [init(yaw: Float, pitch: Float, roll: Float)](avaudio3dangularorientation/init(yaw:pitch:roll:).md)
  Creates a 3D angular orientation using the yaw, pitch, and roll values you specify.
- [func AVAudioMake3DAngularOrientation(Float, Float, Float) -> AVAudio3DAngularOrientation](avaudiomake3dangularorientation(_:_:_:).md)
  Creates a 3D angular orientation using the yaw, pitch, and roll values you specify.
### Getting Angular Orientation Properties
- [var yaw: Float](avaudio3dangularorientation/yaw.md)
  The side-to-side movement of the listener’s head.
- [var pitch: Float](avaudio3dangularorientation/pitch.md)
  The up-and-down movement of the listener’s head.
- [var roll: Float](avaudio3dangularorientation/roll.md)
  The tilt of the listener’s head.

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
- [struct AVAudio3DVectorOrientation](avaudio3dvectororientation.md)
  A structure that represents two orthogonal vectors that describe the orientation of the listener in 3D space.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dangularorientation)*