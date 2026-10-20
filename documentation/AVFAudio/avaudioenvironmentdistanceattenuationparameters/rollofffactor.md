# rolloffFactor

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A factor that determines the attenuation curve.

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
var rolloffFactor: Float { get set }
```

```objc
@property (nonatomic) float rolloffFactor;
```

#### Discussion

A higher value results in a steeper attenuation curve. The default value is `1.0`, and the value must be greater than `0.0`.

This property is relevant for [`AVAudioEnvironmentDistanceAttenuationModel.exponential`](../avaudioenvironmentdistanceattenuationmodel/exponential.md), [`AVAudioEnvironmentDistanceAttenuationModel.inverse`](../avaudioenvironmentdistanceattenuationmodel/inverse.md), and [`AVAudioEnvironmentDistanceAttenuationModel.linear`](../avaudioenvironmentdistanceattenuationmodel/linear.md).

## See Also

### Configuring distance attenuation
- [var maximumDistance: Float](./maximumdistance.md)
  The distance beyond which the node applies no further attenuation, in meters.
- [var referenceDistance: Float](./referencedistance.md)
  The minimum distance at which the node applies attenuation, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentdistanceattenuationparameters/rollofffactor)*