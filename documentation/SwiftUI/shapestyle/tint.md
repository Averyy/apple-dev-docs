# tint

**Framework**: SwiftUI  
**Kind**: property

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
static var tint: TintShapeStyle { get }
```

#### Discussion

You can set the tint color with the `tint(_:)` modifier. If no explicit tint is set, the tint is derived from the app’s accent color.

## See Also

- [static var foreground: ForegroundStyle](shapestyle/foreground.md)
  The foreground style in the current context.
- [static var background: BackgroundStyle](shapestyle/background.md)
  The background style in the current context.
- [static var selection: SelectionShapeStyle](shapestyle/selection.md)
  A style used to visually indicate selection following platform conventional colors and behaviors.
- [static var separator: SeparatorShapeStyle](shapestyle/separator.md)
  A style appropriate for foreground separator or border lines.
- [static var placeholder: PlaceholderTextShapeStyle](shapestyle/placeholder.md)
  A style appropriate for placeholder text.
- [static var link: LinkShapeStyle](shapestyle/link.md)
  A style appropriate for links.
- [static var fill: FillShapeStyle](shapestyle/fill.md)
  An overlay fill style for filling shapes.
- [static var windowBackground: WindowBackgroundShapeStyle](shapestyle/windowbackground.md)
  A style appropriate for elements that should match the background of their containing window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/tint)*