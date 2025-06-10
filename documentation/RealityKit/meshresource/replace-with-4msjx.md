# replace(with:)

**Framework**: RealityKit  
**Kind**: method

Replace the contents of this mesh resource.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func replace(with content: MeshResource.Contents) throws
```

#### Discussion

> **Note**: The contents of the modified mesh resource will not be synced between network clients.

## See Also

- [var expectedMaterialCount: Int](meshresource/expectedmaterialcount.md)
  The number of material entries required to render the mesh resource.
- [func replace(with: MeshResource.Contents) async throws](meshresource/replace(with:)-8uvri.md)
  Replace the contents of this mesh resource asynchronously.
- [func replaceAsync(with:)](meshresource/replaceasync(with:).md)
  Replace the contents of this mesh resource asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/replace(with:)-4msjx)*