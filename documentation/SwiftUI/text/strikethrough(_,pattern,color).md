# strikethrough(_:pattern:color:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Applies a strikethrough to the text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func strikethrough(_ isActive: Bool = true, pattern: Text.LineStyle.Pattern, color: Color? = nil) -> Text
```

## Return Value

Text with a line through its center.

## Parameters

- `isActive`: A Boolean value that indicates whether strikethrough is added. The default value is `true`.
- `pattern`: The pattern of the line.
- `color`: The color of the strikethrough. If `color` is `nil`, the strikethrough uses the default foreground color.

## See Also

### Styling the view’s text
- [func foregroundStyle<S>(S) -> Text](./foregroundstyle%28_%29.md)
  Sets the style of the text displayed by this view.
- [func bold() -> Text](./bold%28%29.md)
  Applies a bold or emphasized treatment to the fonts of the text.
- [func bold(Bool) -> Text](./bold%28_%29.md)
  Applies a bold font weight to the text.
- [func italic() -> Text](./italic%28%29.md)
  Applies italics to the text.
- [func italic(Bool) -> Text](./italic%28_%29.md)
  Applies italics to the text.
- [func strikethrough(Bool, color: Color?) -> Text](./strikethrough%28_,color%29.md)
  Applies a strikethrough to the text.
- [func underline(Bool, color: Color?) -> Text](./underline%28_,color%29.md)
  Applies an underline to the text.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text](./underline%28_,pattern,color%29.md)
  Applies an underline to the text.
- [func monospaced(Bool) -> Text](./monospaced%28_%29.md)
  Modifies the font of the text to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> Text](./monospaceddigit%28%29.md)
  Modifies the text view’s font to use fixed-width digits, while leaving other characters proportionally spaced.
- [func kerning(CGFloat) -> Text](./kerning%28_%29.md)
  Sets the spacing, or kerning, between characters.
- [func tracking(CGFloat) -> Text](./tracking%28_%29.md)
  Sets the tracking for the text.
- [func baselineOffset(CGFloat) -> Text](./baselineoffset%28_%29.md)
  Sets the vertical offset for the text relative to its baseline.
- [Text.Case](./case.md)
  A scheme for transforming the capitalization of characters within text.
- [struct DateStyle](./datestyle.md)
  A predefined style used to display a `Date`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/strikethrough(_:pattern:color:))*