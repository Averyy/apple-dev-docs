# Font.Leading

**Framework**: SwiftUI  
**Kind**: enum

A line spacing adjustment that you can apply to a font.

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
enum Leading
```

#### Overview

Apply one of the `Leading` values to a font using the [`leading(_:)`](font/leading(_:).md) method to increase or decrease the line spacing.

## Topics

### Getting leading line spacing options
- [Font.Leading.standard](font/leading/standard.md)
  The font’s default line spacing.
- [Font.Leading.loose](font/leading/loose.md)
  Increased line spacing.
- [Font.Leading.tight](font/leading/tight.md)
  Reduced line spacing.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
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
- [struct Width](font/width.md)
  A width to use for fonts that have multiple widths.
- [func leading(Font.Leading) -> Font](font/leading(_:).md)
  Adjusts the line spacing of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/leading)*