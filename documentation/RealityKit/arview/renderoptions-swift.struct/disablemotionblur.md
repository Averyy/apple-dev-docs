# disableMotionBlur

**Framework**: RealityKit  
**Kind**: property

Disable the motion blur for all virtual content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
static let disableMotionBlur: ARView.RenderOptions
```

## Mentions

- [Reducing GPU Utilization in Your RealityKit App](reducing-gpu-utilization-in-your-realitykit-app.md)

#### Discussion

A video stream consists of a sequence of images. Each image in the sequence represents a short, but non-zero period of time. Fast-moving, real-world objects captured within a frame can experience a visual smearing, known as .

By default, virtual objects that appear in the scene don’t experience motion blur. Instead, they exist at exactly one point in the frame for any given image in the image sequence. RealityKit offers an effect that introduces motion blur for virtual objects, taking into account the relative motion of the camera and the object.

Because of its computational cost, motion blur is off by default on all but the latest hardware. To enable or disable the effect, you add or remove the [`disableMotionBlur`](arview/renderoptions-swift.struct/disablemotionblur.md) option to or from the [`renderOptions`](arview/renderoptions-swift.property.md) set, respectively. If you do enable motion blur, be sure to measure your app’s CPU and GPU utilization to find out how it affects your app’s performance, as described in [`Improving the Performance of a RealityKit App`](improving-the-performance-of-a-realitykit-app.md).

## See Also

- [static let disableCameraGrain: ARView.RenderOptions](arview/renderoptions-swift.struct/disablecameragrain.md)
  Disable the image noise effect.
- [static let disableHDR: ARView.RenderOptions](arview/renderoptions-swift.struct/disablehdr.md)
  Disable the high dynamic range post-processing effect.
- [static let disableGroundingShadows: ARView.RenderOptions](arview/renderoptions-swift.struct/disablegroundingshadows.md)
  Disable rendering of ambient occlusion and shadows that ground objects in an AR scene.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.struct/disablemotionblur)*