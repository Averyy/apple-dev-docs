# GlassBackgroundEffectConfiguration

**Framework**: SwiftUI  
**Kind**: struct

A configuration used to build a custom effect.

**Availability**:
- visionOS 2.4+

## Declaration

```swift
struct GlassBackgroundEffectConfiguration
```

## Topics

### Structures
- [GlassBackgroundEffectConfiguration.Content](glassbackgroundeffectconfiguration/content-swift.struct.md)
  A type-erased content of a glass background.
### Instance Properties
- [let content: GlassBackgroundEffectConfiguration.Content](glassbackgroundeffectconfiguration/content-swift.property.md)
  A view that requires a glass background.

## See Also

- [func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some View](view/glassbackgroundeffect(displaymode:).md)
  Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode) -> some View](view/glassbackgroundeffect(in:displaymode:).md)
  Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [enum GlassBackgroundDisplayMode](glassbackgrounddisplaymode.md)
  The display mode of a glass background.
- [protocol GlassBackgroundEffect](glassbackgroundeffect.md)
  A specification for the appearance of a glass background.
- [struct AutomaticGlassBackgroundEffect](automaticglassbackgroundeffect.md)
  The automatic glass background effect.
- [struct FeatheredGlassBackgroundEffect](featheredglassbackgroundeffect.md)
  The feathered glass background effect.
- [struct PlateGlassBackgroundEffect](plateglassbackgroundeffect.md)
  The plate glass background effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/glassbackgroundeffectconfiguration)*