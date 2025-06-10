# ARView.RenderOptions

**Framework**: RealityKit  
**Kind**: struct

The available rendering options that you use to selectively disable certain rendering effects.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
struct RenderOptions
```

## Mentions

- [Reducing GPU Utilization in Your RealityKit App](reducing-gpu-utilization-in-your-realitykit-app.md)

#### Overview

RealityKit applies effects to the render make the AR experience more immersive. You can selectively disable any of these effects by adding one or more options from the [`ARView.RenderOptions`](arview/renderoptions-swift.struct.md) set to the view’s [`renderOptions`](arview/renderoptions-swift.property.md) property.

When you initialize a new [`ARView`](arview.md) instance, RealityKit automatically disables certain effects for you, depending on the device hardware. You can change the view’s [`renderOptions`](arview/renderoptions-swift.property.md) to suit your app’s needs, but be sure to consider your app’s GPU utilization when doing so, as described in [`Improving the Performance of a RealityKit App`](improving-the-performance-of-a-realitykit-app.md).

## Topics

### Disabling rendering effects
- [static let disableCameraGrain: ARView.RenderOptions](arview/renderoptions-swift.struct/disablecameragrain.md)
  Disable the image noise effect.
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

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct RealityViewEnvironment](realityviewenvironment.md)
  A struct that determines the background and default lighting properties for a reality view.
- [struct RealityViewRenderingEffects](realityviewrenderingeffects.md)
  A struct for enabling and disabling rendering effects for RealityKit content.
- [struct RealityViewRenderingEffectMode](realityviewrenderingeffectmode.md)
  A mode that determines whether a rendering effect is enabled or disabled.
- [struct RealityViewDynamicRange](realityviewdynamicrange.md)
  Options that determine the state of high dynamic range rendering for virtual content.
- [enum AntialiasingMode](antialiasingmode.md)
  The rendering technique used to smooth edges of virtual content.
- [struct RealityViewPostProcessEffect](realityviewpostprocesseffect.md)
  A struct for enabling or disabling post processing effects for all content a reality view contains.
- [struct PostProcessEffectContext](postprocesseffectcontext.md)
  An object RealityKit passes data to a post process effect method.
- [ARView.Environment](arview/environment-swift.struct.md)
  A description of background, lighting, and acoustic properties for a view’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.struct)*