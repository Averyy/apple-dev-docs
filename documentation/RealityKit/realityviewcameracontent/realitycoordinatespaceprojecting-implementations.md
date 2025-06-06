# RealityCoordinateSpaceProjecting Implementations

**Framework**: RealityKit

## Topics

### Instance Methods
- [func entities(at: CGPoint, in: some CoordinateSpaceProtocol) -> [Entity]](realityviewcameracontent/entities(at:in:).md)
  Finds all the hit entities when projecting a ray from a starting point.
- [func entity(at: CGPoint, in: some CoordinateSpaceProtocol) -> Entity?](realityviewcameracontent/entity(at:in:).md)
  Finds the first entity hit when projecting a ray from a starting point.
- [func hitTest(point: CGPoint, in: some CoordinateSpaceProtocol, query: CollisionCastQueryType, mask: CollisionGroup) -> [CollisionCastHit]](realityviewcameracontent/hittest(point:in:query:mask:).md)
  Searches the scene for entities at the specified point in the view.
- [func project(point: SIMD3<Float>, to: some CoordinateSpaceProtocol) -> CGPoint?](realityviewcameracontent/project(point:to:).md)
  Projects a point from the 3D world coordinate system of the scene to the 2D pixel coordinate system of the reality view.
- [func ray(through: CGPoint, in: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> (origin: SIMD3<Float>, direction: SIMD3<Float>)?](realityviewcameracontent/ray(through:in:to:).md)
  Determines the position and direction of a ray through the given point in the 2D space of the view.
- [func unproject(CGPoint, from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace, ontoPlane: float4x4) -> SIMD3<Float>?](realityviewcameracontent/unproject(_:from:to:ontoplane:).md)
  Unprojects a point from the view onto a plane in 3D world coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcameracontent/realitycoordinatespaceprojecting-implementations)*