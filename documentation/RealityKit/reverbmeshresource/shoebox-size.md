# shoebox(size:)

**Framework**: RealityKit  
**Kind**: method

Creates a box mesh with the vertices positioned such that the bottom surface is at y=0, with faces oriented inward.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func shoebox(size: SIMD3<Float>) -> Self
```

#### Discussion

Use this factory method for objects that *define* the scene rather than objects within it — for example, the enclosing walls, floor, and ceiling of a room.

```swift
let room = ReverbMeshResource.shoebox(size: [4, 3, 5])
```

## Parameters

- `size`: The width, height, and depth of the box, in meters.

## See Also

- [static func box(size: SIMD3<Float>) -> Self](reverbmeshresource/box(size:).md)
  Creates a box mesh with vertices positioned such that the origin is at the center, with faces oriented outward.
- [static func plane(width: Float, depth: Float) -> Self](reverbmeshresource/plane(width:depth:).md)
  Creates a new rectangle reverb mesh with the specified dimensions in the entity’s xz-plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/reverbmeshresource/shoebox(size:))*