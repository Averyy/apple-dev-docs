# mesh

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The (simulation) mesh of the cloth body that defines the rest pose of the body.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var mesh: ClothMeshResource { get }
```

#### Discussion

This acts as the initial pose of the body when [`initialMeshDraping`](./initialmeshdraping.md) is `nil`.

The different stiffnesses of the assigned material determine in which ways and how firmly the body tries to preserve this rest pose. You can use [`resetDeformation(entity:)`](./resetdeformation%28entity%29.md) to restore the body back to this rest pose at any time.

The topology of the mesh can influence the simulation behavior.

## See Also

### Creating a cloth body
- [init(mesh: ClothMeshResource, meshDraping: ClothPoseResource?)](./init%28mesh,meshdraping%29.md)
  Creates a new cloth body component.
- [var initialMeshDraping: ClothPoseResource?](./initialmeshdraping.md)
  An optional pose that specifies an already draped configuration of the cloth at the start of the simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/mesh)*