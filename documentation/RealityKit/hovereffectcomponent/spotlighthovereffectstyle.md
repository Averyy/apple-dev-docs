# HoverEffectComponent.SpotlightHoverEffectStyle

**Framework**: RealityKit  
**Kind**: struct

A type that configures the visual aspects of a spotlight hover effect for an entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct SpotlightHoverEffectStyle
```

## Topics

### Operators
- [static func == (HoverEffectComponent.SpotlightHoverEffectStyle, HoverEffectComponent.SpotlightHoverEffectStyle) -> Bool](hovereffectcomponent/spotlighthovereffectstyle/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(color: UIColor?, strength: Float)](hovereffectcomponent/spotlighthovereffectstyle/init(color:strength:)-58ai1.md)
  Creates a new spotlight effect with a color and strength.
- [init(color: NSColor?, strength: Float)](hovereffectcomponent/spotlighthovereffectstyle/init(color:strength:)-97kh4.md)
  Creates a new spotlight effect with a color and strength.
- [init(color: UIColor?, strength: Float, opacityFunction: HoverEffectComponent.OpacityFunction)](hovereffectcomponent/spotlighthovereffectstyle/init(color:strength:opacityfunction:)-3tsob.md)
  Creates a new spotlight effect with a color and strength.
- [init(color: NSColor?, strength: Float, opacityFunction: HoverEffectComponent.OpacityFunction)](hovereffectcomponent/spotlighthovereffectstyle/init(color:strength:opacityfunction:)-57r9t.md)
  Creates a new spotlight effect with a color and strength.
### Instance Properties
- [var color: NSColor](hovereffectcomponent/spotlighthovereffectstyle/color-4n481.md)
  The color tint for the spotlight hover effect.
- [var color: UIColor](hovereffectcomponent/spotlighthovereffectstyle/color-tdv8.md)
  The color tint for the spotlight hover effect.
- [var opacityFunction: HoverEffectComponent.OpacityFunction](hovereffectcomponent/spotlighthovereffectstyle/opacityfunction.md)
  The blending technique the hover effect applies to the entity’s base material.
- [var strength: Float](hovereffectcomponent/spotlighthovereffectstyle/strength.md)
  A floating-point value that represents the intensity of the effect.
### Type Properties
- [static let `default`: HoverEffectComponent.SpotlightHoverEffectStyle](hovereffectcomponent/spotlighthovereffectstyle/default.md)
  The default style applies a white spotlight glow at the hover location.
### Default Implementations
- [Equatable Implementations](hovereffectcomponent/spotlighthovereffectstyle/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hovereffectcomponent/spotlighthovereffectstyle)*