# initialMeshDraping

**Framework**: RealityKit  
**Kind**: property

An optional pose that specifies an already draped configuration of the cloth at the start of the simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var initialMeshDraping: ClothPoseResource? { get }
```

#### Discussion

This configuration is applied when the body is created or reset, providing the cloth with an initial settled state. In contrast, the rest pose defined by [`mesh`](clothbodycomponent/mesh.md) represents the reference shape that the cloth attempts to preserve during deformation.

The number and ordering of positions in this pose resource must match those of the [`mesh`](clothbodycomponent/mesh.md).

## See Also

- [init(mesh: ClothMeshResource, meshDraping: ClothPoseResource?)](clothbodycomponent/init(mesh:meshdraping:).md)
  Creates a new cloth body component.
- [var mesh: ClothMeshResource](clothbodycomponent/mesh.md)
  The (simulation) mesh of the cloth body that defines the rest pose of the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/initialmeshdraping)*