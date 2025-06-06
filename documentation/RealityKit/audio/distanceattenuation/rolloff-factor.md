# Audio.DistanceAttenuation.rolloff(factor:)

**Framework**: RealityKit  
**Kind**: case

A standard geometric model for attenuating audio intensity naturally with distance, using a specified loss strength factor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
case rolloff(factor: Double)
```

#### Discussion

The case’s default value is `1.0`, which attenuates spatial audio as the listener moves away from the source, similar to real-world physics. You can increase or decrease this effect by changing `factor` to other values. For example:

- `0.5` reduces the effect by 50%
- `2.0` doubles the effect
- `0.0` completely disables attenuation

## Parameters

- `factor`: The attenuation model’s loss strength factor in the range of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/distanceattenuation/rolloff(factor:))*