# random::half3_01_using

**Framework**: ComputeGraph  
**Kind**: func

Generates a pseudo-random 3D vector with half-precision components between 0 and 1 using a specific seed.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
half3 random::half3_01_using(uint seed)
```

#### Return Value

A pseudo-random 3D half-precision vector with components in the range [0.0, 1.0].

#### Discussion

This function generates a random 3D vector where each component is independently generated in the range [0.0, 1.0] using half-precision floating-point format and sequential seed values (seed, seed+1, seed+2). The seed is not modified, allowing for reproducible random number generation.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/cfe5fe00f07a2e48f8d3e0a81c383765/random__half3_01_using.svg)

## Parameters

- `seed`: The base seed value to use for random number generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random/half3_01_using)*