# convert(_:from:to:)

**Framework**: RealityKit  
**Kind**: method

Converts a Rotation3D from a defined SwiftUI coordinate space to a quaternion in a RealityKit coordinate space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func convert(_ rotation: Rotation3D, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> simd_quatf
```

#### Discussion

This function performs a change-of-basis operation, so the returned quaternion performs the same transformation in `realitySpace` that the specified `Rotation3D` performs in `space`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcontent/convert(_:from:to:)-5l7df)*