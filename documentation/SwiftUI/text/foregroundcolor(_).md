# foregroundColor(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the color of the text displayed by this view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: foregroundStyle(_:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: foregroundStyle(_:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: foregroundStyle(_:))
- macOS 10.15+ - Deprecated in 27.2 (renamed: foregroundStyle(_:))
- tvOS 13.0+ - Deprecated in 27.2 (renamed: foregroundStyle(_:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: foregroundStyle(_:))
- watchOS 6.0+ - Deprecated in 27.2 (renamed: foregroundStyle(_:))

> **Deprecated**: Use [`foregroundStyle(_:)`](./foregroundstyle%28_%29.md) instead.

## Declaration

```swift
nonisolated
func foregroundColor(_ color: Color?) -> Text
```

## Return Value

A text view that uses the color value you supply.

## Discussion

Use this method to change the color of the text rendered by a text view.

For example, you can display the names of the colors red, green, and blue in their respective colors:

```swift
HStack {
    Text("Red").foregroundColor(.red)
    Text("Green").foregroundColor(.green)
    Text("Blue").foregroundColor(.blue)
}
```

![Three text views arranged horizontally, each containing](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-Text-foregroundColor@2x.png)

## Parameters

- `color`: The color to use when displaying this text.

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
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text](./strikethrough%28_,pattern,color%29.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/foregroundcolor(_:))*