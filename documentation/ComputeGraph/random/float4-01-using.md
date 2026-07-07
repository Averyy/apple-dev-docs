# random::float4_01_using

**Framework**: Compute Graph  
**Kind**: func

Generates a pseudo-random 4D vector with single-precision components between 0 and 1 using a specific seed.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
float4 random::float4_01_using(uint seed)
```

#### Return Value

A pseudo-random 4D single-precision vector with components in the range [0.0, 1.0].

#### Discussion

This function generates a random 4D vector where each component is independently generated in the range [0.0, 1.0] using single-precision floating-point format and sequential seed values (seed, seed+1, seed+2, seed+3). The seed is not modified, allowing for reproducible random number generation.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/fb94c182753143b313b74cf116992461/random__float4_01_using.svg)

## Parameters

- `seed`: The base seed value to use for random number generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random/float4_01_using)*