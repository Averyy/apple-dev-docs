# disableFaceMesh

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

Disable generation of the face entity with the default occlusion material.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let disableFaceMesh: ARView.RenderOptions
```

## Discussion

By default, [ARKit](../../../ARKit/ARKit.md) detects people and hides virtual objects behind their faces.

## See Also

### Disabling rendering effects
- [static let disableCameraGrain: ARView.RenderOptions](./disablecameragrain.md)
  Disable the image noise effect.
- [static let disableHDR: ARView.RenderOptions](./disablehdr.md)
  Disable the high dynamic range post-processing effect.
- [static let disableGroundingShadows: ARView.RenderOptions](./disablegroundingshadows.md)
  Disable rendering of ambient occlusion and shadows that ground objects in an AR scene.
- [static let disableMotionBlur: ARView.RenderOptions](./disablemotionblur.md)
  Disable the motion blur for all virtual content.
- [static let disableDepthOfField: ARView.RenderOptions](./disabledepthoffield.md)
  Disable the depth of field effect for all virtual content.
- [static let disablePersonOcclusion: ARView.RenderOptions](./disablepersonocclusion.md)
  Disable person segmentation.
- [static let disableAREnvironmentLighting: ARView.RenderOptions](./disablearenvironmentlighting.md)
  Disable lighting from environment probes.
- [static let disableFaceOcclusions: ARView.RenderOptions](./disablefaceocclusions.md)
  Disable automatic face occlusion.
- [static let disableAutomaticLighting: ARView.RenderOptions](./disableautomaticlighting.md)
  Disable automatic updates of the scene lighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.struct/disablefacemesh)*