# drawingGroup(opaque:colorMode:)

**Framework**: Swiftui  
**Kind**: method

Composites this view’s contents into an offscreen image before final display.

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
func drawingGroup(opaque: Bool = false, colorMode: ColorRenderingMode = .nonLinear) -> some View
```

#### Return Value

A view that composites this view’s contents into an offscreen image before display.

#### Discussion

The `drawingGroup(opaque:colorMode:)` modifier flattens a subtree of views into a single view before rendering it.

In the example below, the contents of the view are composited to a single bitmap; the bitmap is then displayed in place of the view:

```swift
VStack {
    ZStack {
        Text("DrawingGroup")
            .foregroundColor(.black)
            .padding(20)
            .background(Color.red)
        Text("DrawingGroup")
            .blur(radius: 2)
    }
    .font(.largeTitle)
    .compositingGroup()
    .opacity(1.0)
}
 .background(Color.white)
 .drawingGroup()
```

> **Note**: Views backed by native platform views may not render into the image. Instead, they log a warning and display a placeholder image to highlight the error.

![A screenshot showing the effects on several stacks configured as a](https://docs-assets.developer.apple.com/published/c81675b1f1b78f79e131cdabc7d7a89a/SwiftUI-View-drawingGroup%402x.png)

## Parameters

- `opaque`: A Boolean value that indicates whether the image is opaque.   The default is  ; if set to  , the alpha channel of the   image must be  .
- `colorMode`: One of the working color space and storage formats   defined in  . The default is   .

## See Also

- [func blendMode(BlendMode) -> some View](view/blendmode(_:).md)
  Sets the blend mode for compositing this view with overlapping views.
- [func compositingGroup() -> some View](view/compositinggroup.md)
  Wraps this view in a compositing group.
- [enum BlendMode](blendmode.md)
  Modes for compositing a view with overlapping content.
- [enum ColorRenderingMode](colorrenderingmode.md)
  The set of possible working color spaces for color-compositing operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/drawinggroup(opaque:colormode:))*