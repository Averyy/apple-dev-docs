# TextAttribute

**Framework**: SwiftUI  
**Kind**: protocol

A value that you can attach to text views and that text renderers can query.

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
protocol TextAttribute : Hashable
```

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Creating visual effects with SwiftUI](creating-visual-effects-with-swiftui.md)
  Add scroll effects, rich color treatments, custom transitions, and advanced effects using shaders and a text renderer.
- [func textRenderer<T>(T) -> some View](view/textrenderer(_:).md)
  Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [protocol TextRenderer](textrenderer.md)
  A value that can replace the default text view rendering behavior.
- [struct TextProxy](textproxy.md)
  A proxy for a text view that custom text renderers use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textattribute)*