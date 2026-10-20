# AVAudioEnvironmentReverbParameters

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAudioEnvironmentReverbParameters : NSObject
```

#### Overview

Use reverberation to simulate the acoustic characteristics of an environment. The [`AVAudioEnvironmentNode`](./avaudioenvironmentnode.md) class has a built-in reverb that describe the space that the listener is in.

The reverb has a single filter that sits at the end of the chain. You use this filter to shape the overall sound of the reverb. For instance, select one of the reverb presets to simulate the general space, and then use the filter to brighten or darken the overall sound.

You can’t create a standalone instance of [`AVAudioEnvironmentReverbParameters`](./avaudioenvironmentreverbparameters.md). Only an instance vended by a source object is valid, such as an [`AVAudioEnvironmentNode`](./avaudioenvironmentnode.md) instance.

## Topics

### Enabling and disabling reverb
- [var enable: Bool](./avaudioenvironmentreverbparameters/enable.md)
  A Boolean value that indicates whether reverberation is in an enabled state.
### Getting and setting reverb values
- [var level: Float](./avaudioenvironmentreverbparameters/level.md)
  Controls the amount of reverb, in decibels.
- [var filterParameters: AVAudioUnitEQFilterParameters](./avaudioenvironmentreverbparameters/filterparameters.md)
  A filter that the system applies to the output.
- [func loadFactoryReverbPreset(AVAudioUnitReverbPreset)](./avaudioenvironmentreverbparameters/loadfactoryreverbpreset%28_%29.md)
  Loads one of the reverbs factory presets.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Spatial audio
- [class AVAudioEnvironmentNode](./avaudioenvironmentnode.md)
  An object that simulates a 3D audio environment.
- [class AVAudioEnvironmentDistanceAttenuationParameters](./avaudioenvironmentdistanceattenuationparameters.md)
  An object that specifies the amount of attenuation distance, the gradual loss in audio intensity, and other characteristics.
- [protocol AVAudio3DMixing](./avaudio3dmixing.md)
  A collection of properties that define 3D mixing properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentreverbparameters)*