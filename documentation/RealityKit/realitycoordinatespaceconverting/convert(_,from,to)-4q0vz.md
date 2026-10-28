# convert(_:from:to:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns a 3D Transform converted from a defined SwiftUI coordinate space to a RealityKit coordinate space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func convert(_ transform: AffineTransform3D, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> Transform
```

**Other overloads**:

```swift
func convert(_ point: Point3D, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> SIMD3<Float>
```

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
func convert(_ vector: Vector3D, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> SIMD3<Float>
```

## Discussion

This function performs a change-of-basis operation, so the returned [`Transform`](../transform.md) performs the same transformation in `realitySpace` that the specified `AffineTransform3D` performs in `space`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realitycoordinatespaceconverting/convert(_:from:to:)-4q0vz)*