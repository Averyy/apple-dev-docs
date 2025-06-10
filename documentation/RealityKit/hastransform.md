# HasTransform

**Framework**: RealityKit  
**Kind**: protocol

An interface that enables manipulating the scale, rotation, and translation of an entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency protocol HasTransform : Entity
```

#### Overview

All entities automatically adopt this protocol because the [`Entity`](entity.md) base class does. This adoption gives all entities a [`Transform`](transform.md) component, and a collection of methods for manipulating the component, that you use to position the entity in space.

## Topics

### Accessing the component
- [var transform: Transform](hastransform/transform.md)
  The transform of an entity relative to its parent.
### Scaling an entity
- [var scale: SIMD3<Float>](hastransform/scale.md)
  The scale of the entity relative to its parent.
- [func scale(relativeTo: Entity?) -> SIMD3<Float>](hastransform/scale(relativeto:).md)
  Gets the scale of an entity relative to the given entity.
- [func setScale(SIMD3<Float>, relativeTo: Entity?)](hastransform/setscale(_:relativeto:).md)
  Sets the scale factor of the entity relative to the given reference entity.
### Rotating an entity
- [var orientation: simd_quatf](hastransform/orientation.md)
  The rotation of the entity relative to its parent.
- [func orientation(relativeTo: Entity?) -> simd_quatf](hastransform/orientation(relativeto:).md)
  Gets the orientation of an entity relative to the given entity.
- [func setOrientation(simd_quatf, relativeTo: Entity?)](hastransform/setorientation(_:relativeto:).md)
  Sets the orientation of the entity relative to the given reference entity.
### Positioning an entity
- [var position: SIMD3<Float>](hastransform/position.md)
  The position of the entity relative to its parent.
- [func position(relativeTo: Entity?) -> SIMD3<Float>](hastransform/position(relativeto:).md)
  Gets the position of an entity relative to the given entity.
- [func setPosition(SIMD3<Float>, relativeTo: Entity?)](hastransform/setposition(_:relativeto:).md)
  Sets the position of the entity relative to the given reference entity.
### Using a matrix
- [Transforming entities between RealityKit coordinate spaces](transforming-entities-between-realitykit-coordinate-spaces.md)
  Move an entity between a volumetric window and an immersive space using coordinate space transformations.
- [func transformMatrix(relativeTo: Entity?) -> float4x4](hastransform/transformmatrix(relativeto:).md)
  Gets the 4 x 4 transform matrix of an entity relative to the given entity.
- [func setTransformMatrix(float4x4, relativeTo: Entity?)](hastransform/settransformmatrix(_:relativeto:).md)
  Sets the transform of the entity relative to the given reference entity using a 4x4 matrix representation.
### Moving an entity
- [func move(to: Transform, relativeTo: Entity?)](hastransform/move(to:relativeto:)-6lohd.md)
  Moves an entity instantly to a new location given by a transform.
- [func move(to: float4x4, relativeTo: Entity?)](hastransform/move(to:relativeto:)-6jul8.md)
  Moves an entity instantly to a new location given by a 4x4 matrix.
- [func look(at: SIMD3<Float>, from: SIMD3<Float>, upVector: SIMD3<Float>, relativeTo: Entity?)](hastransform/look(at:from:upvector:relativeto:).md)
  Positions and orients the entity to look at a target from a given position.
- [func look(at:from:upVector:relativeTo:forward:)](hastransform/look(at:from:upvector:relativeto:forward:).md)
  Positions and orients the entity such that it looks at certain target from a give position.
- [func align(GeometricPin, to: GeometricPin) -> float4x4?](hastransform/align(_:to:).md)
  Moves and rotates the entity by a transformation from the origin pin to the target pin.
### Animating an entity
- [func move(to: Transform, relativeTo: Entity?, duration: TimeInterval, timingFunction: AnimationTimingFunction) -> AnimationPlaybackController](hastransform/move(to:relativeto:duration:timingfunction:)-35qp2.md)
  Moves an entity over a period of time to a new location given by a transform.
- [func move(to: float4x4, relativeTo: Entity?, duration: TimeInterval, timingFunction: AnimationTimingFunction) -> AnimationPlaybackController](hastransform/move(to:relativeto:duration:timingfunction:)-6la93.md)
  Moves an entity over a period of time to a new location given by a 4x4 matrix.
### Converting values between coordinate spaces
- [func convert(position: SIMD3<Float>, from: Entity?) -> SIMD3<Float>](hastransform/convert(position:from:).md)
  Converts a position from the local space of a reference entity to the local space of the entity on which you called this method.
- [func convert(position: SIMD3<Float>, to: Entity?) -> SIMD3<Float>](hastransform/convert(position:to:).md)
  Converts a position from the local space of the entity on which you called this method to the local space of a reference entity.
- [func convert(direction: SIMD3<Float>, from: Entity?) -> SIMD3<Float>](hastransform/convert(direction:from:).md)
  Converts a direction vector from the local space of a reference entity to the local space of the entity on which you called this method.
- [func convert(direction: SIMD3<Float>, to: Entity?) -> SIMD3<Float>](hastransform/convert(direction:to:).md)
  Converts a direction vector from the local space of the entity on which you called this method to the local space of a reference entity.
- [func convert(normal: SIMD3<Float>, from: Entity?) -> SIMD3<Float>](hastransform/convert(normal:from:).md)
  Converts a normal vector from the local space of a reference entity to the local space of the entity on which you called this method.
- [func convert(normal: SIMD3<Float>, to: Entity?) -> SIMD3<Float>](hastransform/convert(normal:to:).md)
  Converts a normal vector from the local space of the entity on which you called this method to the local space of a reference entity.
- [func convert(transform: Transform, from: Entity?) -> Transform](hastransform/convert(transform:from:).md)
  Converts the scale, rotation, and position of a transform from the local space of a reference entity to the local space of the entity on which you called this method.
- [func convert(transform: Transform, to: Entity?) -> Transform](hastransform/convert(transform:to:).md)
  Converts the scale, rotation, and position of a transform from the local space of the entity on which you called this method to the local space of a reference entity.
### Getting a bounding box
- [func visualBounds(recursive: Bool, relativeTo: Entity?, excludeInactive: Bool) -> BoundingBox](hastransform/visualbounds(recursive:relativeto:excludeinactive:).md)
  Computes a bounding box for the entity in the specified space, optionally including child entities.
### Instance Methods
- [func move(to:relativeTo:)](hastransform/move(to:relativeto:).md)
  Moves an entity instantly to a new location given by a transform.
- [func move(to:relativeTo:duration:timingFunction:)](hastransform/move(to:relativeto:duration:timingfunction:).md)
  Moves an entity over a period of time to a new location given by a transform.

## Relationships

### Inherits From
- [Entity](entity.md)
### Inherited By
- [HasBodyTracking](hasbodytracking.md)
- [HasCollision](hascollision.md)
- [HasDirectionalLight](hasdirectionallight.md)
- [HasModel](hasmodel.md)
- [HasPerspectiveCamera](hasperspectivecamera.md)
- [HasPhysics](hasphysics.md)
- [HasPhysicsBody](hasphysicsbody.md)
- [HasPointLight](haspointlight.md)
- [HasSpotLight](hasspotlight.md)
### Conforming Types
- [AnchorEntity](anchorentity.md)
- [BodyTrackedEntity](bodytrackedentity.md)
- [DirectionalLight](directionallight.md)
- [Entity](entity.md)
- [ModelEntity](modelentity.md)
- [PerspectiveCamera](perspectivecamera.md)
- [PointLight](pointlight.md)
- [SpotLight](spotlight.md)
- [TriggerVolume](triggervolume.md)
- [ViewAttachmentEntity](viewattachmententity.md)

## See Also

- [struct Transform](transform.md)
  A component that defines the scale, rotation, and translation of an entity.
- [func transformMatrix(relativeTo: Entity.CoordinateSpaceReference) -> float4x4?](entity/transformmatrix(relativeto:).md)
  Returns the 4 x 4 transform matrix of an entity relative to the given coordinate space.
- [Entity.CoordinateSpaceReference](entity/coordinatespacereference.md)
  Defines the coordinate space reference for transform conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform)*