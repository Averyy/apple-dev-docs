# TextProxy

**Framework**: SwiftUI  
**Kind**: struct

A proxy for a text view that custom text renderers use.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct TextProxy
```

## Topics

### Instance Methods
- [func sizeThatFits(ProposedViewSize) -> CGSize](textproxy/sizethatfits(_:).md)
  Returns the space needed by the text view, for a proposed size.

## See Also

- [Creating visual effects with SwiftUI](creating-visual-effects-with-swiftui.md)
  Add scroll effects, rich color treatments, custom transitions, and advanced effects using shaders and a text renderer.
- [protocol TextAttribute](textattribute.md)
  A value that you can attach to text views and that text renderers can query.
- [func textRenderer<T>(T) -> some View](view/textrenderer(_:).md)
  Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [protocol TextRenderer](textrenderer.md)
  A value that can replace the default text view rendering behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textproxy)*