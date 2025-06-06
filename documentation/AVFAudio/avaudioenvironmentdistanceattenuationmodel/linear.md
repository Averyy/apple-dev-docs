# AVAudioEnvironmentDistanceAttenuationModel.linear

**Framework**: AVFAudio  
**Kind**: case

A linear model that describes the drop-off in gain as the source moves away from the listener.

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
case linear
```

#### Discussion

The framework calculates this value as `distanceGain = (1 – rolloffFactor * (distance – referenceDistance) / (maximumDistance – referenceDistance))`.

## See Also

- [AVAudioEnvironmentDistanceAttenuationModel.exponential](avaudioenvironmentdistanceattenuationmodel/exponential.md)
  An exponential model that describes the drop-off in gain as the source moves away from the listener.
- [AVAudioEnvironmentDistanceAttenuationModel.inverse](avaudioenvironmentdistanceattenuationmodel/inverse.md)
  An inverse model that describes the drop-off in gain as the source moves away from the listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentdistanceattenuationmodel/linear)*