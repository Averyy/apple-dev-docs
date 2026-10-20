# foreground

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

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
@export(implementation)
static var foreground: ForegroundStyle { get }
```

Available when `Self` is `ForegroundStyle`.

#### Discussion

Access this value to get the style SwiftUI uses for foreground elements, like text, symbols, and shapes, in the current context. Use the [`foregroundStyle(_:)`](../view/foregroundstyle%28_%29.md) modifier to set a new foreground style for a given view and its child views.

For information about how to use shape styles, see [`ShapeStyle`](../shapestyle.md).

## See Also

### Semantic styles
- [static var background: BackgroundStyle](./background.md)
  The background style in the current context.
- [static var selection: SelectionShapeStyle](./selection.md)
  A style used to visually indicate selection following platform conventional colors and behaviors.
- [static var separator: SeparatorShapeStyle](./separator.md)
  A style appropriate for foreground separator or border lines.
- [static var tint: TintShapeStyle](./tint.md)
  A style that reflects the current tint color.
- [static var placeholder: PlaceholderTextShapeStyle](./placeholder.md)
  A style appropriate for placeholder text.
- [static var link: LinkShapeStyle](./link.md)
  A style appropriate for links.
- [static var fill: FillShapeStyle](./fill.md)
  An overlay fill style for filling shapes.
- [static var windowBackground: WindowBackgroundShapeStyle](./windowbackground.md)
  A style appropriate for elements that should match the background of their containing window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/foreground)*