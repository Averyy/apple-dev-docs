# computePath(to:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously requests a pathfind from the owning entity’s position to the target position and waits for the path or a failure. If the function returns an empty path, the pathfind succeeded with no nodes (for example, the start and end positions are in the same place). If the function returns nil, the pathfinding failed to find a path.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func computePath(to targetPosition: SIMD3<Float>) async -> [NavigationMeshResource.PathNode]?
```

## See Also

- [func computePath(from: SIMD3<Float>, to: SIMD3<Float>) async -> [NavigationMeshResource.PathNode]?](navigationcontroller/computepath(from:to:).md)
  Asynchronously requests a pathfind from a given position to the target position and waits for the path or a failure. If the function returns an empty path, the pathfind succeeded with no nodes (for example, the start and end positions are in the same place). If the function returns nil, the pathfinding failed to find a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationcontroller/computepath(to:))*