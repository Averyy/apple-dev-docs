# foregroundStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style of the text displayed by this view.

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
nonisolated
func foregroundStyle<S>(_ style: S) -> Text where S : ShapeStyle
```

#### Return Value

A text view that uses the color value you supply.

#### Discussion

Use this method to change the rendering style of the text rendered by a text view.

For example, you can display the names of the colors red, green, and blue in their respective colors:

```swift
HStack {
    Text("Red").foregroundStyle(.red)
    Text("Green").foregroundStyle(.green)
    Text("Blue").foregroundStyle(.blue)
}
```

![Three text views arranged horizontally, each containing](https://docs-assets.developer.apple.com/published/31654f673e42a4a453b46dbad7d32b61/SwiftUI-Text-foregroundColor%402x.png)

## Parameters

- `style`: The style to use when displaying this text.

## See Also

- [func bold() -> Text](text/bold.md)
  Applies a bold or emphasized treatment to the fonts of the text.
- [func bold(Bool) -> Text](text/bold(_:).md)
  Applies a bold font weight to the text.
- [func italic() -> Text](text/italic.md)
  Applies italics to the text.
- [func italic(Bool) -> Text](text/italic(_:).md)
  Applies italics to the text.
- [func strikethrough(Bool, color: Color?) -> Text](text/strikethrough(_:color:).md)
  Applies a strikethrough to the text.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text](text/strikethrough(_:pattern:color:).md)
  Applies a strikethrough to the text.
- [func underline(Bool, color: Color?) -> Text](text/underline(_:color:).md)
  Applies an underline to the text.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text](text/underline(_:pattern:color:).md)
  Applies an underline to the text.
- [func monospaced(Bool) -> Text](text/monospaced(_:).md)
  Modifies the font of the text to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> Text](text/monospaceddigit.md)
  Modifies the text view’s font to use fixed-width digits, while leaving other characters proportionally spaced.
- [func kerning(CGFloat) -> Text](text/kerning(_:).md)
  Sets the spacing, or kerning, between characters.
- [func tracking(CGFloat) -> Text](text/tracking(_:).md)
  Sets the tracking for the text.
- [func baselineOffset(CGFloat) -> Text](text/baselineoffset(_:).md)
  Sets the vertical offset for the text relative to its baseline.
- [Text.Case](text/case.md)
  A scheme for transforming the capitalization of characters within text.
- [struct DateStyle](text/datestyle.md)
  A predefined style used to display a `Date`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/foregroundstyle(_:))*