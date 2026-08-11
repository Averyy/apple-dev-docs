# scalingAbsorption(by:)

**Framework**: RealityKit  
**Kind**: method

Scale the absorption data by a frequency-dependent scalar value between -1 and 1.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func scalingAbsorption(by frequencyDependentScalar: (Float) -> Float) -> Audio.Material
```

#### Return Value

Audio material with absorption data scaled by the frequency-dependent scaling function.

#### Discussion

- No adjustment is made to the coefficient when the scalar is 0.
- The coefficient is set to 0 when the scalar is -1.
- The coefficient is set to 1 when the scalar is +1.
- If the scalar value is between -1 and 0, the coefficient is adjusted by the percentage defined by the absolute value of the scalar between the original coefficient and 0.
- If the scalar value is between 0 and 1, the coefficient is adjusted by the percentage defined by the scalar between the original coefficient and 1.

Example usage:

```None
// Make a generic carpet material more absorptive by making it thicker.
// Below 1000Hz, the absorption remains the same. Above 1000Hz, the absorption is increased.
let thickCarpet: Audio.Material = .carpet.scalingAbsorption { frequency in
    frequency > 1000 ? 0.5 : .zero
}
```

## Parameters

- `frequencyDependentScalar`: A function with frequency as input and coefficient scalar as output.

## See Also

- [func scalingScattering(by: (Float) -> Float) -> Audio.Material](audio/material/scalingscattering(by:).md)
  Scale the scattering data by a frequency-dependent scalar value between -1 and 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/material/scalingabsorption(by:))*