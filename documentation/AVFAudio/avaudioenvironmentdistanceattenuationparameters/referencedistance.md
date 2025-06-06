# referenceDistance

**Framework**: AVFAudio  
**Kind**: property

The minimum distance at which the node applies attenuation, in meters.

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
var referenceDistance: Float { get set }
```

#### Discussion

The default value is `1.0` meter.

This property is relevant for [`AVAudioEnvironmentDistanceAttenuationModel.inverse`](avaudioenvironmentdistanceattenuationmodel/inverse.md) and [`AVAudioEnvironmentDistanceAttenuationModel.linear`](avaudioenvironmentdistanceattenuationmodel/linear.md).

## See Also

- [var maximumDistance: Float](avaudioenvironmentdistanceattenuationparameters/maximumdistance.md)
  The distance beyond which the node applies no further attenuation, in meters.
- [var rolloffFactor: Float](avaudioenvironmentdistanceattenuationparameters/rollofffactor.md)
  A factor that determines the attenuation curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentdistanceattenuationparameters/referencedistance)*