# RealityViewPostProcessEffect

**Framework**: RealityKit  
**Kind**: struct

A struct for enabling or disabling post processing effects for all content a reality view contains.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
struct RealityViewPostProcessEffect
```

## Topics

### Type Properties
- [static var none: RealityViewPostProcessEffect](realityviewpostprocesseffect/none.md)
  A mode that does not apply post processing effects.
### Type Methods
- [static func effect(some PostProcessEffect) -> RealityViewPostProcessEffect](realityviewpostprocesseffect/effect(_:).md)
  A post processing effect mode that accepts a conforming type for post processing.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [struct PostProcessEffectContext](postprocesseffectcontext.md)
  An object RealityKit passes data to a post process effect method.
- [ARView.Environment](arview/environment-swift.struct.md)
  A description of background, lighting, and acoustic properties for a view’s content.
- [ARView.RenderOptions](arview/renderoptions-swift.struct.md)
  The available rendering options that you use to selectively disable certain rendering effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewpostprocesseffect)*