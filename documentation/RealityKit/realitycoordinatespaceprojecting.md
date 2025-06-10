# RealityCoordinateSpaceProjecting

**Framework**: RealityKit  
**Kind**: protocol

A protocol for coordinate spaces that can project 2D points to and from 3D.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
protocol RealityCoordinateSpaceProjecting
```

## Topics

### Instance Methods
- [func entities(at: CGPoint, in: some CoordinateSpaceProtocol) -> [Entity]](realitycoordinatespaceprojecting/entities(at:in:).md)
  Finds all the hit entities when projecting a ray from a starting point.
- [func entity(at: CGPoint, in: some CoordinateSpaceProtocol) -> Entity?](realitycoordinatespaceprojecting/entity(at:in:).md)
  Finds the first entity hit when projecting a ray from a starting point.
- [func hitTest(point: CGPoint, in: some CoordinateSpaceProtocol, query: CollisionCastQueryType, mask: CollisionGroup) -> [CollisionCastHit]](realitycoordinatespaceprojecting/hittest(point:in:query:mask:).md)
  Searches the scene for entities at the specified point in the view.
- [func project(point: SIMD3<Float>, to: some CoordinateSpaceProtocol) -> CGPoint?](realitycoordinatespaceprojecting/project(point:to:).md)
  Projects a point from the 3D world coordinate system of the scene to the 2D pixel coordinate system of the reality view.
- [func ray(through: CGPoint, in: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> (origin: SIMD3<Float>, direction: SIMD3<Float>)?](realitycoordinatespaceprojecting/ray(through:in:to:).md)
  Determines the position and direction of a ray through the given point in the 2D space of the view.
- [func unproject(CGPoint, from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace, ontoPlane: float4x4) -> SIMD3<Float>?](realitycoordinatespaceprojecting/unproject(_:from:to:ontoplane:).md)
  Unprojects a point from the view onto a plane in 3D world coordinates.

## Relationships

### Conforming Types
- [EntityTargetValue](entitytargetvalue.md)
- [RealityViewCameraContent](realityviewcameracontent.md)

## See Also

- [protocol RealityCoordinateSpaceConverting](realitycoordinatespaceconverting.md)
  A value that can be converted between SwiftUI `CoordinateSpace` and RealityKit `Entity`.
- [struct SceneRealityCoordinateSpace](scenerealitycoordinatespace.md)
  The coordinate space that represents the center of a RealityKit scene.
- [struct CameraRealityCoordinateSpace](camerarealitycoordinatespace.md)
  The coordinate space that represents the scene’s active camera.
- [protocol RealityCoordinateSpace](realitycoordinatespace.md)
  A 3D coordinate space that exists within a RealityKit hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realitycoordinatespaceprojecting)*