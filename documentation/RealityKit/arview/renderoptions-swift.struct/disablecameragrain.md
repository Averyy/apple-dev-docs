# disableCameraGrain

**Framework**: RealityKit  
**Kind**: property

Disable the image noise effect.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let disableCameraGrain: ARView.RenderOptions
```

#### Discussion

Images from a camera may contain a small amount of noise, called , that increases as the available light decreases. Virtual objects rendered without noise and placed into an otherwise grainy image look out of place. You can use RealityKit to add noise to the rendered output to match noise in the camera feed.

| Without camera grain | With camera grain |
| --- | --- |
| ![A screenshot of a scene with a blue sphere on a white surface. The white surface has grain, but the blue sphere does not, which makes the sphere appear out of place.](https://docs-assets.developer.apple.com/published/1f352b25e2cd3cc5669f56a96d80ea4b/ARView-RenderOptions-swift-struct-disableCameraGrain-without.jpg) | ![A screenshot of a scene with a blue sphere on a white surface. The white surface and the sphere both have gain, which makes the sphere better blend into the surroundings.](https://docs-assets.developer.apple.com/published/02fb553ab4017889f128a431dd0ecd17/ARView-RenderOptions-swift-struct-disableCameraGrain-with.jpg) |

Applying this effect involves a low, constant GPU cost. If necessary, you can disable the effect by adding the [`disableCameraGrain`](arview/renderoptions-swift.struct/disablecameragrain.md) option to the view’s [`renderOptions`](arview/renderoptions-swift.property.md) set. Disabling the effect is most useful for older devices, like those with an A9 processor or earlier.

When deciding whether to use any effect, be sure to consider your app’s CPU and GPU utilization, as described in [`Improving the Performance of a RealityKit App`](improving-the-performance-of-a-realitykit-app.md).

## See Also

- [static let disableHDR: ARView.RenderOptions](arview/renderoptions-swift.struct/disablehdr.md)
  Disable the high dynamic range post-processing effect.
- [static let disableGroundingShadows: ARView.RenderOptions](arview/renderoptions-swift.struct/disablegroundingshadows.md)
  Disable rendering of ambient occlusion and shadows that ground objects in an AR scene.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.struct/disablecameragrain)*