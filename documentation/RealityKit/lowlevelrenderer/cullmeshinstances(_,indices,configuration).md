# cullMeshInstances(_:indices:configuration:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Culls mesh instances against a frustum and returns the surviving indices.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func cullMeshInstances(_ meshInstances: LowLevelMeshInstanceArray, indices: Span<Int>, configuration: LowLevelRenderer.CullConfiguration) -> [Int]
```

#### Return Value

The indices of instances that are not culled, in input order.

#### Discussion

A convenience overload that allocates and returns the surviving indices as an array.

## Parameters

- `meshInstances`: The mesh instance array to test.
- `indices`: The candidate indices to test.
- `configuration`: The cull configuration supplying the frustum planes.

## See Also

### Culling and sorting instances
- [static func cullMeshInstances(LowLevelMeshInstanceArray, indices: Span<Int>, outIndices: inout OutputSpan<Int>, configuration: LowLevelRenderer.CullConfiguration)](./cullmeshinstances%28_,indices,outindices,configuration%29.md)
  Culls mesh instances against a frustum, writing surviving indices to an output span.
- [LowLevelRenderer.CullConfiguration](./cullconfiguration.md)
  The configuration for a frustum culling operation.
- [static func sortMeshInstances(LowLevelMeshInstanceArray, indices: inout MutableSpan<Int>, configuration: LowLevelRenderer.SortConfiguration)](./sortmeshinstances%28_,indices,configuration%29.md)
  Sorts the given mesh instances by sort category and, for transparent instances, by back-to-front distance from the camera.
- [LowLevelRenderer.SortConfiguration](./sortconfiguration.md)
  The configuration for a mesh instance sort pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/cullmeshinstances(_:indices:configuration:))*