# unproject(_:to:)

**Framework**: RealityKit  
**Kind**: method

Unproject a 2D point from the gesture value into 3D world coordinates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
func unproject(_ keyPath: KeyPath<Value, CGPoint>, to realitySpace: some RealityCoordinateSpace) -> SIMD3<Float>?
```

#### Return Value

3D position in `realitySpace`.

## Parameters

- `keyPath`: A key path for a point on the gesture value.
- `realitySpace`: The 3D coordinate space of the returned point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitytargetvalue/unproject(_:to:))*