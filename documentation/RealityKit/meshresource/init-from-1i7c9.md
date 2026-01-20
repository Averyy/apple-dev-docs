# init(from:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously creates a mesh resource from a low-level mesh.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(from mesh: LowLevelMesh) async throws
```

## Parameters

- `mesh`: The vertex data that defines the mesh.

## See Also

- [static func generate(from: MeshResource.Contents) throws -> MeshResource](meshresource/generate(from:)-4aahn.md)
  Create a mesh resource from contents.
- [static func generate(from: MeshResource.Contents) throws -> MeshResource](meshresource/generate(from:)-4aahn.md)
  Create a mesh resource from contents.
- [convenience init(shape: ShapeResource)](meshresource/init(shape:)-3rtda.md)
  Generates a MeshResource from a ShapeResource.
- [convenience init(shape: ShapeResource)](meshresource/init(shape:)-3rtda.md)
  Generates a MeshResource from a ShapeResource.
- [static func generateAsync(from: MeshResource.Contents) -> LoadRequest<MeshResource>](meshresource/generateasync(from:)-1n2vv.md)
  Create a mesh resource from contents asynchronously.
- [static func generateAsync(from: MeshResource.Contents) -> LoadRequest<MeshResource>](meshresource/generateasync(from:)-1n2vv.md)
  Create a mesh resource from contents asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/init(from:)-1i7c9)*