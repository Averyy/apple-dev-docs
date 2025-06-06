# windowBackground

**Framework**: SwiftUI  
**Kind**: property

A style appropriate for elements that should match the background of their containing window.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
static var windowBackground: WindowBackgroundShapeStyle { get }
```

#### Discussion

On macOS, this has a unique appearance compared to the default `ShapeStyle.background`. It matches the default background of a window: a wallpaper-tinted light gray in the light appearance and a wallpaper-tinted dark gray in the dark appearance.

On visionOS, the default glass window background can only be created using `glassBackgroundEffect`.

For information about how to use shape styles, see [`ShapeStyle`](shapestyle.md).

## See Also

- [static var foreground: ForegroundStyle](shapestyle/foreground.md)
  The foreground style in the current context.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/windowbackground)*