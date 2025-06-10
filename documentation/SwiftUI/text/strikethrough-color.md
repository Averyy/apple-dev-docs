# strikethrough(_:color:)

**Framework**: SwiftUI  
**Kind**: method

Applies a strikethrough to the text.

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
nonisolated
func strikethrough(_ isActive: Bool = true, color: Color? = nil) -> Text
```

#### Return Value

Text with a line through its center.

## Parameters

- `isActive`: A Boolean value that indicates whether the text has a   strikethrough applied.
- `color`: The color of the strikethrough. If   is  , the   strikethrough uses the default foreground color.

## See Also

- [func foregroundStyle<S>(S) -> Text](text/foregroundstyle(_:).md)
  Sets the style of the text displayed by this view.
- [func bold() -> Text](text/bold.md)
  Applies a bold or emphasized treatment to the fonts of the text.
- [func bold(Bool) -> Text](text/bold(_:).md)
  Applies a bold font weight to the text.
- [func italic() -> Text](text/italic.md)
  Applies italics to the text.
- [func italic(Bool) -> Text](text/italic(_:).md)
  Applies italics to the text.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/strikethrough(_:color:))*