# GlassBackgroundEffect

**Framework**: SwiftUI  
**Kind**: protocol

A specification for the appearance of a glass background.

**Availability**:
- visionOS 2.4+

## Declaration

```swift
protocol GlassBackgroundEffect
```

## Topics

### Associated Types
- [associatedtype Body : GlassBackgroundEffect](glassbackgroundeffect/body.md)
  The type of effect representing the body of this effect. When you create a custom effect, Swift infers this type from your implementation of the required [`makeBody(configuration:)`](glassbackgroundeffect/makebody(configuration:).md) method.
### Instance Methods
- [func makeBody(configuration: Self.Configuration) -> Self.Body](glassbackgroundeffect/makebody(configuration:).md)
  Defines the effect produced by this effect.
### Type Aliases
- [GlassBackgroundEffect.Configuration](glassbackgroundeffect/configuration.md)
  The configuration type passed to `makeBody(configuration:)`.
### Type Properties
- [static var automatic: AutomaticGlassBackgroundEffect](glassbackgroundeffect/automatic.md)
  The default glass background effect, based on the glass’s context.
- [static var feathered: FeatheredGlassBackgroundEffect](glassbackgroundeffect/feathered.md)
  A feathered background effect with default padding amount and default soft edge radiual size.
- [static var plate: PlateGlassBackgroundEffect](glassbackgroundeffect/plate.md)
  A plate glass background effect.
### Type Methods
- [static func feathered(padding: CGFloat, softEdgeRadius: CGFloat?) -> FeatheredGlassBackgroundEffect](glassbackgroundeffect/feathered(padding:softedgeradius:).md)
  A feathered background effect with custom padding and soft edge radius.

## Relationships

### Conforming Types
- [AutomaticGlassBackgroundEffect](automaticglassbackgroundeffect.md)
- [FeatheredGlassBackgroundEffect](featheredglassbackgroundeffect.md)
- [PlateGlassBackgroundEffect](plateglassbackgroundeffect.md)

## See Also

- [func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some View](view/glassbackgroundeffect(displaymode:).md)
  Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode) -> some View](view/glassbackgroundeffect(in:displaymode:).md)
  Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [enum GlassBackgroundDisplayMode](glassbackgrounddisplaymode.md)
  The display mode of a glass background.
- [struct AutomaticGlassBackgroundEffect](automaticglassbackgroundeffect.md)
  The automatic glass background effect.
- [struct GlassBackgroundEffectConfiguration](glassbackgroundeffectconfiguration.md)
  A configuration used to build a custom effect.
- [struct FeatheredGlassBackgroundEffect](featheredglassbackgroundeffect.md)
  The feathered glass background effect.
- [struct PlateGlassBackgroundEffect](plateglassbackgroundeffect.md)
  The plate glass background effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/glassbackgroundeffect)*