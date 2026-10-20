# glassBackgroundEffect(_:in:displayMode:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Fills the view’s background with a custom glass background effect and a shape that you specify.

**Availability**:
- visionOS 2.4+

## Declaration

```swift
nonisolated
func glassBackgroundEffect<T, S>(_ effect: S, in shape: T, displayMode: GlassBackgroundDisplayMode = .always) -> some View where T : InsettableShape, S : GlassBackgroundEffect
```

#### Return Value

A view with a glass background.

## Parameters

- `effect`: A [`GlassBackgroundEffect`](../glassbackgroundeffect.md) instance that SwiftUI uses to the fill the background shape that you specify.
- `shape`: An [`InsettableShape`](../insettableshape.md) instance that SwiftUI draws behind the view.
- `displayMode`: When to display the glass background. The default is [`GlassBackgroundDisplayMode.always`](../glassbackgrounddisplaymode/always.md).

## See Also

### Background elements
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](./background%28alignment,content%29.md)
  Layers the views that you specify behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](./background%28_,ignoressafeareaedges%29.md)
  Sets the view’s background to a style.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](./background%28ignoressafeareaedges%29.md)
  Sets the view’s background to the default background style.
- [func background(_:in:fillStyle:)](./background%28_,in,fillstyle%29.md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background(in:fillStyle:)](./background%28in,fillstyle%29.md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some View](./alternatingrowbackgrounds%28_%29.md)
  Overrides whether lists and tables in this view have alternating row backgrounds.
- [func listRowBackground<V>(V?) -> some View](./listrowbackground%28_%29.md)
  Places a custom background view behind a list row item.
- [func scrollContentBackground(Visibility) -> some View](./scrollcontentbackground%28_%29.md)
  Specifies the visibility of the background for scrollable views within this view.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](./containerbackground%28_,for%29.md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](./containerbackground%28for,alignment,content%29.md)
  Sets the container background of the enclosing container using a view.
- [func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some View](./glassbackgroundeffect%28displaymode%29.md)
  Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<S>(S, displayMode: GlassBackgroundDisplayMode) -> some View](./glassbackgroundeffect%28_,displaymode%29.md)
  Fills the view’s background with a custom glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode) -> some View](./glassbackgroundeffect%28in,displaymode%29.md)
  Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [func backgroundExtensionEffect() -> some View](./backgroundextensioneffect%28%29.md)
  Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
- [func backgroundExtensionEffect(isEnabled: Bool) -> some View](./backgroundextensioneffect%28isenabled%29.md)
  Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/glassbackgroundeffect(_:in:displaymode:))*