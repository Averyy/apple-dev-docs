# lowLevelMesh

**Framework**: RealityKit  
**Kind**: property

The low-level mesh that this mesh is built from, if any.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency var lowLevelMesh: LowLevelMesh? { get }
```

#### Discussion

If this mesh is not built from a [`LowLevelMesh`](lowlevelmesh.md), it returns nil.

## See Also

- [convenience init(from: LowLevelMesh) async throws](meshresource/init(from:)-1ehyt.md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [convenience init(from: LowLevelMesh) throws](meshresource/init(from:)-9kv7c.md)
  Synchronously creates a mesh resource from a low-level mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/lowlevelmesh)*