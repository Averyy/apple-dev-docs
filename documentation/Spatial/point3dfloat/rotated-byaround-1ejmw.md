# rotated(by:around:)

**Framework**: Spatial  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func rotated(by quaternion: simd_quatf, around pivot: Point3DFloat) -> Point3DFloat
```

#### Return Value

A point that’s rotated by the specified rotation.

## Parameters

- `quaternion`: The quaternion that defines the rotation.
- `pivot`: The center of rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/point3dfloat/rotated(by:around:)-1ejmw)*