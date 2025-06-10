# projectionTransform

**Framework**: SceneKit  
**Kind**: property

The camera’s projection transformation.

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
var projectionTransform: SCNMatrix4 { get set }
```

#### Discussion

This transformation expresses the combination of all the camera’s geometric properties: projection type (perspective or orthographic), field of view, depth limits, and orthographic scale (if applicable). SceneKit uses this transformation to convert points in the camera node’s coordinate space to the renderer’s 2D space when rendering and processing events.

You can use this transformation directly if your app needs to convert between view and renderer coordinates for other purposes. Alternatively, if you compute your own projection transform matrix, you can set this property to override the transformation synthesized from the camera’s geometric properties.

> ❗ **Important**:  If you set this property to a custom value, properties such as [`zFar`](scncamera/zfar.md), [`zNear`](scncamera/znear.md), and [`fieldOfView`](scncamera/fieldofview.md) no longer reflect the current camera projection. (The mathematical process that derives a projection matrix from those properties cannot be reversed.) When you use SceneKit for an ARKit app with the [`ARSCNView`](https://developer.apple.com/documentation/ARKit/ARSCNView) class, ARKit overrides the camera’s projection matrix.

## See Also

- [var usesOrthographicProjection: Bool](scncamera/usesorthographicprojection.md)
  A Boolean value that determines whether the camera uses an orthographic projection.
- [var orthographicScale: Double](scncamera/orthographicscale.md)
  Specifies the camera’s magnification factor when using an orthographic projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/projectiontransform)*