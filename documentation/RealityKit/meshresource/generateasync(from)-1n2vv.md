# generateAsync(from:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Create a mesh resource from contents asynchronously.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0 (renamed: init(from:))
- iPadOS 15.0+ - Deprecated in 18.0 (renamed: init(from:))
- Mac Catalyst 15.0+ - Deprecated in 18.0 (renamed: init(from:))
- macOS 12.0+ - Deprecated in 15.0 (renamed: init(from:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: init(from:))

## Declaration

```swift
@MainActor
@preconcurrency static func generateAsync(from content: MeshResource.Contents) -> LoadRequest<MeshResource>
```

**Other overloads**:

```swift
@MainActor
@preconcurrency static func generateAsync(from descriptors: [MeshDescriptor]) -> LoadRequest<MeshResource>
```

## See Also

### Creating a mesh resource
- [static func generate(from: MeshResource.Contents) throws -> MeshResource](./generate%28from%29-4aahn.md)
  Create a mesh resource from contents.
- [static func generate(from: MeshResource.Contents) throws -> MeshResource](./generate%28from%29-4aahn.md)
  Create a mesh resource from contents.
- [convenience init(from: LowLevelMesh) async throws](./init%28from%29-1i7c9.md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [convenience init(from: LowLevelMesh) async throws](./init%28from%29-1i7c9.md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [convenience init(shape: ShapeResource)](./init%28shape%29-3rtda.md)
  Generates a MeshResource from a ShapeResource.
- [convenience init(shape: ShapeResource)](./init%28shape%29-3rtda.md)
  Generates a MeshResource from a ShapeResource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generateasync(from:)-1n2vv)*