# transform

**Framework**: PHASE  
**Kind**: property

A matrix, in local coordinates, that determines the object’s pose in the scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var transform: simd_float4x4 { get set }
```

## Mentions

- [Playing sound from a location in a 3D scene](playing-sound-from-a-location-in-a-3d-scene.md)

#### Discussion

The value of this property requires orthogonal basis vectors and uniform scale.

The framework interprets the transform’s position values in a right-handed coordinate system, where the  axis extends upward and and the negative  axis extends forward.

##### Set an Objects Position

An object positions in the 3D scene by the transformʼs first 3 elements of the last column. The following code sets an object’s position to `(0,0,-6)`, which is 6 meters in front of the world origin `(0,0,0)`.

```swift
var boardPieceTransform: simd_float4x4 = matrix_identity_float4x4
boardPieceTransform.columns.3.z -= 6.0
boardPieceSource.transform = boardPieceTransform
```

Set the [`unitsPerMeter`](phaseengine/unitspermeter.md) parameter to instruct PHASE to interpret [`transform`](phaseobject/transform.md) values in your app’s preferred unit of measurement.

## See Also

- [var worldTransform: simd_float4x4](phaseobject/worldtransform.md)
  A matrix, in scene coordinates, that determines the object’s pose in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseobject/transform)*