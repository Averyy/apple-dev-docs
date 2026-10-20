# Text.DateStyle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A predefined style used to display a `Date`.

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
struct DateStyle
```

## Topics

### Getting text date styles
- [static let date: Text.DateStyle](./datestyle/date.md)
  A style displaying a date.
- [static let offset: Text.DateStyle](./datestyle/offset.md)
  A style displaying a date as offset from now.
- [static let relative: Text.DateStyle](./datestyle/relative.md)
  A style displaying a date as relative to now.
- [static let time: Text.DateStyle](./datestyle/time.md)
  A style displaying only the time component for a date.
- [static let timer: Text.DateStyle](./datestyle/timer.md)
  A style displaying a date as timer counting from now.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/datestyle)*