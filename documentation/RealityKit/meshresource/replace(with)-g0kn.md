# replace(with:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Replace the contents of this mesh resource.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func replace(with content: MeshResource.Contents) throws
```

**Other overloads**:

```swift
nonisolated
func replace(with content: MeshResource.Contents) async throws
```

## Discussion

> **Note**: The contents of the modified mesh resource will not be synced between network clients.

## See Also

### Configuring the resource
- [var expectedMaterialCount: Int](./expectedmaterialcount.md)
  The number of material entries required to render the mesh resource.
- [func replaceAsync(with: MeshResource.Contents) -> LoadRequest<MeshResource>](./replaceasync%28with%29.md)
  Replace the contents of this mesh resource asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/replace(with:)-g0kn)*