# Font.Width

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A width to use for fonts that have multiple widths.

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
struct Width
```

## Topics

### Getting standard font widths
- [static let compressed: Font.Width](./width/compressed.md)
- [static let condensed: Font.Width](./width/condensed.md)
- [static let expanded: Font.Width](./width/expanded.md)
- [static let standard: Font.Width](./width/standard.md)
### Creating an explicit font width
- [init(CGFloat)](./width/init%28_%29.md)
### Accessing the width’s value
- [var value: CGFloat](./width/value.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [func leading(Font.Leading) -> Font](./leading%28_%29.md)
  Adjusts the line spacing of a font.
- [Font.Leading](./leading.md)
  A line spacing adjustment that you can apply to a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/width)*