# random::float4_01

**Framework**: Compute Graph  
**Kind**: func

Generates a pseudo-random 4D vector with single-precision components between 0 and 1.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
float4 random::float4_01()
```

#### Return Value

A pseudo-random 4D single-precision vector with components in the range [0.0, 1.0].

#### Discussion

This function generates a random 4D vector where each component is independently generated in the range [0.0, 1.0] using single-precision floating-point format. The internal random seed is incremented for subsequent calls.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/9207b28bf6c8660e5c72a242b0e55ea4/random__float4_01.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random/float4_01)*