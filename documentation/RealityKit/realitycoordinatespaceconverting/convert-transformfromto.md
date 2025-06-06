# convert(transform:from:to:)

**Framework**: RealityKit  
**Kind**: method

Returns an AffineTransform3D converted from a RealityKit coordinate space to a defined SwiftUI coordinate space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func convert(transform: Transform, from realitySpace: some RealityCoordinateSpace, to space: some CoordinateSpaceProtocol) -> AffineTransform3D
```

#### Discussion

This function performs a change-of-basis operation, so the returned `AffineTransform3D` performs the same transformation in `space` that the specified [`Transform`](transform.md) performs in `realitySpace`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realitycoordinatespaceconverting/convert(transform:from:to:))*