# AVAudioEnvironmentDistanceAttenuationModel

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Types of distance attenuation models.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum AVAudioEnvironmentDistanceAttenuationModel
```

```c
enum AVAudioEnvironmentDistanceAttenuationModel : NSInteger;
```

## Overview

Distance attenuation is the natural attenuation of sound when traveling from the source to the listener. The different attenuation models describe the drop-off in gain as the source moves away from the listener.

## Topics

### Creating an attenuation model
- [init?(rawValue: Int)](./avaudioenvironmentdistanceattenuationmodel/init%28rawvalue%29.md)
### Choosing an attenuation model
- [AVAudioEnvironmentDistanceAttenuationModel.exponential](./avaudioenvironmentdistanceattenuationmodel/exponential.md)
  An exponential model that describes the drop-off in gain as the source moves away from the listener.
- [AVAudioEnvironmentDistanceAttenuationModel.inverse](./avaudioenvironmentdistanceattenuationmodel/inverse.md)
  An inverse model that describes the drop-off in gain as the source moves away from the listener.
- [AVAudioEnvironmentDistanceAttenuationModel.linear](./avaudioenvironmentdistanceattenuationmodel/linear.md)
  A linear model that describes the drop-off in gain as the source moves away from the listener.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Choosing an attenuation model
- [var distanceAttenuationModel: AVAudioEnvironmentDistanceAttenuationModel](./avaudioenvironmentdistanceattenuationparameters/distanceattenuationmodel.md)
  The distance attenuation model that describes the drop-off in gain as the source moves away from the listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentdistanceattenuationmodel)*