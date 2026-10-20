# background(_:in:fillStyle:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the view’s background to an insettable shape filled with a style.

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
nonisolated
func background<S, T>(_ style: S, in shape: T, fillStyle: FillStyle = FillStyle()) -> some View where S : ShapeStyle, T : InsettableShape
```

**Other overloads**:

```swift
nonisolated
func background<S, T>(_ style: S, in shape: T, fillStyle: FillStyle = FillStyle()) -> some View where S : ShapeStyle, T : Shape
```

#### Return Value

A view with the specified insettable shape drawn behind it.

#### Discussion

Use this modifier to layer a type that conforms to the [`InsettableShape`](../insettableshape.md) protocol — like a [`Rectangle`](../rectangle.md), [`Circle`](../circle.md), or [`Capsule`](../capsule.md) — behind a view. Specify the [`ShapeStyle`](../shapestyle.md) that’s used to fill the shape. For example, you can place a [`RoundedRectangle`](../roundedrectangle.md) behind a [`Label`](../label.md):

```swift
Label("Flag", systemImage: "flag.fill")
    .padding()
    .background(.teal, in: RoundedRectangle(cornerRadius: 8))
```

The [`teal`](../shapestyle/teal.md) color fills the shape:

![A screenshot of the flag icon and word on a teal rectangle with](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-background-8@2x.png)

This modifier is a convenience method for placing a single shape behind a view. To create a background with other [`View`](../view.md) types — or with a stack of views — use [`background(alignment:content:)`](./background%28alignment,content%29.md) instead. To add a [`ShapeStyle`](../shapestyle.md) as a background, use [`background(_:ignoresSafeAreaEdges:)`](./background%28_,ignoressafeareaedges%29.md).

## Parameters

- `style`: A [`ShapeStyle`](../shapestyle.md) that SwiftUI uses to the fill the shape that you specify.
- `shape`: An instance of a type that conforms to [`InsettableShape`](../insettableshape.md) that SwiftUI draws behind the view.
- `fillStyle`: The [`FillStyle`](../fillstyle.md) to use when drawing the shape. The default style uses the nonzero winding number rule and antialiasing.

## See Also

### Layering views
- [Adding a background to your view](../adding-a-background-to-your-view.md)
  Compose a background behind your view and extend it beyond the safe area insets.
- [struct ZStack](../zstack.md)
  A view that overlays its subviews, aligning them in both axes.
- [func zIndex(Double) -> some View](./zindex%28_%29.md)
  Controls the display order of overlapping views.
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](./background%28alignment,content%29.md)
  Layers the views that you specify behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](./background%28_,ignoressafeareaedges%29.md)
  Sets the view’s background to a style.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](./background%28ignoressafeareaedges%29.md)
  Sets the view’s background to the default background style.
- [func background(in:fillStyle:)](./background%28in,fillstyle%29.md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](./overlay%28alignment,content%29.md)
  Layers the views that you specify in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](./overlay%28_,ignoressafeareaedges%29.md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](./overlay%28_,in,fillstyle%29.md)
  Layers a shape that you specify in front of this view.
- [var backgroundMaterial: Material?](../environmentvalues/backgroundmaterial.md)
  The material underneath the current view.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](./containerbackground%28_,for%29.md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](./containerbackground%28for,alignment,content%29.md)
  Sets the container background of the enclosing container using a view.
- [struct ContainerBackgroundPlacement](../containerbackgroundplacement.md)
  The placement of a container background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/background(_:in:fillstyle:))*