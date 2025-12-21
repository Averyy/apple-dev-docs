# rotated(by:)

**Framework**: Spatial  
**Kind**: method

Returns a ray that’s rotated by the specified quaternion.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

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