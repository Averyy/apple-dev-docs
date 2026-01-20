# generateAsync(from:)

**Framework**: RealityKit  
**Kind**: method

Create a mesh resource from contents asynchronously.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func generateAsync(from content: MeshResource.Contents) -> LoadRequest<MeshResource>
```

## See Also

- [static func generate(from: MeshResource.Contents) throws -> MeshResource](meshresource/generate(from:)-4aahn.md)
  Create a mesh resource from contents.
- [static func generate(from: MeshResource.Contents) throws -> MeshResource](meshresource/generate(from:)-4aahn.md)
  Create a mesh resource from contents.
- [convenience init(from: LowLevelMesh) async throws](meshresource/init(from:)-1i7c9.md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [convenience init(from: LowLevelMesh) async throws](meshresource/init(from:)-1i7c9.md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [convenience init(shape: ShapeResource)](meshresource/init(shape:)-3rtda.md)
  Generates a MeshResource from a ShapeResource.
- [convenience init(shape: ShapeResource)](meshresource/init(shape:)-3rtda.md)
  Generates a MeshResource from a ShapeResource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generateasync(from:)-1n2vv)*