# init(from:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously creates a mesh resource from a low-level mesh.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(from mesh: LowLevelMesh) async throws
```

## Parameters

- `mesh`: The vertex data that defines the mesh.

## See Also

- [convenience init(from: LowLevelMesh) throws](meshresource/init(from:)-9kv7c.md)
  Synchronously creates a mesh resource from a low-level mesh.
- [var lowLevelMesh: LowLevelMesh?](meshresource/lowlevelmesh.md)
  The low-level mesh that this mesh is built from, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/init(from:)-1ehyt)*