# disableDepthOfField

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

Disable the depth of field effect for all virtual content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let disableDepthOfField: ARView.RenderOptions
```

## Discussion

When you set the focal point of a camera, you actually choose a range of focus rather than a point. Objects outside the range — either too close or too far away — appear out of focus, while objects inside the range appear in focus. The size of the range, known as the depth of field, depends on characteristics of the lens, the focal point, and other factors.

![An illustration of a camera with three virtual objects — each a](https://developer.apple.com/tutorials/images/com.apple.RealityKit/ARView-RenderOptions-swift-struct-disableDepthOfField-1@2x.png)

If you place a virtual object outside of the range of focus, it can appear detached from the scene in which it appears unless you blur the object to match its surroundings. In many cases, the depth of field is large enough that this doesn’t matter. But if it does matter for your app, you can enable a post-processing effect that blurs virtual objects to account for depth of field.

| Without depth of field | With depth of field |
| --- | --- |
| ![A screenshot of a scene with blue and red spheres of varying distance. The scene has no depth of field, so all objects appear in focus.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/ARView-RenderOptions-swift-struct-disableDepthOfField-2-without.jpg) | ![A screenshot of a scene with blue and red spheres of varying distance. The scene has depth field, so the sphere in the middle appears in focus, while the closer and further spheres appear slightly blurred.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/ARView-RenderOptions-swift-struct-disableDepthOfField-2-with.jpg) |

Because of its computational cost, the system disables depth of field by default when you create a new [`ARView`](../../arview.md) instance. To enable depth of field, remove the [`disableDepthOfField`](./disabledepthoffield.md) option from the [`renderOptions`](../renderoptions-swift.property.md) set. If you do enable depth of field, be sure to check your app’s performance, as described in [Improving the Performance of a RealityKit App](../../improving-the-performance-of-a-realitykit-app.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.struct/disabledepthoffield)*