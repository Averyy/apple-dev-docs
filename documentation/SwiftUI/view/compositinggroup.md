# compositingGroup()

**Framework**: SwiftUI  
**Kind**: method

Wraps this view in a compositing group.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func compositingGroup() -> some View
```

#### Return Value

A view that wraps this view in a compositing group.

#### Discussion

A compositing group makes compositing effects in this view’s ancestor views, such as opacity and the blend mode, take effect before this view is rendered.

Use `compositingGroup()` to apply effects to a parent view before applying effects to this view.

In the example below the `compositingGroup()` modifier separates the application of effects into stages. It applies the [`opacity(_:)`](view/opacity(_:).md) effect to the VStack before the `blur(radius:)` effect is applied to the views inside the enclosed [`ZStack`](zstack.md). This limits the scope of the opacity change to the outermost view.

```swift
VStack {
    ZStack {
        Text("CompositingGroup")
            .foregroundColor(.black)
            .padding(20)
            .background(Color.red)
        Text("CompositingGroup")
            .blur(radius: 2)
    }
    .font(.largeTitle)
    .compositingGroup()
    .opacity(0.9)
}
```

![A view showing the effect of the compositingGroup modifier in applying](https://docs-assets.developer.apple.com/published/102ab31bc2decb6b1f250dfb49c77c62/SwiftUI-View-compositingGroup%402x.png)

## See Also

- [func blendMode(BlendMode) -> some View](view/blendmode(_:).md)
  Sets the blend mode for compositing this view with overlapping views.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](view/drawinggroup(opaque:colormode:).md)
  Composites this view’s contents into an offscreen image before final display.
- [enum BlendMode](blendmode.md)
  Modes for compositing a view with overlapping content.
- [enum ColorRenderingMode](colorrenderingmode.md)
  The set of possible working color spaces for color-compositing operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/compositinggroup())*