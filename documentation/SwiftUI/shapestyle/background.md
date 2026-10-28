# background

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The background style in the current context.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@export(implementation)
static var background: BackgroundStyle { get }
```

Available when `Self` is `BackgroundStyle`.

## Discussion

Access this value to get the style SwiftUI uses for the background in the current context. The specific color that SwiftUI renders depends on factors like the platform and whether the user has turned on Dark Mode.

For information about how to use shape styles, see [`ShapeStyle`](../shapestyle.md).

## See Also

### Semantic styles
- [static var foreground: ForegroundStyle](./foreground.md)
  The foreground style in the current context.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/background)*