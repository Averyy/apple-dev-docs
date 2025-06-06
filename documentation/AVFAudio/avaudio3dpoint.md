# AVAudio3DPoint

**Framework**: AVFAudio  
**Kind**: struct

A structure that represents a point in 3D space.

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
struct AVAudio3DPoint
```

#### Overview

Classes that deal with 3D audio, such as those adopting [`AVAudioMixing`](avaudiomixing.md) and [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md), use this structure. The system represents this point in meters.

## Topics

### Creating a Point
- [init()](avaudio3dpoint/init.md)
  Creates a 3D point.
- [init(x: Float, y: Float, z: Float)](avaudio3dpoint/init(x:y:z:).md)
  Creates a 3D point using the x, y, and z coordinates you specify.
- [func AVAudioMake3DPoint(Float, Float, Float) -> AVAudio3DPoint](avaudiomake3dpoint(_:_:_:).md)
  Creates a 3D point using the x, y, and z coordinates you specify.
### Getting Point Properties
- [var x: Float](avaudio3dpoint/x.md)
  The location on the x-axis, in meters.
- [var y: Float](avaudio3dpoint/y.md)
  The location on the y-axis, in meters.
- [var z: Float](avaudio3dpoint/z.md)
  The location on the z-axis, in meters.

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
- [enum AVAudio3DMixingPointSourceInHeadMode](avaudio3dmixingpointsourceinheadmode.md)
  The in-head modes for a point source.
- [typealias AVAudio3DVector](avaudio3dvector.md)
  A structure that represents a vector in 3D space, in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dpoint)*