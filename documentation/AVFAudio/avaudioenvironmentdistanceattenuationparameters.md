# AVAudioEnvironmentDistanceAttenuationParameters

**Framework**: AVFAudio  
**Kind**: class

An object that specifies the amount of attenuation distance, the gradual loss in audio intensity, and other characteristics.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioEnvironmentDistanceAttenuationParameters
```

#### Overview

> ❗ **Important**:  A source object (for example, [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md)) provides an instance to this object. You can’t create standalone instances.

 A source object (for example, [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md)) provides an instance to this object. You can’t create standalone instances.

## Topics

### Getting and Setting the Attenuation Model
- [var distanceAttenuationModel: AVAudioEnvironmentDistanceAttenuationModel](avaudioenvironmentdistanceattenuationparameters/distanceattenuationmodel.md)
  The distance attenuation model that describes the drop-off in gain as the source moves away from the listener.
- [enum AVAudioEnvironmentDistanceAttenuationModel](avaudioenvironmentdistanceattenuationmodel.md)
  Types of distance attenuation models.
### Getting and Setting the Attenuation Values
- [var maximumDistance: Float](avaudioenvironmentdistanceattenuationparameters/maximumdistance.md)
  The distance beyond which the node applies no further attenuation, in meters.
- [var referenceDistance: Float](avaudioenvironmentdistanceattenuationparameters/referencedistance.md)
  The minimum distance at which the node applies attenuation, in meters.
- [var rolloffFactor: Float](avaudioenvironmentdistanceattenuationparameters/rollofffactor.md)
  A factor that determines the attenuation curve.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioEnvironmentNode](avaudioenvironmentnode.md)
  An object that simulates a 3D audio environment.
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
- [enum AVAudio3DMixingPointSourceInHeadMode](avaudio3dmixingpointsourceinheadmode.md)
  The in-head modes for a point source.
- [typealias AVAudio3DVector](avaudio3dvector.md)
  A structure that represents a vector in 3D space, in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentdistanceattenuationparameters)*