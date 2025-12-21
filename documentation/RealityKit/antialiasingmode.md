# AntialiasingMode

**Framework**: RealityKit  
**Kind**: enum

The rendering technique used to smooth edges of virtual content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
enum AntialiasingMode
```

## Topics

### Setting the antialiasing mode
- [AntialiasingMode.multisample4X](antialiasingmode/multisample4x.md)
  Multisampling renders each pixel multiple times and combines the results, creating a higher quality image at a performance cost proportional to the number of samples used.
- [AntialiasingMode.none](antialiasingmode/none.md)
  Do not apply any technique to smooth jagged edges.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [struct RealityViewPostProcessEffect](realityviewpostprocesseffect.md)
  A struct for enabling or disabling post processing effects for all content a reality view contains.
- [struct PostProcessEffectContext](postprocesseffectcontext.md)
  An object RealityKit passes data to a post process effect method.
- [ARView.Environment](arview/environment-swift.struct.md)
  A description of background, lighting, and acoustic properties for a view’s content.
- [ARView.RenderOptions](arview/renderoptions-swift.struct.md)
  The available rendering options that you use to selectively disable certain rendering effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/antialiasingmode)*