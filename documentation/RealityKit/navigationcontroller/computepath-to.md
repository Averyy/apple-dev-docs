# computePath(to:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously requests a pathfind from the owning entity’s position to the target position and waits for the path or a failure. If the function returns an empty path, the pathfind succeeded with no nodes (for example, the start and end positions are in the same place). If the function returns nil, the pathfinding failed to find a path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func computePath(to targetPosition: SIMD3<Float>) async -> [NavigationMeshResource.PathNode]?
```

## See Also

- [func computePath(from: SIMD3<Float>, to: SIMD3<Float>) async -> [NavigationMeshResource.PathNode]?](navigationcontroller/computepath(from:to:).md)
  Asynchronously requests a pathfind from a given position to the target position and waits for the path or a failure. If the function returns an empty path, the pathfind succeeded with no nodes (for example, the start and end positions are in the same place). If the function returns nil, the pathfinding failed to find a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationcontroller/computepath(to:))*