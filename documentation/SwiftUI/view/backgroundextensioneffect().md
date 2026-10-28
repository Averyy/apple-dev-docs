# backgroundExtensionEffect()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func backgroundExtensionEffect() -> some View
```

## Discussion

Use this modifier when you want to extend the view beyond its bounds so the copies can function as backgrounds for other elements on top. The most common use case is to apply this to a view in the detail column of a navigation split view so it can extend under the sidebar or inspector region to provide seamless immersive visuals.

```swift
NavigationSplitView {
    // sidebar content
} detail: {
    ZStack {
        BannerView()
            .backgroundExtensionEffect()
    }
}
.inspector(isPresented: $showInspector) {
    // inspector content
}
```

Apply this modifier with discretion. This should often be used with only a single instance of background content with consideration of visual clarity and performance.

> **Note**: This modifier will clip the view to prevent copies from overlapping with each other.

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
- [func glassBackgroundEffect<T, S>(S, in: T, displayMode: GlassBackgroundDisplayMode) -> some View](./glassbackgroundeffect%28_,in,displaymode%29.md)
  Fills the view’s background with a custom glass background effect and a shape that you specify.
- [func backgroundExtensionEffect(isEnabled: Bool) -> some View](./backgroundextensioneffect%28isenabled%29.md)
  Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/backgroundextensioneffect())*