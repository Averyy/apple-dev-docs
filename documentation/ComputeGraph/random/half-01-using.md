# random::half_01_using

**Framework**: ComputeGraph  
**Kind**: func

Generates a pseudo-random half-precision float between 0 and 1 using a specific seed.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
half random::half_01_using(uint seed)
```

#### Return Value

A pseudo-random half-precision float in the range [0.0, 1.0].

#### Discussion

This function generates a random value in the range [0.0, 1.0] using half-precision floating-point format and the provided seed. The seed is not modified, allowing for reproducible random number generation.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/a82de8bdc1fa7c149fc2e5c52aa53d5d/random__half_01_using.svg)

## Parameters

- `seed`: The seed value to use for random number generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random/half_01_using)*