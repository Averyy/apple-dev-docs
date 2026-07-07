# init(from:)

**Framework**: RealityKit  
**Kind**: init

Creates a cloth mesh resource from a rendering mesh resource.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
convenience init(from mesh: MeshResource) throws
```

#### Discussion

Generates a cloth mesh from a rendering mesh without remeshing. No remeshing is performed. In other words, the resulting [`ClothMeshResource`](clothmeshresource.md) will match exactly the original [`MeshResource`](meshresource.md).

- from: The [`MeshResource`](meshresource.md) to generate a [`ClothMeshResource`](clothmeshresource.md) from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshresource/init(from:))*