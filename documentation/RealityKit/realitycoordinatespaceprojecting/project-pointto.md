# project(point:to:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Projects a point from the 3D world coordinate system of the scene to the 2D pixel coordinate system of the reality view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
func project(point: SIMD3<Float>, to space: some CoordinateSpaceProtocol) -> CGPoint?
```

#### Return Value

A point in the provided coordinate space.

## Parameters

- `point`: The point in 3D world coordinates.
- `space`: The 2D coordinate space in which this function returns the point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realitycoordinatespaceprojecting/project(point:to:))*