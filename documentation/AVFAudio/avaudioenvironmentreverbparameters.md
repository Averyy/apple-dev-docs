# AVAudioEnvironmentReverbParameters

**Framework**: AVFAudio  
**Kind**: class

A class that encapsulates the parameters that you use to control the reverb of the environment node class.

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
class AVAudioEnvironmentReverbParameters
```

#### Overview

Use reverberation to simulate the acoustic characteristics of an environment. The [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md) class has a built-in reverb that describe the space that the listener is in.

The reverb has a single filter that sits at the end of the chain. You use this filter to shape the overall sound of the reverb. For instance, select one of the reverb presets to simulate the general space, and then use the filter to brighten or darken the overall sound.

You can’t create a standalone instance of [`AVAudioEnvironmentReverbParameters`](avaudioenvironmentreverbparameters.md). Only an instance vended by a source object is valid, such as an [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md) instance.

## Topics

### Enabling and Disabling Reverb
- [var enable: Bool](avaudioenvironmentreverbparameters/enable.md)
  A Boolean value that indicates whether reverberation is in an enabled state.
### Getting and Setting Reverb Values
- [var level: Float](avaudioenvironmentreverbparameters/level.md)
  Controls the amount of reverb, in decibels.
- [var filterParameters: AVAudioUnitEQFilterParameters](avaudioenvironmentreverbparameters/filterparameters.md)
  A filter that the system applies to the output.
- [func loadFactoryReverbPreset(AVAudioUnitReverbPreset)](avaudioenvironmentreverbparameters/loadfactoryreverbpreset(_:).md)
  Loads one of the reverbs factory presets.

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
- [class AVAudioEnvironmentDistanceAttenuationParameters](avaudioenvironmentdistanceattenuationparameters.md)
  An object that specifies the amount of attenuation distance, the gradual loss in audio intensity, and other characteristics.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentreverbparameters)*