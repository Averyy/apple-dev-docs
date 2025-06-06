# RealityCoordinateSpaceConverting Implementations

**Framework**: RealityKit

## Topics

### Instance Methods
- [func convert(AffineTransform3D, from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> Transform](realityviewcontent/convert(_:from:to:)-3mtt3.md)
  Returns a 3D Transform converted from a defined SwiftUI coordinate space to a RealityKit coordinate space.
- [func convert(Rotation3D, from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> simd_quatf](realityviewcontent/convert(_:from:to:)-5l7df.md)
  Converts a Rotation3D from a defined SwiftUI coordinate space to a quaternion in a RealityKit coordinate space.
- [func convert(Vector3D, from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> SIMD3<Float>](realityviewcontent/convert(_:from:to:)-88idf.md)
  ConvConverts a 3D vector from a SwiftUI coordinate space to one in a RealityKit coordinate space.
- [func convert(Point3D, from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> SIMD3<Float>](realityviewcontent/convert(_:from:to:)-9p0pn.md)
  Converts a `Point3D` from a defined SwiftUI coordinate space to a 3D point in a RealityKit coordinate space.
- [func convert(Rect3D, from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> BoundingBox](realityviewcontent/convert(_:from:to:)-dq8.md)
  Converts a Rect3D from a defined SwiftUI coordinate space to a BoundingBox in a RealityKit coordinate space.
- [func convert(Size3D, from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> SIMD3<Float>](realityviewcontent/convert(_:from:to:)-kvk8.md)
  Converts a Size3D from a defined SwiftUI coordinate space to a 3D size vector in a RealityKit coordinate space.
- [func convert(boundingBox: BoundingBox, from: some RealityCoordinateSpace, to: some CoordinateSpaceProtocol) -> Rect3D](realityviewcontent/convert(boundingbox:from:to:).md)
  Converts a BoundingBox from a RealityKit coordinate space to a Rect3D in a defined SwiftUI coordinate space.
- [func convert(point: SIMD3<Float>, from: some RealityCoordinateSpace, to: some CoordinateSpaceProtocol) -> Point3D](realityviewcontent/convert(point:from:to:).md)
  Converts a 3D point from a RealityKit coordinate space to one in a SwiftUI coordinate space.
- [func convert(rotation: simd_quatf, from: some RealityCoordinateSpace, to: some CoordinateSpaceProtocol) -> Rotation3D](realityviewcontent/convert(rotation:from:to:).md)
  Converts a quaternion from a RealityKit coordinate space to a Rotation3D in a defined SwiftUI coordinate space.
- [func convert(size: SIMD3<Float>, from: some RealityCoordinateSpace, to: some CoordinateSpaceProtocol) -> Size3D](realityviewcontent/convert(size:from:to:).md)
  Converts a 3D size vector from a RealityKit coordinate space to a Size3D in a defined SwiftUI coordinate space.
- [func convert(transform: Transform, from: some RealityCoordinateSpace, to: some CoordinateSpaceProtocol) -> AffineTransform3D](realityviewcontent/convert(transform:from:to:).md)
  Returns an AffineTransform3D converted from a RealityKit coordinate space to a defined SwiftUI coordinate space.
- [func convert(vector: SIMD3<Float>, from: some RealityCoordinateSpace, to: some CoordinateSpaceProtocol) -> Vector3D](realityviewcontent/convert(vector:from:to:).md)
  Converts a 3D vector from a RealityKit coordinate space to one in a SwiftUI coordinate space.
- [func transform(from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> AffineTransform3D](realityviewcontent/transform(from:to:)-2vye3.md)
- [func transform(from: some RealityCoordinateSpace, to: some CoordinateSpaceProtocol) -> AffineTransform3D](realityviewcontent/transform(from:to:)-35xr5.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcontent/realitycoordinatespaceconverting-implementations)*