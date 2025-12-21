# binocularFrustumMatrixForDrawableTarget(drawableTarget:convention:increaseTangents:depthRange:)

**Framework**: Compositor Services  
**Kind**: method

Returns the transform which can be used for binocular frustum culling. A matrix to convert between the device coordinate space to normalized device coordinate space. This should be acquired between starting and submitting a frame. Renderer should not utilize this transform for actual rendering output.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func binocularFrustumMatrixForDrawableTarget(drawableTarget: LayerRenderer.Drawable.Target, convention: AxisDirectionConvention = .rightUpBack, increaseTangents: SIMD4<Float>, depthRange: SIMD2<Float>) -> matrix_float4x4
```

#### Return Value

A transform which combines  perspective projection matrix that transforms coordinates from view coordinate space to clip space and a view matrix which brings device coordinate space to binocular camera space

#### Discussion

```None
            /
           /
          / Monocular eye
         /------
```

Binocular  / eye    | \     ╱ \   ╱ \ ╱ \ Monocular eye ╲ ╲ ╲

The convention is defined in normalized device coordinates, which impact the rendering direction of rendering but have no impact on the convention used for model/view space. To convert from view space to the axis direction convention used by the projection matrix, a rotation/mirror matrix can be applied pre-projection matrix.

The axes are defined as: • X axes determines the horizontal direction of pixels – right convention means the left-most pixel is the left of the view • Y axes determines the vertical direction of pixels – up convention means the top-most pixel is the top of the view • Z axes determines the handedness/winding order The default convention is `rightUpBack` for CompositorServices and Metal renderers which has a counter-clockwise winding order.

It computes corresponding binocular view relative to views, for defined transforms and projection matrix.

To avoid false positives during culling, transform should have broader tangents and depth range compared to one will be used for rendering. As the the time performing culling becomes more distant from `presentation time`, renderer should request for wider tangents/depth.

`drawableTargetViewCount` for given target should be more than 1 view.

## Parameters

- `convention`: The normalized device coordinate axes convention used.
- `increaseTangents`: The requested increased tangents   for computing the projection transform. Values should be positive.
- `depthRange`: The requested depth range   for computing the projection transform. Values should be positive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/binocularfrustummatrixfordrawabletarget(drawabletarget:convention:increasetangents:depthrange:))*