# tint

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A style that reflects the current tint color.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@export(implementation)
static var tint: TintShapeStyle { get }
```

Available when `Self` is `TintShapeStyle`.

#### Discussion

You can set the tint color with the `tint(_:)` modifier. If no explicit tint is set, the tint is derived from the app’s accent color.

## See Also

### Semantic styles
- [static var foreground: ForegroundStyle](./foreground.md)
  The foreground style in the current context.
- [static var background: BackgroundStyle](./background.md)
  The background style in the current context.
- [static var selection: SelectionShapeStyle](./selection.md)
  A style used to visually indicate selection following platform conventional colors and behaviors.
- [static var separator: SeparatorShapeStyle](./separator.md)
  A style appropriate for foreground separator or border lines.
- [static var placeholder: PlaceholderTextShapeStyle](./placeholder.md)
  A style appropriate for placeholder text.
- [static var link: LinkShapeStyle](./link.md)
  A style appropriate for links.
- [static var fill: FillShapeStyle](./fill.md)
  An overlay fill style for filling shapes.
- [static var windowBackground: WindowBackgroundShapeStyle](./windowbackground.md)
  A style appropriate for elements that should match the background of their containing window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/tint)*