# graph::localToWorld

**Framework**: Compute Graph  
**Kind**: func  
**Role**: Function

Returns the transformation matrix from local space to world space.

**Availability**:
- macOS
- Reality Composer Pro

## Declaration

```swift
float4x4 graph::localToWorld()
```

## Return Value

A 4x4 transformation matrix for local-to-world conversion.

## Discussion

This matrix transforms coordinates from the graph’s local coordinate system to the scene’s coordinate system, incorporating all parent transformations.

> **Visual**: ![Graph](https://developer.apple.com/tutorials/images/com.apple.computegraph/graph__localToWorld.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/graph/localtoworld)*