# TextRenderer

**Framework**: SwiftUI  
**Kind**: protocol

A value that can replace the default text view rendering behavior.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
protocol TextRenderer : Animatable
```

## Topics

### Instance Properties
- [var displayPadding: EdgeInsets](textrenderer/displaypadding.md)
  Returns the size of the extra padding added to any drawing layer used to rasterize the text. For example when drawing the text with a shadow this may be used to extend the drawing bounds to avoid clipping the shadow.
### Instance Methods
- [func draw(layout: Text.Layout, in: inout GraphicsContext)](textrenderer/draw(layout:in:).md)
  Draws `layout` into `ctx`.
- [func sizeThatFits(proposal: ProposedViewSize, text: TextProxy) -> CGSize](textrenderer/sizethatfits(proposal:text:).md)
  Returns the size of the text in `proposal`. The provided `text` proxy value may be used to query the sizing behavior of the underlying text layout.

## Relationships

### Inherits From
- [Animatable](animatable.md)

## See Also

- [Creating visual effects with SwiftUI](creating-visual-effects-with-swiftui.md)
  Add scroll effects, rich color treatments, custom transitions, and advanced effects using shaders and a text renderer.
- [protocol TextAttribute](textattribute.md)
  A value that you can attach to text views and that text renderers can query.
- [func textRenderer<T>(T) -> some View](view/textrenderer(_:).md)
  Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [struct TextProxy](textproxy.md)
  A proxy for a text view that custom text renderers use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textrenderer)*