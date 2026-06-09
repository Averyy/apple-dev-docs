# expectedMaterialCount

**Framework**: RealityKit  
**Kind**: property

The number of material entries required to render the mesh resource.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var expectedMaterialCount: Int { get }
```

#### Discussion

Use this value to determine the number of [`Material`](material.md) instances to provide in the [`materials`](modelcomponent/materials.md) array. When a mesh has multiple submeshes, each submesh references a material by index.

## See Also

- [func replace(with: MeshResource.Contents) throws](meshresource/replace(with:)-g0kn.md)
  Replace the contents of this mesh resource.
- [func replace(with: MeshResource.Contents) throws](meshresource/replace(with:)-g0kn.md)
  Replace the contents of this mesh resource.
- [func replaceAsync(with: MeshResource.Contents) -> LoadRequest<MeshResource>](meshresource/replaceasync(with:).md)
  Replace the contents of this mesh resource asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/expectedmaterialcount)*