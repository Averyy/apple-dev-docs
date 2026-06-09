# random::float3_01_using

**Framework**: ComputeGraph  
**Kind**: func

Generates a pseudo-random 3D vector with single-precision components between 0 and 1 using a specific seed.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
float3 random::float3_01_using(uint seed)
```

#### Return Value

A pseudo-random 3D single-precision vector with components in the range [0.0, 1.0].

#### Discussion

This function generates a random 3D vector where each component is independently generated in the range [0.0, 1.0] using single-precision floating-point format and sequential seed values (seed, seed+1, seed+2). The seed is not modified, allowing for reproducible random number generation.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/fe9c924ca5b6e6f5dd90149982762acc/random__float3_01_using.svg)

## Parameters

- `seed`: The base seed value to use for random number generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random/float3_01_using)*