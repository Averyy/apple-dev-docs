# HoverEffectComponent.HoverEffect

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

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

### Instance Properties
- [var groupID: HoverEffectComponent.GroupID?](./hovereffect-swift.struct/groupid.md)
  An optional group identifier for the hover effect.
### Type Methods
- [static func highlight(HoverEffectComponent.HighlightHoverEffectStyle) -> HoverEffectComponent.HoverEffect](./hovereffect-swift.struct/highlight%28_%29.md)
  Returns a hover effect style that uniformly highlights the entity and also applies a feathered spotlight effect.
- [static func highlight(HoverEffectComponent.HighlightHoverEffectStyle, groupID: HoverEffectComponent.GroupID) -> HoverEffectComponent.HoverEffect](./hovereffect-swift.struct/highlight%28_,groupid%29.md)
  Returns a highlight hover effect that is assigned to the group.
- [static func shader(HoverEffectComponent.ShaderHoverEffectInputs) -> HoverEffectComponent.HoverEffect](./hovereffect-swift.struct/shader%28_%29.md)
  Returns a hover effect style that applies hover state data to a custom shader that applies to the entity’s model.
- [static func shader(HoverEffectComponent.ShaderHoverEffectInputs, groupID: HoverEffectComponent.GroupID) -> HoverEffectComponent.HoverEffect](./hovereffect-swift.struct/shader%28_,groupid%29.md)
  Returns a shader hover effect that is assigned to the group.
- [static func spotlight(HoverEffectComponent.SpotlightHoverEffectStyle) -> HoverEffectComponent.HoverEffect](./hovereffect-swift.struct/spotlight%28_%29.md)
  Returns a hover effect that displays a feathered spotlight on the entity where the current hover location is.
- [static func spotlight(HoverEffectComponent.SpotlightHoverEffectStyle, groupID: HoverEffectComponent.GroupID) -> HoverEffectComponent.HoverEffect](./hovereffect-swift.struct/spotlight%28_,groupid%29.md)
  Returns a spotlight hover effect that is assigned to the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hovereffectcomponent/hovereffect-swift.struct)*