# transform

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The transformation matrix that converts between the device’s coordinate space to the position of the view in that space.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var transform: simd_float4x4 { get }
```

```c
simd_float4x4 cp_view_get_transform(cp_view_t view);
```

## Discussion

When you generate a frame, you specify a pose matrix that indicates the device’s position and orientation in the world coordinate space. When the device is a head-mounted display, the view for each eye has an additional matrix to specify the position of that eye relative to the device’s pose. Multiply the device’s pose matrix by the returned matrix to obtain the view’s location in the world coordinate space.

## See Also

### Getting the transformations
- [var tangents: simd_float4](./tangents.md)
  The tangent values for the angles you use to determine the planes of the viewing frustum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/view/transform)*