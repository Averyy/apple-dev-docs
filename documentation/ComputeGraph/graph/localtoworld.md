# graph::localToWorld

**Framework**: ComputeGraph  
**Kind**: func

Returns the transformation matrix from local space to world space.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
float4x4 graph::localToWorld()
```

#### Return Value

A 4x4 transformation matrix for local-to-world conversion.

#### Discussion

This matrix transforms coordinates from the graph’s local coordinate system to the scene’s coordinate system, incorporating all parent transformations.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/489118d441497d08dcfb7420d1dd604f/graph__localToWorld.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/graph/localtoworld)*