# MeshAnchor

**Framework**: ARKit  
**Kind**: struct

A volume of space that contains a mesh of a person’s surroundings.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct MeshAnchor
```

## Topics

### Getting mesh information
- [var originFromAnchorTransform: simd_float4x4](meshanchor/originfromanchortransform.md)
  The location and orientation of a mesh in world space.
- [var geometry: MeshAnchor.Geometry](meshanchor/geometry-swift.property.md)
  The shape of a mesh anchor.
- [MeshAnchor.Geometry](meshanchor/geometry-swift.struct.md)
  The shapes that make up a mesh anchor.
- [MeshAnchor.MeshClassification](meshanchor/meshclassification.md)
  The kinds of classification a face of a mesh can have.
### Inspecting mesh anchors
- [var id: UUID](meshanchor/id.md)
  The unique identifier of this anchor.
- [var description: String](meshanchor/description.md)
  A textual representation of this anchor.
### Default Implementations
- [ARKitCoordinateSpaceProviding Implementations](meshanchor/arkitcoordinatespaceproviding-implementations.md)
- [Equatable Implementations](meshanchor/equatable-implementations.md)

## Relationships

### Conforms To
- [ARKitCoordinateSpaceProviding](arkitcoordinatespaceproviding.md)
- [Anchor](anchor.md)
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Incorporating real-world surroundings in an immersive experience](../visionos/incorporating-real-world-surroundings-in-an-immersive-experience.md)
  Create an immersive experience by making your app’s content respond to the local shape of the world.
- [Applying mesh to real-world surroundings](../visionos/applying-mesh-to-real-world-surroundings.md)
  Add a layer of mesh to objects in the real world, using scene reconstruction in ARKit.
- [Obscuring virtual items in a scene behind real-world items](../visionos/obscuring-virtual-items-in-a-scene-behind-real-world-items.md)
  Increase the realism of an immersive experience by adding entities with invisible materials  real-world objects.
- [class SceneReconstructionProvider](scenereconstructionprovider.md)
  A source of live data about the shape of a person’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/meshanchor)*