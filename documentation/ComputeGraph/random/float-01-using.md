# random::float_01_using

**Framework**: ComputeGraph  
**Kind**: func

Generates a pseudo-random single-precision float between 0 and 1 using a specific seed.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
float random::float_01_using(uint seed)
```

#### Return Value

A pseudo-random single-precision float in the range [0.0, 1.0].

#### Discussion

This function generates a random value in the range [0.0, 1.0] using single-precision floating-point format and the provided seed. The seed is not modified, allowing for reproducible random number generation.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/b21b827f570ccdf02cce761fed453015/random__float_01_using.svg)

## Parameters

- `seed`: The seed value to use for random number generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random/float_01_using)*