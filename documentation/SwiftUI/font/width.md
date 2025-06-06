# Font.Width

**Framework**: SwiftUI  
**Kind**: struct

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
- [static let compressed: Font.Width](font/width/compressed.md)
- [static let condensed: Font.Width](font/width/condensed.md)
- [static let expanded: Font.Width](font/width/expanded.md)
- [static let standard: Font.Width](font/width/standard.md)
### Creating an explicit font width
- [init(CGFloat)](font/width/init(_:).md)
### Accessing the width’s value
- [var value: CGFloat](font/width/value.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func bold() -> Font](font/bold.md)
  Adds bold styling to the font.
- [func italic() -> Font](font/italic.md)
  Adds italics to the font.
- [func monospaced() -> Font](font/monospaced.md)
  Returns a fixed-width font from the same family as the base font.
- [func monospacedDigit() -> Font](font/monospaceddigit.md)
  Returns a modified font that uses fixed-width digits, while leaving other characters proportionally spaced.
- [func smallCaps() -> Font](font/smallcaps.md)
  Adjusts the font to enable all small capitals.
- [func lowercaseSmallCaps() -> Font](font/lowercasesmallcaps.md)
  Adjusts the font to enable lowercase small capitals.
- [func uppercaseSmallCaps() -> Font](font/uppercasesmallcaps.md)
  Adjusts the font to enable uppercase small capitals.
- [func weight(Font.Weight) -> Font](font/weight(_:).md)
  Sets the weight of the font.
- [func width(Font.Width) -> Font](font/width(_:).md)
  Sets the width of the font.
- [func leading(Font.Leading) -> Font](font/leading(_:).md)
  Adjusts the line spacing of a font.
- [Font.Leading](font/leading.md)
  A line spacing adjustment that you can apply to a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/width)*