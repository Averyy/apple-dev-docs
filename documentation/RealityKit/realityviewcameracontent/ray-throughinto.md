# ray(through:in:to:)

**Framework**: RealityKit  
**Kind**: method

Determines the position and direction of a ray through the given point in the 2D space of the view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
func ray(through: CGPoint, in space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> (origin: SIMD3<Float>, direction: SIMD3<Float>)?
```

#### Return Value

A 3D ray, expressed in the `realitySpace` coordinate space, which starts at the camera position and passes through the specified `point`.

## Parameters

- `point`: A point in the provided coordinate space.
- `space`: The 2D coordinate space in which to interpret the  .
- `realitySpace`: The 3D coordinate space you want the returned ray in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcameracontent/ray(through:in:to:))*