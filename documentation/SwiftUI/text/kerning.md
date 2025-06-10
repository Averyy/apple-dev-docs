# kerning(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the spacing, or kerning, between characters.

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
func kerning(_ kerning: CGFloat) -> Text
```

#### Return Value

Text with the specified amount of kerning.

#### Discussion

Kerning defines the offset, in points, that a text view should shift characters from the default spacing. Use positive kerning to widen the spacing between characters. Use negative kerning to tighten the spacing between characters.

```swift
VStack(alignment: .leading) {
    Text("ABCDEF").kerning(-3)
    Text("ABCDEF")
    Text("ABCDEF").kerning(3)
}
```

The last character in the first case, which uses negative kerning, experiences cropping because the kerning affects the trailing edge of the text view as well.

![Three text views showing character groups, with progressively](https://docs-assets.developer.apple.com/published/8a1af1e199d6c4f2dabecc906d0b2b5b/SwiftUI-Text-kerning-1%402x.png)

Kerning attempts to maintain ligatures. For example, the Hoefler Text font uses a ligature for the letter combination , as in the word , shown here with a small negative and a small positive kerning:

![Two text views showing the word raffle in the Hoefler Text font, the](https://docs-assets.developer.apple.com/published/e150d2faa87f2502f78816d52bf23e9c/SwiftUI-Text-kerning-2%402x.png)

The  letter combination keeps a constant shape as the other letters move together or apart. Beyond a certain point in either direction, however, kerning does disable nonessential ligatures.

![Two text views showing the word raffle in the Hoefler Text font, the](https://docs-assets.developer.apple.com/published/12c156ffa170a7b5e73e033db44cf721/SwiftUI-Text-kerning-3%402x.png)

> ❗ **Important**: If you add both the [`tracking(_:)`](text/tracking(_:).md) and [`kerning(_:)`](text/kerning(_:).md) modifiers to a view, the view applies the tracking and ignores the kerning.

## Parameters

- `kerning`: The spacing to use between individual characters in   this text. Value of   sets the kerning to the system default value.

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
- [func tracking(CGFloat) -> Text](text/tracking(_:).md)
  Sets the tracking for the text.
- [func baselineOffset(CGFloat) -> Text](text/baselineoffset(_:).md)
  Sets the vertical offset for the text relative to its baseline.
- [Text.Case](text/case.md)
  A scheme for transforming the capitalization of characters within text.
- [struct DateStyle](text/datestyle.md)
  A predefined style used to display a `Date`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/kerning(_:))*