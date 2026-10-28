# AVAudioEnvironmentDistanceAttenuationParameters

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAudioEnvironmentDistanceAttenuationParameters : NSObject
```

## Overview

> ❗ **Important**:  A source object (for example, [`AVAudioEnvironmentNode`](./avaudioenvironmentnode.md)) provides an instance to this object. You can’t create standalone instances.

## Topics

### Choosing an attenuation model
- [var distanceAttenuationModel: AVAudioEnvironmentDistanceAttenuationModel](./avaudioenvironmentdistanceattenuationparameters/distanceattenuationmodel.md)
  The distance attenuation model that describes the drop-off in gain as the source moves away from the listener.
- [enum AVAudioEnvironmentDistanceAttenuationModel](./avaudioenvironmentdistanceattenuationmodel.md)
  Types of distance attenuation models.
### Configuring distance attenuation
- [var maximumDistance: Float](./avaudioenvironmentdistanceattenuationparameters/maximumdistance.md)
  The distance beyond which the node applies no further attenuation, in meters.
- [var referenceDistance: Float](./avaudioenvironmentdistanceattenuationparameters/referencedistance.md)
  The minimum distance at which the node applies attenuation, in meters.
- [var rolloffFactor: Float](./avaudioenvironmentdistanceattenuationparameters/rollofffactor.md)
  A factor that determines the attenuation curve.

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
- [class AVAudioEnvironmentReverbParameters](./avaudioenvironmentreverbparameters.md)
  A class that encapsulates the parameters that you use to control the reverb of the environment node class.
- [protocol AVAudio3DMixing](./avaudio3dmixing.md)
  A collection of properties that define 3D mixing properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentdistanceattenuationparameters)*