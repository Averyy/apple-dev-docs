# random::float2_01

**Framework**: Compute Graph  
**Kind**: func

Generates a pseudo-random 2D vector with single-precision components between 0 and 1.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
float2 random::float2_01()
```

#### Return Value

A pseudo-random 2D single-precision vector with components in the range [0.0, 1.0].

#### Discussion

This function generates a random 2D vector where each component is independently generated in the range [0.0, 1.0] using single-precision floating-point format. The internal random seed is incremented for subsequent calls.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/fa3d8292555b631f73aa738318517806/random__float2_01.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random/float2_01)*