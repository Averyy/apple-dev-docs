# disableAREnvironmentLighting

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

Disable lighting from environment probes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let disableAREnvironmentLighting: ARView.RenderOptions
```

## Discussion

By default, RealityKit automatically creates light probes to record the lighting conditions both globally, and at appropriate points in the scene. The framework adjusts the complexity of the light probe set to match the capabilities of the GPU. For example, it might use only a global probe on less capable devices. It then applies environment lighting to virtual objects based on the probes.

To disable this effect, add this option to the [`renderOptions`](../renderoptions-swift.property.md) set.

Alternatively, to use environment lighting but control the probes manually, ensure the render option set doesn’t include this option. Then configure the session for manual environment texturing, using the [`ARWorldTrackingConfiguration.EnvironmentTexturing.manual`](../../../ARKit/arworldtrackingconfiguration/environmenttexturing-swift.enum/manual.md) value.

For more information about creating and placing probes manually, see [Adding realistic reflections to an AR experience](../../../ARKit/adding-realistic-reflections-to-an-ar-experience.md).

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
- [static let disableFaceOcclusions: ARView.RenderOptions](./disablefaceocclusions.md)
  Disable automatic face occlusion.
- [static let disableAutomaticLighting: ARView.RenderOptions](./disableautomaticlighting.md)
  Disable automatic updates of the scene lighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.struct/disablearenvironmentlighting)*