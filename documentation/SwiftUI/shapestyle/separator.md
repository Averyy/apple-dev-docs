# separator

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A style appropriate for foreground separator or border lines.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 10.15+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@export(implementation)
static var separator: SeparatorShapeStyle { get }
```

Available when `Self` is `SeparatorShapeStyle`.

## Discussion

For information about how to use shape styles, see [`ShapeStyle`](../shapestyle.md).

## See Also

### Semantic styles
- [static var foreground: ForegroundStyle](./foreground.md)
  The foreground style in the current context.
- [static var background: BackgroundStyle](./background.md)
  The background style in the current context.
- [static var selection: SelectionShapeStyle](./selection.md)
  A style used to visually indicate selection following platform conventional colors and behaviors.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/separator)*