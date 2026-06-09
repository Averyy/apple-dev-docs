# cullMeshInstances(_:indices:outIndices:configuration:)

**Framework**: RealityKit  
**Kind**: method

Culls mesh instances against a frustum, writing surviving indices to an output span.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func cullMeshInstances(_ meshInstances: LowLevelMeshInstanceArray, indices: Span<Int>, outIndices: inout OutputSpan<Int>, configuration: LowLevelRenderer.CullConfiguration)
```

#### Discussion

Tests each instance’s bounds against the planes in `configuration.frustum`, using `meshInstance.bounds` when set and falling back to the mesh part’s bounds otherwise. Instances whose bounds lie entirely outside any single plane are discarded; the rest are appended to `outIndices` in the same order as `indices`. `nil` slots in `meshInstances` are skipped.

## Parameters

- `meshInstances`: The mesh instance array to test.
- `indices`: The candidate indices to test.
- `outIndices`: The span that receives surviving indices. Must have free capacity of at least `indices.count`.
- `configuration`: The cull configuration supplying the frustum planes.

## See Also

- [static func cullMeshInstances(LowLevelMeshInstanceArray, indices: Span<Int>, configuration: LowLevelRenderer.CullConfiguration) -> [Int]](lowlevelrenderer/cullmeshinstances(_:indices:configuration:).md)
  Culls mesh instances against a frustum and returns the surviving indices.
- [LowLevelRenderer.CullConfiguration](lowlevelrenderer/cullconfiguration.md)
  The parameters for a frustum culling operation.
- [static func sortMeshInstances(LowLevelMeshInstanceArray, indices: inout MutableSpan<Int>, configuration: LowLevelRenderer.SortConfiguration)](lowlevelrenderer/sortmeshinstances(_:indices:configuration:).md)
  Sorts the given mesh instances by sort category and, for transparent instances, by back-to-front distance from the camera.
- [LowLevelRenderer.SortConfiguration](lowlevelrenderer/sortconfiguration.md)
  The parameters for a mesh instance sort pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/cullmeshinstances(_:indices:outindices:configuration:))*