# indexCount

**Framework**: RealityKit  
**Kind**: property

The number of indices in the mesh.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var indexCount: Int { get }
```

#### Discussion

This count will be equal to the number of primitives in the mesh multiplied by the number of vertices per primitive. For example, a triangular mesh with nine triangles has an index count of 9 ⨉ 3 = 27 indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshresource/indexcount)*