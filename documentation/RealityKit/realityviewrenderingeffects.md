# RealityViewRenderingEffects

**Framework**: RealityKit  
**Kind**: struct

A struct for enabling and disabling rendering effects for RealityKit content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
struct RealityViewRenderingEffects
```

## Topics

### Instance Properties
- [var antialiasing: AntialiasingMode](realityviewrenderingeffects/antialiasing.md)
  Enables or disables an antialiasing effect which smooths the edges of virtual content.
- [var cameraGrain: RealityViewRenderingEffectMode](realityviewrenderingeffects/cameragrain.md)
  Enables or disables an image noise effect for virtual content.
- [var depthOfField: RealityViewRenderingEffectMode](realityviewrenderingeffects/depthoffield.md)
  Enables or disables a depth of field effect for virtual content.
- [var dynamicRange: RealityViewDynamicRange](realityviewrenderingeffects/dynamicrange.md)
  Enables or disables high dynamic range rendering for virtual content.
- [var motionBlur: RealityViewRenderingEffectMode](realityviewrenderingeffects/motionblur.md)
  Enables or disables a motion blur effect for virtual content.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct RealityViewEnvironment](realityviewenvironment.md)
  A struct that determines the background and default lighting properties for a reality view.
- [struct RealityViewRenderingEffectMode](realityviewrenderingeffectmode.md)
  A mode that determines whether a rendering effect is enabled or disabled.
- [struct RealityViewDynamicRange](realityviewdynamicrange.md)
  Options that determine the state of high dynamic range rendering for virtual content.
- [enum AntialiasingMode](antialiasingmode.md)
  The rendering technique used to smooth edges of virtual content.
- [ARView.Environment](arview/environment-swift.struct.md)
  A description of background, lighting, and acoustic properties for a view’s content.
- [ARView.RenderOptions](arview/renderoptions-swift.struct.md)
  The available rendering options that you use to selectively disable certain rendering effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewrenderingeffects)*