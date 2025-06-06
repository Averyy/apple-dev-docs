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

### Operators
- [static func == (HoverEffectComponent.OpacityFunction, HoverEffectComponent.OpacityFunction) -> Bool](hovereffectcomponent/opacityfunction/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [HoverEffectComponent.OpacityFunction.blend](hovereffectcomponent/opacityfunction/blend.md)
  Draws the hover effect with an opacity that’s equal to the product of the entity’s base material and the shader’s output.
- [HoverEffectComponent.OpacityFunction.full](hovereffectcomponent/opacityfunction/full.md)
  Applies an opaque hover effect and ignores the opacity of the entity’s base material.
- [HoverEffectComponent.OpacityFunction.mask](hovereffectcomponent/opacityfunction/mask.md)
  Applies a hover effect with full opacity when the opacity of the entity’s base material is greater than five percent.
### Instance Properties
- [var hashValue: Int](hovereffectcomponent/opacityfunction/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](hovereffectcomponent/opacityfunction/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](hovereffectcomponent/opacityfunction/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hovereffectcomponent/opacityfunction)*