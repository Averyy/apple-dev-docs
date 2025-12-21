# disableGroundingShadows

**Framework**: RealityKit  
**Kind**: property

Disable rendering of ambient occlusion and shadows that ground objects in an AR scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let disableGroundingShadows: ARView.RenderOptions
```

#### Discussion

Objects in the real world cast a grounding shadow onto adjacent surfaces due to ambient light. This provides viewers with a visual cue that the object is in close proximity to the surface. Objects without a grounding shadow appear disconnected from their environment. To create the same visual cue for virtual objects, RealityKit provides a grounding shadow effect.

![A side-by-side comparison of a virtual object — a three](https://docs-assets.developer.apple.com/published/3253c594fd848e9a1b779665453f6514/ARView-RenderOptions-swift-struct-disableGroundingShadows-1%402x.png)

Applying this effect involves a low, constant GPU cost. You can disable the effect by adding the [`disableGroundingShadows`](arview/renderoptions-swift.struct/disablegroundingshadows.md) option to the view’s [`renderOptions`](arview/renderoptions-swift.property.md) set, if needed. Disabling the effect is most useful for older devices, like those with an A9 processor or earlier.

## See Also

- [static let disableCameraGrain: ARView.RenderOptions](arview/renderoptions-swift.struct/disablecameragrain.md)
  Disable the image noise effect.
- [static let disableHDR: ARView.RenderOptions](arview/renderoptions-swift.struct/disablehdr.md)
  Disable the high dynamic range post-processing effect.
- [static let disableMotionBlur: ARView.RenderOptions](arview/renderoptions-swift.struct/disablemotionblur.md)
  Disable the motion blur for all virtual content.
- [static let disableDepthOfField: ARView.RenderOptions](arview/renderoptions-swift.struct/disabledepthoffield.md)
  Disable the depth of field effect for all virtual content.
- [static let disableFaceMesh: ARView.RenderOptions](arview/renderoptions-swift.struct/disablefacemesh.md)
  Disable generation of the face entity with the default occlusion material.
- [static let disablePersonOcclusion: ARView.RenderOptions](arview/renderoptions-swift.struct/disablepersonocclusion.md)
  Disable person segmentation.
- [static let disableAREnvironmentLighting: ARView.RenderOptions](arview/renderoptions-swift.struct/disablearenvironmentlighting.md)
  Disable lighting from environment probes.
- [static let disableFaceOcclusions: ARView.RenderOptions](arview/renderoptions-swift.struct/disablefaceocclusions.md)
  Disable automatic face occlusion.
- [static let disableAutomaticLighting: ARView.RenderOptions](arview/renderoptions-swift.struct/disableautomaticlighting.md)
  Disable automatic updates of the scene lighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.struct/disablegroundingshadows)*