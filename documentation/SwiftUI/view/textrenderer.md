# textRenderer(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a new view such that any text views within it will use `renderer` to draw themselves.

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
nonisolated
func textRenderer<T>(_ renderer: T) -> some View where T : TextRenderer
```

#### Return Value

A new view that will use `renderer` to draw its text views.

## Parameters

- `renderer`: The renderer value.

## See Also

- [Creating visual effects with SwiftUI](creating-visual-effects-with-swiftui.md)
  Add scroll effects, rich color treatments, custom transitions, and advanced effects using shaders and a text renderer.
- [protocol TextAttribute](textattribute.md)
  A value that you can attach to text views and that text renderers can query.
- [protocol TextRenderer](textrenderer.md)
  A value that can replace the default text view rendering behavior.
- [struct TextProxy](textproxy.md)
  A proxy for a text view that custom text renderers use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/textrenderer(_:))*