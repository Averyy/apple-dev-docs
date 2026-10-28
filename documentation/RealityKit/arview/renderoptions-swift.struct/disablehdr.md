# disableHDR

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

Disable the high dynamic range post-processing effect.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let disableHDR: ARView.RenderOptions
```

## Discussion

RealityKit applies a high dynamic range effect, along with tone mapping, as a post-processing step in the GPU during the render. This effect is computationally inexpensive, but you can add the [`disableHDR`](./disablehdr.md) option to the view’s [`renderOptions`](../renderoptions-swift.property.md) set to turn the effect off, if needed. Disabling the effect is most useful on older devices, like those with an A9 processor or earlier.

When deciding whether to use any effect, be sure to consider your app’s CPU and GPU utilization, as described in [Improving the Performance of a RealityKit App](../../improving-the-performance-of-a-realitykit-app.md).

## See Also

### Disabling rendering effects
- [static let disableCameraGrain: ARView.RenderOptions](./disablecameragrain.md)
  Disable the image noise effect.
- [static let disableGroundingShadows: ARView.RenderOptions](./disablegroundingshadows.md)
  Disable rendering of ambient occlusion and shadows that ground objects in an AR scene.
- [static let disableMotionBlur: ARView.RenderOptions](./disablemotionblur.md)
  Disable the motion blur for all virtual content.
- [static let disableDepthOfField: ARView.RenderOptions](./disabledepthoffield.md)
  Disable the depth of field effect for all virtual content.
- [static let disableFaceMesh: ARView.RenderOptions](./disablefacemesh.md)
  Disable generation of the face entity with the default occlusion material.
- [static let disablePersonOcclusion: ARView.RenderOptions](./disablepersonocclusion.md)
  Disable person segmentation.
- [static let disableAREnvironmentLighting: ARView.RenderOptions](./disablearenvironmentlighting.md)
  Disable lighting from environment probes.
- [static let disableFaceOcclusions: ARView.RenderOptions](./disablefaceocclusions.md)
  Disable automatic face occlusion.
- [static let disableAutomaticLighting: ARView.RenderOptions](./disableautomaticlighting.md)
  Disable automatic updates of the scene lighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.struct/disablehdr)*