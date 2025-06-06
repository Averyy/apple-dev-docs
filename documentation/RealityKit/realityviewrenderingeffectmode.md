# RealityViewRenderingEffectMode

**Framework**: RealityKit  
**Kind**: struct

A mode that determines whether a rendering effect is enabled or disabled.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
struct RealityViewRenderingEffectMode
```

## Topics

### Setting the rendering effect mode
- [static var `default`: RealityViewRenderingEffectMode](realityviewrenderingeffectmode/default.md)
  The default rendering effect mode.
- [static var enabled: RealityViewRenderingEffectMode](realityviewrenderingeffectmode/enabled.md)
  The enabled rendering effect mode.
- [static var disabled: RealityViewRenderingEffectMode](realityviewrenderingeffectmode/disabled.md)
  The disabled rendering effect mode.
### Protocol support
- [func hash(into: inout Hasher)](realityviewrenderingeffectmode/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](realityviewrenderingeffectmode/hashvalue.md)
  The hash value.
- [static func == (RealityViewRenderingEffectMode, RealityViewRenderingEffectMode) -> Bool](realityviewrenderingeffectmode/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](realityviewrenderingeffectmode/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct RealityViewEnvironment](realityviewenvironment.md)
  A struct that determines the background and default lighting properties for a reality view.
- [struct RealityViewRenderingEffects](realityviewrenderingeffects.md)
  A struct for enabling and disabling rendering effects for RealityKit content.
- [struct RealityViewDynamicRange](realityviewdynamicrange.md)
  Options that determine the state of high dynamic range rendering for virtual content.
- [enum AntialiasingMode](antialiasingmode.md)
  The rendering technique used to smooth edges of virtual content.
- [ARView.Environment](arview/environment-swift.struct.md)
  A description of background, lighting, and acoustic properties for a view’s content.
- [ARView.RenderOptions](arview/renderoptions-swift.struct.md)
  The available rendering options that you use to selectively disable certain rendering effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewrenderingeffectmode)*