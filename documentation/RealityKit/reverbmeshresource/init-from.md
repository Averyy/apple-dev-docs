# init(from:)

**Framework**: RealityKit  
**Kind**: init

Creates a reverb mesh resource from a mesh resource.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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