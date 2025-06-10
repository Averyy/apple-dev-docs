# orthographicScale

**Framework**: SceneKit  
**Kind**: property

Specifies the camera’s magnification factor when using an orthographic projection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var orthographicScale: Double { get set }
```

#### Discussion

In an orthographic projection, equally sized objects appear equally sized regardless of their distance from the camera. To switch between orthographic and perspective projections, see the [`usesOrthographicProjection`](scncamera/usesorthographicprojection.md) property.

## See Also

- [var projectionTransform: SCNMatrix4](scncamera/projectiontransform.md)
  The camera’s projection transformation.
- [var usesOrthographicProjection: Bool](scncamera/usesorthographicprojection.md)
  A Boolean value that determines whether the camera uses an orthographic projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/orthographicscale)*