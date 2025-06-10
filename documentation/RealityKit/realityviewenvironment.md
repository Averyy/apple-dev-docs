# RealityViewEnvironment

**Framework**: RealityKit  
**Kind**: struct

A struct that determines the background and default lighting properties for a reality view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
struct RealityViewEnvironment
```

## Topics

### Setting the environment background
- [static var `default`: RealityViewEnvironment](realityviewenvironment/default.md)
  The view uses any background style you apply via the view’s background style.
- [static func skybox(EnvironmentResource) -> RealityViewEnvironment](realityviewenvironment/skybox(_:).md)
  The view uses a skybox environment as the background.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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
- [ARView.RenderOptions](arview/renderoptions-swift.struct.md)
  The available rendering options that you use to selectively disable certain rendering effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewenvironment)*