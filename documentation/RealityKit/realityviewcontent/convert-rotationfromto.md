# convert(rotation:from:to:)

**Framework**: RealityKit  
**Kind**: method

Converts a quaternion from a RealityKit coordinate space to a Rotation3D in a defined SwiftUI coordinate space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func convert(rotation: simd_quatf, from realitySpace: some RealityCoordinateSpace, to space: some CoordinateSpaceProtocol) -> Rotation3D
```

#### Discussion

This function performs a change-of-basis operation, so the returned `Rotation3D` performs the same transformation in `space` that the specified quaternion performs in `realitySpace`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcontent/convert(rotation:from:to:))*