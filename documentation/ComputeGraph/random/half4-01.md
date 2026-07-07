# random::half4_01

**Framework**: Compute Graph  
**Kind**: func

Generates a pseudo-random 4D vector with half-precision components between 0 and 1.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
half4 random::half4_01()
```

#### Return Value

A pseudo-random 4D half-precision vector with components in the range [0.0, 1.0].

#### Discussion

This function generates a random 4D vector where each component is independently generated in the range [0.0, 1.0] using half-precision floating-point format. The internal random seed is incremented for subsequent calls.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/26009181e8647f29deefce6cce3a4852/random__half4_01.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random/half4_01)*