# replaceAsync(with:)

**Framework**: Realitykit  
**Kind**: method

Replace the contents of this mesh resource asynchronously.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func replaceAsync(with content: MeshResource.Contents) -> LoadRequest<MeshResource>
```

#### Discussion

> **Note**: The contents of the modified mesh resource will not be synced between network clients.

## See Also

- [var expectedMaterialCount: Int](meshresource/expectedmaterialcount.md)
  The number of material entries required to render the mesh resource.
- [func replace(with: MeshResource.Contents) throws](meshresource/replace(with:)-4msjx.md)
  Replace the contents of this mesh resource.
- [func replace(with: MeshResource.Contents) async throws](meshresource/replace(with:)-8uvri.md)
  Replace the contents of this mesh resource asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/replaceasync(with:))*