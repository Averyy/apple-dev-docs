# RealityCoordinateSpaceConverting

**Framework**: RealityKit  
**Kind**: protocol

A value that can be converted between SwiftUI `CoordinateSpace` and RealityKit `Entity`.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
protocol RealityCoordinateSpaceConverting
```

## Topics

### Instance Methods
- [func convert(_:from:to:)](realitycoordinatespaceconverting/convert(_:from:to:).md)
  Converts a `Point3D` from a defined SwiftUI coordinate space to a 3D point in a RealityKit coordinate space.
- [func convert(boundingBox: BoundingBox, from: some RealityCoordinateSpace, to: some CoordinateSpaceProtocol) -> Rect3D](realitycoordinatespaceconverting/convert(boundingbox:from:to:).md)
  Converts a BoundingBox from a RealityKit coordinate space to a Rect3D in a defined SwiftUI coordinate space.
- [func convert(point: SIMD3<Float>, from: some RealityCoordinateSpace, to: some CoordinateSpaceProtocol) -> Point3D](realitycoordinatespaceconverting/convert(point:from:to:).md)
  Converts a 3D point from a RealityKit coordinate space to one in a SwiftUI coordinate space.
- [func convert(rotation: simd_quatf, from: some RealityCoordinateSpace, to: some CoordinateSpaceProtocol) -> Rotation3D](realitycoordinatespaceconverting/convert(rotation:from:to:).md)
  Converts a quaternion from a RealityKit coordinate space to a Rotation3D in a defined SwiftUI coordinate space.
- [func convert(size: SIMD3<Float>, from: some RealityCoordinateSpace, to: some CoordinateSpaceProtocol) -> Size3D](realitycoordinatespaceconverting/convert(size:from:to:).md)
  Converts a 3D size vector from a RealityKit coordinate space to a Size3D in a defined SwiftUI coordinate space.
- [func convert(transform: Transform, from: some RealityCoordinateSpace, to: some CoordinateSpaceProtocol) -> AffineTransform3D](realitycoordinatespaceconverting/convert(transform:from:to:).md)
  Returns an AffineTransform3D converted from a RealityKit coordinate space to a defined SwiftUI coordinate space.
- [func convert(vector: SIMD3<Float>, from: some RealityCoordinateSpace, to: some CoordinateSpaceProtocol) -> Vector3D](realitycoordinatespaceconverting/convert(vector:from:to:).md)
  Converts a 3D vector from a RealityKit coordinate space to one in a SwiftUI coordinate space.
- [func transform(from:to:)](realitycoordinatespaceconverting/transform(from:to:).md)

## Relationships

### Conforming Types
- [EntityTargetValue](entitytargetvalue.md)
- [RealityViewContent](realityviewcontent.md)

## See Also

- [struct SceneRealityCoordinateSpace](scenerealitycoordinatespace.md)
  The coordinate space that represents the center of a RealityKit scene.
- [struct CameraRealityCoordinateSpace](camerarealitycoordinatespace.md)
  The coordinate space that represents the scene’s active camera.
- [protocol RealityCoordinateSpace](realitycoordinatespace.md)
  A 3D coordinate space that exists within a RealityKit hierarchy.
- [protocol RealityCoordinateSpaceProjecting](realitycoordinatespaceprojecting.md)
  A protocol for coordinate spaces that can project 2D points to and from 3D.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realitycoordinatespaceconverting)*