# generateAsync(from:)

**Framework**: RealityKit  
**Kind**: method

Create a mesh resource from a list of mesh descriptors asynchronously.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func generateAsync(from descriptors: [MeshDescriptor]) -> LoadRequest<MeshResource>
```

## See Also

- [static func generate(from: MeshResource.Contents) throws -> MeshResource](meshresource/generate(from:)-30q3o.md)
  Create a mesh resource from contents.
- [static func generate(from: [MeshDescriptor]) throws -> MeshResource](meshresource/generate(from:)-6l1q2.md)
  Create a mesh resource from a list of mesh descriptors.
- [convenience init(from: [MeshDescriptor]) async throws](meshresource/init(from:)-b7hb.md)
  Initialize a mesh resource from descriptors asynchronously.
- [convenience init(from: MeshResource.Contents) async throws](meshresource/init(from:)-869q3.md)
  Initialize a mesh resource from contents asynchronously.
- [convenience init(shape: ShapeResource) async](meshresource/init(shape:)-9fxu3.md)
  Generates a MeshResource from a ShapeResource.
- [convenience init(shape: ShapeResource)](meshresource/init(shape:)-9yvj0.md)
  Generates a MeshResource from a ShapeResource.
- [static func generateAsync(from: MeshResource.Contents) -> LoadRequest<MeshResource>](meshresource/generateasync(from:)-5z7ky.md)
  Create a mesh resource from contents asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generateasync(from:)-9ify3)*