# replaceAsync(with:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Replace the contents of this mesh resource asynchronously.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0 (renamed: replace(with:))
- iPadOS 15.0+ - Deprecated in 18.0 (renamed: replace(with:))
- Mac Catalyst 15.0+ - Deprecated in 18.0 (renamed: replace(with:))
- macOS 12.0+ - Deprecated in 15.0 (renamed: replace(with:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: replace(with:))

## Declaration

```swift
@MainActor
@preconcurrency func replaceAsync(with content: MeshResource.Contents) -> LoadRequest<MeshResource>
```

#### Discussion

> **Note**: The contents of the modified mesh resource will not be synced between network clients.

## See Also

### Configuring the resource
- [var expectedMaterialCount: Int](./expectedmaterialcount.md)
  The number of material entries required to render the mesh resource.
- [func replace(with: MeshResource.Contents) throws](./replace%28with%29-g0kn.md)
  Replace the contents of this mesh resource.
- [func replace(with: MeshResource.Contents) throws](./replace%28with%29-g0kn.md)
  Replace the contents of this mesh resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/replaceasync(with:))*