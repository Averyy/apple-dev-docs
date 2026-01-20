# init(shape:)

**Framework**: RealityKit  
**Kind**: init

Generates a MeshResource from a ShapeResource.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(shape resource: ShapeResource)
```

## Parameters

- `resource`: The ShapeResource which will be used for generating the mesh.

## See Also

- [static func generate(from: MeshResource.Contents) throws -> MeshResource](meshresource/generate(from:)-4aahn.md)
  Create a mesh resource from contents.
- [static func generate(from: MeshResource.Contents) throws -> MeshResource](meshresource/generate(from:)-4aahn.md)
  Create a mesh resource from contents.
- [convenience init(from: LowLevelMesh) async throws](meshresource/init(from:)-1i7c9.md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [convenience init(from: LowLevelMesh) async throws](meshresource/init(from:)-1i7c9.md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [static func generateAsync(from: MeshResource.Contents) -> LoadRequest<MeshResource>](meshresource/generateasync(from:)-1n2vv.md)
  Create a mesh resource from contents asynchronously.
- [static func generateAsync(from: MeshResource.Contents) -> LoadRequest<MeshResource>](meshresource/generateasync(from:)-1n2vv.md)
  Create a mesh resource from contents asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/init(shape:)-3rtda)*