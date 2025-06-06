# unproject(_:from:to:)

**Framework**: RealityKit  
**Kind**: method

Unproject `point` from a 2D coordinate space into 3D world coordinates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
func unproject(_ point: CGPoint, from space: some CoordinateSpaceProtocol, to realitySpace: some RealityCoordinateSpace) -> SIMD3<Float>?
```

#### Return Value

3D position in `realitySpace`.

## Parameters

- `point`: A point in the provided coordinate space.
- `space`: The 2D coordinate space in which to interpret the  .
- `realitySpace`: The 3D coordinate space of the returned point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitytargetvalue/unproject(_:from:to:))*