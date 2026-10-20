# HoverEffectComponent.HighlightHoverEffectStyle

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A type that configures the visual aspects of a highlight hover effect for an entity

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct HighlightHoverEffectStyle
```

## Topics

### Initializers
- [init(color:strength:)](./highlighthovereffectstyle/init%28color,strength%29.md)
  Creates a new highlight effect with a color and strength.
- [init(color:strength:opacityFunction:)](./highlighthovereffectstyle/init%28color,strength,opacityfunction%29.md)
  Creates a new highlight effect with a color and strength.
### Instance Properties
- [var color: NSColor](./highlighthovereffectstyle/color-369cd.md)
  The color tint for the highlight hover effect.
- [var color: UIColor](./highlighthovereffectstyle/color-9v0tl.md)
  The color tint for the highlight hover effect.
- [var opacityFunction: HoverEffectComponent.OpacityFunction](./highlighthovereffectstyle/opacityfunction.md)
  The blending technique the hover effect applies to the entity’s base material.
- [var strength: Float](./highlighthovereffectstyle/strength.md)
  A floating-point value that represents the intensity of the effect.
### Type Properties
- [static let `default`: HoverEffectComponent.HighlightHoverEffectStyle](./highlighthovereffectstyle/default.md)
  The default style applies a white uniform glow to the affect entity as well as a white spotlight glow at the hover location

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hovereffectcomponent/highlighthovereffectstyle)*