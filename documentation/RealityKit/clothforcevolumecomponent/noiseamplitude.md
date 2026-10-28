# noiseAmplitude

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The amplitude of the noise applied to particles inside the volume.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var noiseAmplitude: Float { get set }
```

## Discussion

Must be non-negative; negative values are clamped to zero.

## See Also

### Adding force noise
- [var noiseFrequency: Float](./noisefrequency.md)
  The frequency of the noise applied to particles inside the volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothforcevolumecomponent/noiseamplitude)*