# random::half2_01_using

**Framework**: Compute Graph  
**Kind**: func

Generates a pseudo-random 2D vector with half-precision components between 0 and 1 using a specific seed.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
half2 random::half2_01_using(uint seed)
```

#### Return Value

A pseudo-random 2D half-precision vector with components in the range [0.0, 1.0].

#### Discussion

This function generates a random 2D vector where each component is independently generated in the range [0.0, 1.0] using half-precision floating-point format and sequential seed values (seed, seed+1). The seed is not modified, allowing for reproducible random number generation.

> **Note**: ![Graph](/images/com.apple.computegraph/random__half2_01_using.svg)

## Parameters

- `seed`: The base seed value to use for random number generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random/half2_01_using)*