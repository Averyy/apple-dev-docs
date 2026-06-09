# graph::worldToLocal

**Framework**: ComputeGraph  
**Kind**: func

Returns the transformation matrix from world space to local space.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
float4x4 graph::worldToLocal()
```

#### Return Value

A 4x4 transformation matrix for world-to-local conversion.

#### Discussion

This matrix transforms coordinates from the scene’s coordinate system to the graph’s local coordinate system. It is the inverse of the local-to-world matrix.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/37540301ac64f35060a951ace32818e4/graph__worldToLocal.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/graph/worldtolocal)*