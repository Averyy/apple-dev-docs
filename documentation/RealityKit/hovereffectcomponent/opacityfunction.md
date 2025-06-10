# HoverEffectComponent.OpacityFunction

**Framework**: RealityKit  
**Kind**: enum

The blending technique options a hover effect applies to its entity’s base material.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum OpacityFunction
```

## Topics

### Enumeration Cases
- [HoverEffectComponent.OpacityFunction.blend](hovereffectcomponent/opacityfunction/blend.md)
  Draws the hover effect with an opacity that’s equal to the product of the entity’s base material and the shader’s output.
- [HoverEffectComponent.OpacityFunction.full](hovereffectcomponent/opacityfunction/full.md)
  Applies an opaque hover effect and ignores the opacity of the entity’s base material.
- [HoverEffectComponent.OpacityFunction.mask](hovereffectcomponent/opacityfunction/mask.md)
  Applies a hover effect with full opacity when the opacity of the entity’s base material is greater than five percent.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hovereffectcomponent/opacityfunction)*