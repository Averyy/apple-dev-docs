# random::half2_01

**Framework**: Compute Graph  
**Kind**: func

Generates a pseudo-random 2D vector with half-precision components between 0 and 1.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
half2 random::half2_01()
```

#### Return Value

A pseudo-random 2D half-precision vector with components in the range [0.0, 1.0].

#### Discussion

This function generates a random 2D vector where each component is independently generated in the range [0.0, 1.0] using half-precision floating-point format. The internal random seed is incremented for subsequent calls.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/727f3c727e69e7392769e6c0554a193f/random__half2_01.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random/half2_01)*