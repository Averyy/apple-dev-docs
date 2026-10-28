# convert(_:from:to:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Converts a Rotation3D from a defined SwiftUI coordinate space to a quaternion in a RealityKit coordinate space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func convert(_ rotation: Rotation3D, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> simd_quatf
```

**Other overloads**:

```swift
func convert(_ point: Point3D, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> SIMD3<Float>
```

```swift
func convert(_ rect: Rect3D, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> BoundingBox
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

## Discussion

This function performs a change-of-basis operation, so the returned quaternion performs the same transformation in `realitySpace` that the specified `Rotation3D` performs in `space`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realitycoordinatespaceconverting/convert(_:from:to:)-1l9lu)*