# convert(_:from:to:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Converts a `Point3D` from a defined SwiftUI coordinate space to a 3D point in a RealityKit coordinate space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func convert(_ point: Point3D, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> SIMD3<Float>
```

**Other overloads**:

```swift
func convert(_ rect: Rect3D, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> BoundingBox
```

```swift
func convert(_ rotation: Rotation3D, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> simd_quatf
```

```swift
func convert(_ size: Size3D, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> SIMD3<Float>
```

```swift
func convert(_ transform: AffineTransform3D, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> Transform
```

```swift
func convert(_ vector: Vector3D, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> SIMD3<Float>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realitycoordinatespaceconverting/convert(_:from:to:)-6uv65)*