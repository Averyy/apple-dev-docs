# replace(with:)

**Framework**: RealityKit  
**Kind**: method

Replace the contents of this mesh resource asynchronously.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
nonisolated
func replace(with content: MeshResource.Contents) async throws
```

#### Discussion

> **Note**: The contents of the modified mesh resource will not be synced between network clients.

## See Also

- [var expectedMaterialCount: Int](meshresource/expectedmaterialcount.md)
  The number of material entries required to render the mesh resource.
- [func replace(with: MeshResource.Contents) throws](meshresource/replace(with:)-4msjx.md)
  Replace the contents of this mesh resource.
- [func replaceAsync(with:)](meshresource/replaceasync(with:).md)
  Replace the contents of this mesh resource asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/replace(with:)-8uvri)*