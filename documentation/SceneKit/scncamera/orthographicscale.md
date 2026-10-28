# orthographicScale

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

Specifies the camera’s magnification factor when using an orthographic projection.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var orthographicScale: Double { get set }
```

```objc
@property (nonatomic) double orthographicScale;
```

## Discussion

In an orthographic projection, equally sized objects appear equally sized regardless of their distance from the camera. To switch between orthographic and perspective projections, see the [`usesOrthographicProjection`](./usesorthographicprojection.md) property.

## See Also

### Managing the Projection Transform
- [var projectionTransform: SCNMatrix4](./projectiontransform.md)
  The camera’s projection transformation.
- [var usesOrthographicProjection: Bool](./usesorthographicprojection.md)
  A Boolean value that determines whether the camera uses an orthographic projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/orthographicscale)*