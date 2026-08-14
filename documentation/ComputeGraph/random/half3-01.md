# random::half3_01

**Framework**: Compute Graph  
**Kind**: func

Generates a pseudo-random 3D vector with half-precision components between 0 and 1.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
half3 random::half3_01()
```

#### Return Value

A pseudo-random 3D half-precision vector with components in the range [0.0, 1.0].

#### Discussion

This function generates a random 3D vector where each component is independently generated in the range [0.0, 1.0] using half-precision floating-point format. The internal random seed is incremented for subsequent calls.

> **Note**: ![Graph](/images/com.apple.computegraph/random__half3_01.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random/half3_01)*