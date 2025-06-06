# AVAudioEnvironmentDistanceAttenuationModel.exponential

**Framework**: AVFAudio  
**Kind**: case

An exponential model that describes the drop-off in gain as the source moves away from the listener.

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
case exponential
```

#### Discussion

The framework calculates this value as `distanceGain = (distance / referenceDistance) ^ (-rolloffFactor)`.

## See Also

- [AVAudioEnvironmentDistanceAttenuationModel.inverse](avaudioenvironmentdistanceattenuationmodel/inverse.md)
  An inverse model that describes the drop-off in gain as the source moves away from the listener.
- [AVAudioEnvironmentDistanceAttenuationModel.linear](avaudioenvironmentdistanceattenuationmodel/linear.md)
  A linear model that describes the drop-off in gain as the source moves away from the listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentdistanceattenuationmodel/exponential)*