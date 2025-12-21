# blendMode(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the blend mode for compositing this view with overlapping views.

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
func blendMode(_ blendMode: BlendMode) -> some View
```

#### Return Value

A view that applies `blendMode` to this view.

#### Discussion

Use `blendMode(_:)` to combine overlapping views and use a different visual effect to produce the result. The [`BlendMode`](blendmode.md) enumeration defines many possible effects.

In the example below, the two overlapping rectangles have a [`BlendMode.colorBurn`](blendmode/colorburn.md) effect applied, which effectively removes the non-overlapping portion of the second image:

```swift
HStack {
    Color.yellow.frame(width: 50, height: 50, alignment: .center)

    Color.red.frame(width: 50, height: 50, alignment: .center)
        .rotationEffect(.degrees(45))
        .padding(-20)
        .blendMode(.colorBurn)
}
```

![Two overlapping rectangles showing the effect of the blend mode view](https://docs-assets.developer.apple.com/published/c895f1b7ba32ddd9875ab5476003803e/SwiftUI-blendMode%402x.png)

## Parameters

- `blendMode`: The   for compositing this view.

## See Also

- [func compositingGroup() -> some View](view/compositinggroup.md)
  Wraps this view in a compositing group.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](view/drawinggroup(opaque:colormode:).md)
  Composites this view’s contents into an offscreen image before final display.
- [enum BlendMode](blendmode.md)
  Modes for compositing a view with overlapping content.
- [enum ColorRenderingMode](colorrenderingmode.md)
  The set of possible working color spaces for color-compositing operations.
- [protocol CompositorContent](compositorcontent.md)
- [struct CompositorContentBuilder](compositorcontentbuilder.md)
  A result builder for composing a collection of [`CompositorContent`](compositorcontent.md) elements.
- [struct AnyCompositorContent](anycompositorcontent.md)
  Type erased compositor content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/blendmode(_:))*