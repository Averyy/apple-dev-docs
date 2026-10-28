# usesOrthographicProjection

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the camera uses an orthographic projection.

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
var usesOrthographicProjection: Bool { get set }
```

```objc
@property (nonatomic) BOOL usesOrthographicProjection;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md), specifying a perspective projection. In a perspective projection, equally sized objects nearer to the camera appear larger than those farther away.

Set the value of this property to [`true`](../../Swift/true.md) to specify an orthographic projection. In an orthographic projection, equally sized objects appear equally sized regardless of distance from the camera.

To control the magnification factor of an orthographic camera, use its [`orthographicScale`](./orthographicscale.md) property.

## See Also

### Managing the Projection Transform
- [var projectionTransform: SCNMatrix4](./projectiontransform.md)
  The camera’s projection transformation.
- [var orthographicScale: Double](./orthographicscale.md)
  Specifies the camera’s magnification factor when using an orthographic projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/usesorthographicprojection)*