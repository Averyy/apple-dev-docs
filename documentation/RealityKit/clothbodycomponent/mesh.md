# mesh

**Framework**: RealityKit  
**Kind**: property

The (simulation) mesh of the cloth body that defines the rest pose of the body.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var mesh: ClothMeshResource { get }
```

#### Discussion

This acts as the initial pose of the body when [`initialMeshDraping`](clothbodycomponent/initialmeshdraping.md) is `nil`.

The different stiffnesses of the assigned material determine in which ways and how firmly the body tries to preserve this rest pose. You can use [`resetDeformation(entity:)`](clothbodycomponent/resetdeformation(entity:).md) to restore the body back to this rest pose at any time.

The topology of the mesh can influence the simulation behavior.

## See Also

- [init(mesh: ClothMeshResource, meshDraping: ClothPoseResource?)](clothbodycomponent/init(mesh:meshdraping:).md)
  Creates a new cloth body component.
- [var initialMeshDraping: ClothPoseResource?](clothbodycomponent/initialmeshdraping.md)
  An optional pose that specifies an already draped configuration of the cloth at the start of the simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/mesh)*