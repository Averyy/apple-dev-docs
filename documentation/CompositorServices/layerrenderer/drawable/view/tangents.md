# tangents

**Framework**: Compositor Services  
**Kind**: property

The tangent values for the angles you use to determine the planes of the viewing frustum.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var tangents: simd_float4 { get }
```

#### Discussion

In a 3D scene, the viewing frustum is the volume between the near and far clipping planes that contains the scene’s visible content. When you render this content into a view, you generate a two-dimensional version of your content suitable for display. To ensure your content still looks three-dimensional, apply a perspective projection matrix to your content. This matrix scales your content appropriately based on its distance from the viewing point.

This function returns the tangent values you use to build the perspective projection matrix for your content. You can also use the values to determine the apparent size of the view at any distance from the viewing point. When you multiply a tangent value by a distance, you obtain the horizontal or vertical distance from the view’s center point to the corresponding rectangle edge at that distance. For a perspective projection matrix, multiply these values by the distance to the near clipping plane and combine them to create the matrix rows you need.

> **Note**: The angles and tangent values are always positive.

The angles and tangent values are always positive.

## See Also

- [var transform: simd_float4x4](layerrenderer/drawable/view/transform.md)
  The transformation matrix that converts between the device’s coordinate space to the position of the view in that space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/view/tangents)*