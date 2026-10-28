# bold()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds bold or emphasized styling to the font.

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
func bold() -> Font
```

## Discussion

For fonts created from text styles, it could mean applying emphasized styling, which does not necessarily mean the bold weight specifically, so this modifier is not to be confused with [`weight(_:)`](./weight%28_%29.md).

For example:

```swift
Font.body.bold()
```

will most likely get you the emphasized version of body text style, which is often in [`semibold`](./weight/semibold.md) weight. While

```swift
Font.body.weight(.bold)
```

will specifically get you the body text style font in the [`bold`](./weight/bold.md) weight.

## See Also

### Styling a font
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
- [func leading(Font.Leading) -> Font](./leading%28_%29.md)
  Adjusts the line spacing of a font.
- [Font.Leading](./leading.md)
  A line spacing adjustment that you can apply to a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/bold())*