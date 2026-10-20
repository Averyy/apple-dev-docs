# distanceAttenuationModel

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The distance attenuation model that describes the drop-off in gain as the source moves away from the listener.

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
var distanceAttenuationModel: AVAudioEnvironmentDistanceAttenuationModel { get set }
```

```objc
@property (nonatomic) AVAudioEnvironmentDistanceAttenuationModel distanceAttenuationModel;
```

#### Discussion

The default value is the [`AVAudioEnvironmentDistanceAttenuationModel.inverse`](../avaudioenvironmentdistanceattenuationmodel/inverse.md) attenuation model.

## See Also

### Choosing an attenuation model
- [enum AVAudioEnvironmentDistanceAttenuationModel](../avaudioenvironmentdistanceattenuationmodel.md)
  Types of distance attenuation models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentdistanceattenuationparameters/distanceattenuationmodel)*