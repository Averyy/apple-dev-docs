# foreground

**Framework**: SwiftUI  
**Kind**: property

The foreground style in the current context.

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
static var foreground: ForegroundStyle { get }
```

#### Discussion

Access this value to get the style SwiftUI uses for foreground elements, like text, symbols, and shapes, in the current context. Use the [`foregroundStyle(_:)`](view/foregroundstyle(_:).md) modifier to set a new foreground style for a given view and its child views.

For information about how to use shape styles, see [`ShapeStyle`](shapestyle.md).

## See Also

- [static var background: BackgroundStyle](shapestyle/background.md)
  The background style in the current context.
- [static var selection: SelectionShapeStyle](shapestyle/selection.md)
  A style used to visually indicate selection following platform conventional colors and behaviors.
- [static var separator: SeparatorShapeStyle](shapestyle/separator.md)
  A style appropriate for foreground separator or border lines.
- [static var tint: TintShapeStyle](shapestyle/tint.md)
  A style that reflects the current tint color.
- [static var placeholder: PlaceholderTextShapeStyle](shapestyle/placeholder.md)
  A style appropriate for placeholder text.
- [static var link: LinkShapeStyle](shapestyle/link.md)
  A style appropriate for links.
- [static var fill: FillShapeStyle](shapestyle/fill.md)
  An overlay fill style for filling shapes.
- [static var windowBackground: WindowBackgroundShapeStyle](shapestyle/windowbackground.md)
  A style appropriate for elements that should match the background of their containing window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/foreground)*