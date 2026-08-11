# sortMeshInstances(_:indices:configuration:)

**Framework**: RealityKit  
**Kind**: method

Sorts the given mesh instances by sort category and, for transparent instances, by back-to-front distance from the camera.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func sortMeshInstances(_ meshInstances: LowLevelMeshInstanceArray, indices: inout MutableSpan<Int>, configuration: LowLevelRenderer.SortConfiguration)
```

#### Discussion

Call this before `render(using:_:)` to produce a draw order for the callback. Opaque instances sort before transparent ones; within transparent instances, farther instances sort before nearer ones.

## Parameters

- `meshInstances`: The mesh instance array whose elements to sort.
- `indices`: The index span to sort in place.
- `configuration`: The sort configuration supplying the camera position.

## See Also

- [static func cullMeshInstances(LowLevelMeshInstanceArray, indices: Span<Int>, outIndices: inout OutputSpan<Int>, configuration: LowLevelRenderer.CullConfiguration)](lowlevelrenderer/cullmeshinstances(_:indices:outindices:configuration:).md)
  Culls mesh instances against a frustum, writing surviving indices to an output span.
- [static func cullMeshInstances(LowLevelMeshInstanceArray, indices: Span<Int>, configuration: LowLevelRenderer.CullConfiguration) -> [Int]](lowlevelrenderer/cullmeshinstances(_:indices:configuration:).md)
  Culls mesh instances against a frustum and returns the surviving indices.
- [LowLevelRenderer.CullConfiguration](lowlevelrenderer/cullconfiguration.md)
  The configuration for a frustum culling operation.
- [LowLevelRenderer.SortConfiguration](lowlevelrenderer/sortconfiguration.md)
  The configuration for a mesh instance sort pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/sortmeshinstances(_:indices:configuration:))*