# maximumDistance

**Framework**: AVFAudio  
**Kind**: property

The distance beyond which the node applies no further attenuation, in meters.

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
var maximumDistance: Float { get set }
```

#### Discussion

The default value is `100000.0` meters.

This property is relevant for [`AVAudioEnvironmentDistanceAttenuationModel.inverse`](avaudioenvironmentdistanceattenuationmodel/inverse.md).

## See Also

- [var referenceDistance: Float](avaudioenvironmentdistanceattenuationparameters/referencedistance.md)
  The minimum distance at which the node applies attenuation, in meters.
- [var rolloffFactor: Float](avaudioenvironmentdistanceattenuationparameters/rollofffactor.md)
  A factor that determines the attenuation curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentdistanceattenuationparameters/maximumdistance)*