# init(from:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a MeshResource from the provided MeshAnchor.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(from meshAnchor: MeshAnchor) async throws
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
@preconcurrency convenience init(from planeAnchor: PlaneAnchor) async throws
```

```swift
@MainActor
convenience init(from mesh: ClothMeshResource)
```

```swift
@MainActor
convenience init(from mesh: ClothMeshResource) async
```

```swift
nonisolated
convenience init(from content: MeshResource.Contents) async throws
```

```swift
nonisolated
convenience init(from descriptors: [MeshDescriptor]) async throws
```

## Parameters

- `meshAnchor`: A MeshAnchor that will be used to generate the MeshResource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/init(from:)-7wc9b)*