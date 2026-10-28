# init(from:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Initialize a mesh resource from contents asynchronously.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
nonisolated
convenience init(from content: MeshResource.Contents) async throws
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
@MainActor
convenience init(from mesh: ClothMeshResource) async
```

```swift
nonisolated
convenience init(from descriptors: [MeshDescriptor]) async throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/init(from:)-7ld56)*