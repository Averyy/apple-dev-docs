# Text.LineStyle

**Framework**: SwiftUI  
**Kind**: struct

Description of the style used to draw the line for `StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct LineStyle
```

#### Overview

Use this type to specify `underlineStyle` and `strikethroughStyle` SwiftUI attributes of an `AttributedString`.

## Topics

### Getting text line styles
- [static let single: Text.LineStyle](text/linestyle/single.md)
  Draw a single solid line.
### Creating a text line style
- [init?(nsUnderlineStyle: NSUnderlineStyle)](text/linestyle/init(nsunderlinestyle:).md)
  Creates a `Text.LineStyle` from `NSUnderlineStyle`.
- [init(pattern: Text.LineStyle.Pattern, color: Color?)](text/linestyle/init(pattern:color:).md)
  Creates a line style.
- [Text.LineStyle.Pattern](text/linestyle/pattern.md)
  The pattern, that the line has.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/linestyle)*