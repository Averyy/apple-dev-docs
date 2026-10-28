# init(from:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Asynchronously creates a mesh resource from a cloth mesh resource.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
convenience init(from mesh: ClothMeshResource) async
```

**Other overloads**:

```swift
@MainActor
@preconcurrency convenience init(from mesh: LowLevelMesh) async throws
```

```swift
@MainActor
@preconcurrency convenience init(from mesh: LowLevelMesh) throws
```

```swift
@MainActor
@preconcurrency convenience init(from meshAnchor: MeshAnchor) async throws
```

```swift
@MainActor
@preconcurrency convenience init(from planeAnchor: PlaneAnchor) async throws
```

```swift
@MainActor
convenience init(from mesh: ClothMeshResource)
```

```swift
nonisolated
convenience init(from content: MeshResource.Contents) async throws
```

```swift
nonisolated
convenience init(from descriptors: [MeshDescriptor]) async throws
```

## Discussion

This can be useful if you want to create a visual mesh from the simulation mesh.

## Parameters

- `mesh`: The cloth simulation mesh to create the mesh resource from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/init(from:)-1abra)*