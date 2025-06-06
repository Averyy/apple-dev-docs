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
- [func convert(Rotation3D, from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> simd_quatf](realitycoordinatespaceconverting/convert(_:from:to:)-1l9lu.md)
  Converts a Rotation3D from a defined SwiftUI coordinate space to a quaternion in a RealityKit coordinate space.
- [func convert(Rect3D, from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> BoundingBox](realitycoordinatespaceconverting/convert(_:from:to:)-3fumk.md)
  Converts a Rect3D from a defined SwiftUI coordinate space to a BoundingBox in a RealityKit coordinate space.
- [func convert(AffineTransform3D, from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> Transform](realitycoordinatespaceconverting/convert(_:from:to:)-4q0vz.md)
  Returns a 3D Transform converted from a defined SwiftUI coordinate space to a RealityKit coordinate space.
- [func convert(Size3D, from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> SIMD3<Float>](realitycoordinatespaceconverting/convert(_:from:to:)-6547z.md)
  Converts a Size3D from a defined SwiftUI coordinate space to a 3D size vector in a RealityKit coordinate space.
- [func convert(Vector3D, from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> SIMD3<Float>](realitycoordinatespaceconverting/convert(_:from:to:)-67xm9.md)
  ConvConverts a 3D vector from a SwiftUI coordinate space to one in a RealityKit coordinate space.
- [func convert(Point3D, from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> SIMD3<Float>](realitycoordinatespaceconverting/convert(_:from:to:)-6uv65.md)
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
- [func transform(from: some RealityCoordinateSpace, to: some CoordinateSpaceProtocol) -> AffineTransform3D](realitycoordinatespaceconverting/transform(from:to:)-1fw4u.md)
- [func transform(from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> AffineTransform3D](realitycoordinatespaceconverting/transform(from:to:)-60jfs.md)

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