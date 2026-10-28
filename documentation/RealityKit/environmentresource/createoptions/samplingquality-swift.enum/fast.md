# EnvironmentResource.CreateOptions.SamplingQuality.fast

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

Computes the environment textures with small sampling rates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
case fast
```

## Discussion

Low sampling rates can result in higher noise in high-frequency areas and banding in low-frequency gradients.

## See Also

### Sampling qualities
- [EnvironmentResource.CreateOptions.SamplingQuality.normal](./normal.md)
  Computes the environment textures with regular sampling rates.
- [EnvironmentResource.CreateOptions.SamplingQuality.high](./high.md)
  Computes the environment textures with high sampling rates, reducing texture noise in high-frequency areas.
- [EnvironmentResource.CreateOptions.SamplingQuality.veryHigh](./veryhigh.md)
  Computes the environment textures with very high sampling rates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/createoptions/samplingquality-swift.enum/fast)*