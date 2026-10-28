# backgroundMaterial

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The material underneath the current view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var backgroundMaterial: Material? { get set }
```

## Discussion

This value is `nil` if the current background isn’t one of the standard materials. If you set a material, the standard content styles enable their vibrant rendering modes.

You set this value by calling one of the background modifiers that takes a [`ShapeStyle`](../shapestyle.md), like [`background(_:ignoresSafeAreaEdges:)`](../view/background%28_,ignoressafeareaedges%29.md) or [`background(_:in:fillStyle:)`](../view/background%28_,in,fillstyle%29.md), and passing in a [`Material`](../material.md). You can also set the value manually, using `nil` to disable vibrant rendering, or a [`Material`](../material.md) instance to enable the vibrancy style associated with the specified material.

## See Also

### Layering views
- [Adding a background to your view](../adding-a-background-to-your-view.md)
  Compose a background behind your view and extend it beyond the safe area insets.
- [struct ZStack](../zstack.md)
  A view that overlays its subviews, aligning them in both axes.
- [func zIndex(Double) -> some View](../view/zindex%28_%29.md)
  Controls the display order of overlapping views.
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](../view/background%28alignment,content%29.md)
  Layers the views that you specify behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](../view/background%28_,ignoressafeareaedges%29.md)
  Sets the view’s background to a style.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](../view/background%28ignoressafeareaedges%29.md)
  Sets the view’s background to the default background style.
- [func background(_:in:fillStyle:)](../view/background%28_,in,fillstyle%29.md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background(in:fillStyle:)](../view/background%28in,fillstyle%29.md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](../view/overlay%28alignment,content%29.md)
  Layers the views that you specify in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](../view/overlay%28_,ignoressafeareaedges%29.md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](../view/overlay%28_,in,fillstyle%29.md)
  Layers a shape that you specify in front of this view.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](../view/containerbackground%28_,for%29.md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](../view/containerbackground%28for,alignment,content%29.md)
  Sets the container background of the enclosing container using a view.
- [struct ContainerBackgroundPlacement](../containerbackgroundplacement.md)
  The placement of a container background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/backgroundmaterial)*