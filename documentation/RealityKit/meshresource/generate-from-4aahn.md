# generate(from:)

**Framework**: RealityKit  
**Kind**: method

Create a mesh resource from contents.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func generate(from content: MeshResource.Contents) throws -> MeshResource
```

## See Also

- [convenience init(from: LowLevelMesh) async throws](meshresource/init(from:)-1i7c9.md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [convenience init(from: LowLevelMesh) async throws](meshresource/init(from:)-1i7c9.md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [convenience init(shape: ShapeResource)](meshresource/init(shape:)-3rtda.md)
  Generates a MeshResource from a ShapeResource.
- [convenience init(shape: ShapeResource)](meshresource/init(shape:)-3rtda.md)
  Generates a MeshResource from a ShapeResource.
- [static func generateAsync(from: MeshResource.Contents) -> LoadRequest<MeshResource>](meshresource/generateasync(from:)-1n2vv.md)
  Create a mesh resource from contents asynchronously.
- [static func generateAsync(from: MeshResource.Contents) -> LoadRequest<MeshResource>](meshresource/generateasync(from:)-1n2vv.md)
  Create a mesh resource from contents asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generate(from:)-4aahn)*