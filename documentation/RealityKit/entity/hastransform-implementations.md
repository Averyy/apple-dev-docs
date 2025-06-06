# HasTransform Implementations

**Framework**: RealityKit

## Topics

### Instance Properties
- [var orientation: simd_quatf](entity/orientation.md)
  The rotation of the entity relative to its parent.
- [var position: SIMD3<Float>](entity/position.md)
  The position of the entity relative to its parent.
- [var scale: SIMD3<Float>](entity/scale.md)
  The scale of the entity relative to its parent.
- [var transform: Transform](entity/transform.md)
  The transform of an entity relative to its parent.
### Instance Methods
- [func align(GeometricPin, to: GeometricPin) -> float4x4?](entity/align(_:to:).md)
  Moves and rotates the entity by a transformation from the origin pin to the target pin.
- [func convert(direction: SIMD3<Float>, from: Entity?) -> SIMD3<Float>](entity/convert(direction:from:).md)
  Converts a direction vector from the local space of a reference entity to the local space of the entity on which you called this method.
- [func convert(direction: SIMD3<Float>, to: Entity?) -> SIMD3<Float>](entity/convert(direction:to:).md)
  Converts a direction vector from the local space of the entity on which you called this method to the local space of a reference entity.
- [func convert(normal: SIMD3<Float>, from: Entity?) -> SIMD3<Float>](entity/convert(normal:from:).md)
  Converts a normal vector from the local space of a reference entity to the local space of the entity on which you called this method.
- [func convert(normal: SIMD3<Float>, to: Entity?) -> SIMD3<Float>](entity/convert(normal:to:).md)
  Converts a normal vector from the local space of the entity on which you called this method to the local space of a reference entity.
- [func convert(position: SIMD3<Float>, from: Entity?) -> SIMD3<Float>](entity/convert(position:from:).md)
  Converts a position from the local space of a reference entity to the local space of the entity on which you called this method.
- [func convert(position: SIMD3<Float>, to: Entity?) -> SIMD3<Float>](entity/convert(position:to:).md)
  Converts a position from the local space of the entity on which you called this method to the local space of a reference entity.
- [func convert(transform: Transform, from: Entity?) -> Transform](entity/convert(transform:from:).md)
  Converts the scale, rotation, and position of a transform from the local space of a reference entity to the local space of the entity on which you called this method.
- [func convert(transform: Transform, to: Entity?) -> Transform](entity/convert(transform:to:).md)
  Converts the scale, rotation, and position of a transform from the local space of the entity on which you called this method to the local space of a reference entity.
- [func look(at: SIMD3<Float>, from: SIMD3<Float>, upVector: SIMD3<Float>, relativeTo: Entity?)](entity/look(at:from:upvector:relativeto:).md)
  Positions and orients the entity to look at a target from a given position.
- [func look(at: SIMD3<Float>, from: SIMD3<Float>, upVector: SIMD3<Float>, relativeTo: Entity?, forward: Entity.ForwardDirection)](entity/look(at:from:upvector:relativeto:forward:).md)
  Positions and orients the entity such that it looks at certain target from a give position.
- [func move(to: Transform, relativeTo: Entity?)](entity/move(to:relativeto:)-556u9.md)
  Moves an entity instantly to a new location given by a transform.
- [func move(to: float4x4, relativeTo: Entity?)](entity/move(to:relativeto:)-6yugm.md)
  Moves an entity instantly to a new location given by a 4x4 matrix.
- [func move(to: float4x4, relativeTo: Entity?, duration: TimeInterval, timingFunction: AnimationTimingFunction) -> AnimationPlaybackController](entity/move(to:relativeto:duration:timingfunction:)-3xuzw.md)
  Moves an entity over a period of time to a new location given by a 4x4 matrix.
- [func move(to: Transform, relativeTo: Entity?, duration: TimeInterval, timingFunction: AnimationTimingFunction) -> AnimationPlaybackController](entity/move(to:relativeto:duration:timingfunction:)-905k.md)
  Moves an entity over a period of time to a new location given by a transform.
- [func orientation(relativeTo: Entity?) -> simd_quatf](entity/orientation(relativeto:).md)
  Gets the orientation of an entity relative to the given entity.
- [func position(relativeTo: Entity?) -> SIMD3<Float>](entity/position(relativeto:).md)
  Gets the position of an entity relative to the given entity.
- [func scale(relativeTo: Entity?) -> SIMD3<Float>](entity/scale(relativeto:).md)
  Gets the scale of an entity relative to the given entity.
- [func setOrientation(simd_quatf, relativeTo: Entity?)](entity/setorientation(_:relativeto:).md)
  Sets the orientation of the entity relative to the given reference entity.
- [func setPosition(SIMD3<Float>, relativeTo: Entity?)](entity/setposition(_:relativeto:).md)
  Sets the position of the entity relative to the given reference entity.
- [func setScale(SIMD3<Float>, relativeTo: Entity?)](entity/setscale(_:relativeto:).md)
  Sets the scale factor of the entity relative to the given reference entity.
- [func setTransformMatrix(float4x4, relativeTo: Entity?)](entity/settransformmatrix(_:relativeto:).md)
  Sets the transform of the entity relative to the given reference entity using a 4x4 matrix representation.
- [func transformMatrix(relativeTo: Entity?) -> float4x4](entity/transformmatrix(relativeto:)-7yhub.md)
  Gets the 4 x 4 transform matrix of an entity relative to the given entity.
- [func visualBounds(recursive: Bool, relativeTo: Entity?, excludeInactive: Bool) -> BoundingBox](entity/visualbounds(recursive:relativeto:excludeinactive:).md)
  Computes a bounding box for the entity in the specified space, optionally including child entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/hastransform-implementations)*