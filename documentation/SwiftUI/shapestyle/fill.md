# fill

**Framework**: SwiftUI  
**Kind**: property

An overlay fill style for filling shapes.

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
static var fill: FillShapeStyle { get }
```

#### Discussion

This shape style is appropriate for items situated on top of an existing background color. It incorporates transparency to allow the background color to show through.

Use the primary version of this style to fill thin or small shapes, such as the track of a slider on iOS. Use the secondary version of this style to fill medium-size shapes, such as the background of a switch on iOS. Use the tertiary version of this style to fill large shapes, such as input fields, search bars, or buttons on iOS. Use the quaternary version of this style to fill large areas that contain complex content, such as an expanded table cell on iOS.

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
- [static var windowBackground: WindowBackgroundShapeStyle](shapestyle/windowbackground.md)
  A style appropriate for elements that should match the background of their containing window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/fill)*