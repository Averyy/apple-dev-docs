# projectPoint:orientation:viewportSize:

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns the projection of a point from the 3D world space detected by ARKit into the 2D space of a view rendering the scene.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0

## Declaration

```objc
- (CGPoint) projectPoint:(simd_float3) point orientation:(UIInterfaceOrientation) orientation viewportSize:(CGSize) viewportSize;
```

## Return Value

The projection of the specified point into a 2D pixel coordinate space whose origin is in the upper left corner and whose size matches that of the `viewportSize` parameter.

## Discussion

If you display AR content with SceneKit, the `ARSCNView` class provides an otherwise equivalent [`projectPoint(_:)`](../../SceneKit/scnscenerenderer/projectpoint%28_%29.md) method that requires fewer parameters (because the view can infer its orientation and size).

## Parameters

- `point`: The 3D world-space point to project into 2D view space.
- `orientation`: The orientation in which the camera image is to be presented.
- `viewportSize`: The size, in points, of the view in which the camera image is to be presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/projectpoint:orientation:viewportsize:)*