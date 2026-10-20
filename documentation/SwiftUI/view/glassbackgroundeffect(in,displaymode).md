# glassBackgroundEffect(in:displayMode:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Fills the view’s background with an automatic glass background effect and a shape that you specify.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func glassBackgroundEffect<S>(in shape: S, displayMode: GlassBackgroundDisplayMode = .always) -> some View where S : InsettableShape
```

#### Return Value

A view with a glass background.

#### Discussion

Use this modifier to add a 3D glass background material that includes thickness, specularity, glass blur, shadows, and other effects. Because of its physical depth, the glass background influences z-axis layout.

To ensure that the effect renders properly when you add it to a collection of views in a [`ZStack`](../zstack.md), add the modifier to the stack rather to one of the views in the stack. This includes when you create an implicit stack with view modifiers like [`overlay(alignment:content:)`](./overlay%28alignment,content%29.md) or [`background(alignment:content:)`](./background%28alignment,content%29.md). In those cases, you might need to create an explicit [`ZStack`](../zstack.md) inside the `content` closure to have a place to add the glass background modifier.

Non closed shapes will be rendered as their convex hull.

## Parameters

- `shape`: An [`InsettableShape`](../insettableshape.md) instance that SwiftUI draws behind the view.
- `displayMode`: When to display the glass background. The default is [`GlassBackgroundDisplayMode.always`](../glassbackgrounddisplaymode/always.md).

## See Also

### Adding a glass background on views in visionOS
- [func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some View](./glassbackgroundeffect%28displaymode%29.md)
  Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [enum GlassBackgroundDisplayMode](../glassbackgrounddisplaymode.md)
  The display mode of a glass background.
- [protocol GlassBackgroundEffect](../glassbackgroundeffect.md)
  A specification for the appearance of a glass background.
- [struct AutomaticGlassBackgroundEffect](../automaticglassbackgroundeffect.md)
  The automatic glass background effect.
- [struct GlassBackgroundEffectConfiguration](../glassbackgroundeffectconfiguration.md)
  A configuration used to build a custom effect.
- [struct FeatheredGlassBackgroundEffect](../featheredglassbackgroundeffect.md)
  The feathered glass background effect.
- [struct PlateGlassBackgroundEffect](../plateglassbackgroundeffect.md)
  The plate glass background effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/glassbackgroundeffect(in:displaymode:))*