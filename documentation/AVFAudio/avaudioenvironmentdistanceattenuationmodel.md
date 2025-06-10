# AVAudioEnvironmentDistanceAttenuationModel

**Framework**: AVFAudio  
**Kind**: enum

Types of distance attenuation models.

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
enum AVAudioEnvironmentDistanceAttenuationModel
```

#### Overview

Distance attenuation is the natural attenuation of sound when traveling from the source to the listener. The different attenuation models describe the drop-off in gain as the source moves away from the listener.

## Topics

### Attenuation Models
- [AVAudioEnvironmentDistanceAttenuationModel.exponential](avaudioenvironmentdistanceattenuationmodel/exponential.md)
  An exponential model that describes the drop-off in gain as the source moves away from the listener.
- [AVAudioEnvironmentDistanceAttenuationModel.inverse](avaudioenvironmentdistanceattenuationmodel/inverse.md)
  An inverse model that describes the drop-off in gain as the source moves away from the listener.
- [AVAudioEnvironmentDistanceAttenuationModel.linear](avaudioenvironmentdistanceattenuationmodel/linear.md)
  A linear model that describes the drop-off in gain as the source moves away from the listener.
### Initializers
- [init?(rawValue: Int)](avaudioenvironmentdistanceattenuationmodel/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var distanceAttenuationModel: AVAudioEnvironmentDistanceAttenuationModel](avaudioenvironmentdistanceattenuationparameters/distanceattenuationmodel.md)
  The distance attenuation model that describes the drop-off in gain as the source moves away from the listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentdistanceattenuationmodel)*