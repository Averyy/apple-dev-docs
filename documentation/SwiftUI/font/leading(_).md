# leading(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adjusts the line spacing of a font.

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
func leading(_ leading: Font.Leading) -> Font
```

#### Return Value

A modified font that uses the specified line spacing, or the original font if it doesn’t support line spacing adjustments.

#### Discussion

You can change a font’s line spacing while maintaining other characteristics of the font by applying this modifier. For example, you can decrease spacing of the [`body`](./body.md) font by applying the [`Font.Leading.tight`](./leading/tight.md) value to it:

```swift
let myFont = Font.body.leading(.tight)
```

The availability of leading adjustments depends on the font. For some fonts, the modifier has no effect and returns the original font.

## Parameters

- `leading`: The line spacing adjustment to apply.

## See Also

### Styling a font
- [func bold() -> Font](./bold%28%29.md)
  Adds bold or emphasized styling to the font.
- [func italic() -> Font](./italic%28%29.md)
  Adds italics to the font.
- [func monospaced() -> Font](./monospaced%28%29.md)
  Returns a fixed-width font from the same family as the base font.
- [func monospacedDigit() -> Font](./monospaceddigit%28%29.md)
  Returns a modified font that uses fixed-width digits, while leaving other characters proportionally spaced.
- [func smallCaps() -> Font](./smallcaps%28%29.md)
  Adjusts the font to enable all small capitals.
- [func lowercaseSmallCaps() -> Font](./lowercasesmallcaps%28%29.md)
  Adjusts the font to enable lowercase small capitals.
- [func uppercaseSmallCaps() -> Font](./uppercasesmallcaps%28%29.md)
  Adjusts the font to enable uppercase small capitals.
- [func weight(Font.Weight) -> Font](./weight%28_%29.md)
  Sets the weight of the font.
- [func width(Font.Width) -> Font](./width%28_%29.md)
  Sets the width of the font.
- [struct Width](./width.md)
  A width to use for fonts that have multiple widths.
- [Font.Leading](./leading.md)
  A line spacing adjustment that you can apply to a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/leading(_:))*