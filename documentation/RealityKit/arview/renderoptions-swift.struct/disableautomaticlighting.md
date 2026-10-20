# disableAutomaticLighting

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

Disable automatic updates of the scene lighting.

**Availability**:
- iOS 13.0+ - Deprecated (renamed: disableAREnvironmentLighting)
- iPadOS 13.0+ - Deprecated (renamed: disableAREnvironmentLighting)
- Mac Catalyst 14.0+ - Deprecated (renamed: disableAREnvironmentLighting)

## Declaration

```swift
static let disableAutomaticLighting: ARView.RenderOptions
```

#### Discussion

By default, ARKit analyzes the scene lighting in captured camera images and automatically updates lighting in the scene. Add the [`disableAutomaticLighting`](./disableautomaticlighting.md) option to the AR view’s [`renderOptions`](../renderoptions-swift.property.md) to disable the feature.

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
- [static let disableFaceMesh: ARView.RenderOptions](./disablefacemesh.md)
  Disable generation of the face entity with the default occlusion material.
- [static let disablePersonOcclusion: ARView.RenderOptions](./disablepersonocclusion.md)
  Disable person segmentation.
- [static let disableAREnvironmentLighting: ARView.RenderOptions](./disablearenvironmentlighting.md)
  Disable lighting from environment probes.
- [static let disableFaceOcclusions: ARView.RenderOptions](./disablefaceocclusions.md)
  Disable automatic face occlusion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.struct/disableautomaticlighting)*