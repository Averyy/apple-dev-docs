# box(size:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Creates a box mesh with vertices positioned such that the origin is at the center, with faces oriented outward.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func box(size: SIMD3<Float>) -> Self
```

## Discussion

Use this factory method for objects that are *in* the scene rather than defining the scene, or when combining multiple reverb meshes to define a space (for example, separate entities for the floor, ceiling, and walls of a room).

## Parameters

- `size`: The width, height, and depth of the box, in meters.

## See Also

### Creating standard room shapes
- [static func shoebox(size: SIMD3<Float>) -> Self](./shoebox%28size%29.md)
  Creates a box mesh with the vertices positioned such that the bottom surface is at y=0, with faces oriented inward.
- [static func plane(width: Float, depth: Float) -> Self](./plane%28width,depth%29.md)
  Creates a new rectangle reverb mesh with the specified dimensions in the entity’s xz-plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/reverbmeshresource/box(size:))*