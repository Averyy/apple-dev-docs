# tracking(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the tracking for the text.

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
func tracking(_ tracking: CGFloat) -> Text
```

#### Return Value

Text with the specified amount of tracking.

#### Discussion

Tracking adds space, measured in points, between the characters in the text view. A positive value increases the spacing between characters, while a negative value brings the characters closer together.

```swift
VStack(alignment: .leading) {
    Text("ABCDEF").tracking(-3)
    Text("ABCDEF")
    Text("ABCDEF").tracking(3)
}
```

The code above uses an unusually large amount of tracking to make it easy to see the effect.

![Three text views showing character groups with progressively](https://docs-assets.developer.apple.com/published/34e91c37a0c8ae95ca44b891a26e0797/SwiftUI-Text-tracking%402x.png)

The effect of tracking resembles that of the [`kerning(_:)`](text/kerning(_:).md) modifier, but adds or removes trailing whitespace, rather than changing character offsets. Also, using any nonzero amount of tracking disables nonessential ligatures, whereas kerning attempts to maintain ligatures.

> ❗ **Important**: If you add both the [`tracking(_:)`](text/tracking(_:).md) and [`kerning(_:)`](text/kerning(_:).md) modifiers to a view, the view applies the tracking and ignores the kerning.

## Parameters

- `tracking`: The amount of additional space, in points, that   the view should add to each character cluster after layout. Value of    sets the tracking to the system default value.

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
- [func baselineOffset(CGFloat) -> Text](text/baselineoffset(_:).md)
  Sets the vertical offset for the text relative to its baseline.
- [Text.Case](text/case.md)
  A scheme for transforming the capitalization of characters within text.
- [struct DateStyle](text/datestyle.md)
  A predefined style used to display a `Date`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/tracking(_:))*