# scaled(by:)

**Framework**: RealityKit  
**Kind**: method

Scale the scattering data by a frequency-dependent scalar value between -1 and 1.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func scaled(by frequencyDependentScalar: (Float) -> Float) -> Audio.Scattering
```

#### Discussion

- No adjustment is made to the coefficient when the scalar is 0.
- The coefficient is set to 0 when the scalar is -1.
- The coefficient is set to 1 when the scalar is +1.
- If the scalar value is between -1 and 0, the coefficient is adjusted by the percentage defined by the absolute value of the scalar between the original coefficient and 0.
- If the scalar value is between 0 and 1, the coefficient is adjusted by the percentage defined by the scalar between the original coefficient and 1.

## Parameters

- `frequencyDependentScalar`: A function with frequency as input and coefficient scalar as output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/scattering/scaled(by:))*