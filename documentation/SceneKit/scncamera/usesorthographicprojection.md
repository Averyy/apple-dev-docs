# usesOrthographicProjection

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether the camera uses an orthographic projection.

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
var usesOrthographicProjection: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), specifying a perspective projection. In a perspective projection, equally sized objects nearer to the camera appear larger than those farther away.

Set the value of this property to [`true`](https://developer.apple.com/documentation/Swift/true) to specify an orthographic projection. In an orthographic projection, equally sized objects appear equally sized regardless of distance from the camera.

To control the magnification factor of an orthographic camera, use its [`orthographicScale`](scncamera/orthographicscale.md) property.

## See Also

- [var projectionTransform: SCNMatrix4](scncamera/projectiontransform.md)
  The camera’s projection transformation.
- [var orthographicScale: Double](scncamera/orthographicscale.md)
  Specifies the camera’s magnification factor when using an orthographic projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/usesorthographicprojection)*