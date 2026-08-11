# plane(width:depth:)

**Framework**: RealityKit  
**Kind**: method

Creates a new rectangle reverb mesh with the specified dimensions in the entity’s xz-plane.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func plane(width: Float, depth: Float) -> Self
```

## Parameters

- `width`: The width of the plane along the x-axis, in meters.
- `depth`: The depth of the plane along the z-axis, in meters.

## See Also

- [static func shoebox(size: SIMD3<Float>) -> Self](reverbmeshresource/shoebox(size:).md)
  Creates a box mesh with the vertices positioned such that the bottom surface is at y=0, with faces oriented inward.
- [static func box(size: SIMD3<Float>) -> Self](reverbmeshresource/box(size:).md)
  Creates a box mesh with vertices positioned such that the origin is at the center, with faces oriented outward.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/reverbmeshresource/plane(width:depth:))*