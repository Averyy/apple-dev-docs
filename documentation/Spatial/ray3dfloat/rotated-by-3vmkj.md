# rotated(by:)

**Framework**: Spatial  
**Kind**: method

Returns a ray that’s rotated by the specified quaternion.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func rotated(by quaternion: simd_quatf) -> Ray3DFloat
```

#### Discussion

- Returns A ray with a direction that’s rotated by the specified quaternion.

## Parameters

- `quaternion`: The quaternion that defines the rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3dfloat/rotated(by:)-3vmkj)*