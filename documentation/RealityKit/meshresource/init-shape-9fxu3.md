# init(shape:)

**Framework**: RealityKit  
**Kind**: init

Generates a MeshResource from a ShapeResource.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(shape resource: ShapeResource) async
```

## Parameters

- `resource`: The ShapeResource which will be used for generating the mesh.

## See Also

- [static func generate(from: MeshResource.Contents) throws -> MeshResource](meshresource/generate(from:)-30q3o.md)
  Create a mesh resource from contents.
- [static func generate(from: [MeshDescriptor]) throws -> MeshResource](meshresource/generate(from:)-6l1q2.md)
  Create a mesh resource from a list of mesh descriptors.
- [convenience init(from: [MeshDescriptor]) async throws](meshresource/init(from:)-b7hb.md)
  Initialize a mesh resource from descriptors asynchronously.
- [convenience init(from: MeshResource.Contents) async throws](meshresource/init(from:)-869q3.md)
  Initialize a mesh resource from contents asynchronously.
- [convenience init(shape: ShapeResource)](meshresource/init(shape:)-9yvj0.md)
  Generates a MeshResource from a ShapeResource.
- [static func generateAsync(from: MeshResource.Contents) -> LoadRequest<MeshResource>](meshresource/generateasync(from:)-5z7ky.md)
  Create a mesh resource from contents asynchronously.
- [static func generateAsync(from: [MeshDescriptor]) -> LoadRequest<MeshResource>](meshresource/generateasync(from:)-9ify3.md)
  Create a mesh resource from a list of mesh descriptors asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/init(shape:)-9fxu3)*