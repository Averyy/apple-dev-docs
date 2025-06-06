# HoverEffectComponent.HoverEffect

**Framework**: RealityKit  
**Kind**: struct

An effect that applies when a person looks at or directly touches the entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct HoverEffect
```

## Topics

### Type Methods
- [static func highlight(HoverEffectComponent.HighlightHoverEffectStyle) -> HoverEffectComponent.HoverEffect](hovereffectcomponent/hovereffect-swift.struct/highlight(_:).md)
  Returns a hover effect style that uniformly highlights the entity and also applies a feathered spotlight effect.
- [static func shader(HoverEffectComponent.ShaderHoverEffectInputs) -> HoverEffectComponent.HoverEffect](hovereffectcomponent/hovereffect-swift.struct/shader(_:).md)
  Returns a hover effect style that applies hover state data to a custom shader that applies to the entity’s model.
- [static func spotlight(HoverEffectComponent.SpotlightHoverEffectStyle) -> HoverEffectComponent.HoverEffect](hovereffectcomponent/hovereffect-swift.struct/spotlight(_:).md)
  Returns a hover effect that displays a feathered spotlight on the entity where the current hover location is.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hovereffectcomponent/hovereffect-swift.struct)*