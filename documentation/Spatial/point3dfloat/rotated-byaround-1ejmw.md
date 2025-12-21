# rotated(by:around:)

**Framework**: Spatial  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func rotated(by quaternion: simd_quatf, around pivot: Point3DFloat) -> Point3DFloat
```

#### Return Value

A point that’s rotated by the specified rotation.

#### Discussion

Returns a point that’s rotated by a quaternion around a specified pivot.

## Parameters

- `quaternion`: The quaternion that defines the rotation.
- `pivot`: The center of rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/point3dfloat/rotated(by:around:)-1ejmw)*