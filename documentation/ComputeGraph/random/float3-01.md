# random::float3_01

**Framework**: Compute Graph  
**Kind**: func

Generates a pseudo-random 3D vector with single-precision components between 0 and 1.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
float3 random::float3_01()
```

#### Return Value

A pseudo-random 3D single-precision vector with components in the range [0.0, 1.0].

#### Discussion

This function generates a random 3D vector where each component is independently generated in the range [0.0, 1.0] using single-precision floating-point format. The internal random seed is incremented for subsequent calls.

> **Note**: ![Graph](/images/com.apple.computegraph/random__float3_01.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random/float3_01)*