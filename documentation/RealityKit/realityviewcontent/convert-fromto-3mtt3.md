# convert(_:from:to:)

**Framework**: RealityKit  
**Kind**: method

Returns a 3D Transform converted from a defined SwiftUI coordinate space to a RealityKit coordinate space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func convert(_ transform: AffineTransform3D, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> Transform
```

#### Discussion

This function performs a change-of-basis operation, so the returned [`Transform`](transform.md) performs the same transformation in `realitySpace` that the specified `AffineTransform3D` performs in `space`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcontent/convert(_:from:to:)-3mtt3)*