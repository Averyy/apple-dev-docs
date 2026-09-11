# init(from:)

**Framework**: RealityKit  
**Kind**: init

Creates a reverb mesh resource from a mesh resource.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
convenience init(from mesh: MeshResource) throws
```

#### Discussion

Use this initializer to convert visual or physics geometry you already have into acoustic geometry, without duplicating the data:

```swift
let reverbMesh = try ReverbMeshResource(from: myVisualMesh)
```

## Parameters

- `mesh`: The mesh resource to convert into a reverb mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/reverbmeshresource/init(from:))*