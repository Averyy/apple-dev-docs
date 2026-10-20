# CTParagraphStyleSpecifier.tabStops

**Framework**: Core Text  
**Kind**: case  
**Role**: Case

The text tab objects, sorted by location, that define the tab stops for the paragraph style.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case tabStops
```

```c
kCTParagraphStyleSpecifierTabStops
```

#### Discussion

Type: An array of [`CTTextTab`](../cttexttab.md) objects. Default value: 12 left-aligned tabs, spaced by `28.0` points. Affects: [`CTFramesetter`](../ctframesetter.md) and [`CTTypesetter`](../cttypesetter.md).

## See Also

### Constants
- [CTParagraphStyleSpecifier.alignment](./alignment.md)
  The text alignment.
- [CTParagraphStyleSpecifier.firstLineHeadIndent](./firstlineheadindent.md)
  The distance, in points, from the leading margin of a frame to the beginning of the paragraph’s first line.
- [CTParagraphStyleSpecifier.headIndent](./headindent.md)
  The distance, in points, from the leading margin of a text container to the beginning of lines other than the first.
- [CTParagraphStyleSpecifier.tailIndent](./tailindent.md)
  The distance, in points, from the margin of a frame to the end of lines.
- [CTParagraphStyleSpecifier.defaultTabInterval](./defaulttabinterval.md)
  The document-wide default tab interval.
- [CTParagraphStyleSpecifier.lineBreakMode](./linebreakmode.md)
  The mode that should be used to break lines when laying out the paragraph’s text.
- [CTParagraphStyleSpecifier.lineHeightMultiple](./lineheightmultiple.md)
  The line height multiple.
- [CTParagraphStyleSpecifier.maximumLineHeight](./maximumlineheight.md)
  The maximum height that any line in the frame will occupy, regardless of the font size or size of any attached graphic.
- [CTParagraphStyleSpecifier.minimumLineHeight](./minimumlineheight.md)
  The minimum height that any line in the frame will occupy, regardless of the font size or size of any attached graphic.
- [CTParagraphStyleSpecifier.lineSpacing](./linespacing.md)
  The space in points added between lines within the paragraph (commonly known as leading).
- [CTParagraphStyleSpecifier.paragraphSpacing](./paragraphspacing.md)
  The space added at the end of the paragraph to separate it from the following paragraph.
- [CTParagraphStyleSpecifier.paragraphSpacingBefore](./paragraphspacingbefore.md)
  The distance between the paragraph’s top and the beginning of its text content.
- [CTParagraphStyleSpecifier.baseWritingDirection](./basewritingdirection.md)
  The base writing direction of the lines.
- [CTParagraphStyleSpecifier.maximumLineSpacing](./maximumlinespacing.md)
  The maximum space in points between lines within the paragraph (commonly known as leading).
- [CTParagraphStyleSpecifier.minimumLineSpacing](./minimumlinespacing.md)
  The minimum space in points between lines within the paragraph (commonly known as leading).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/tabstops)*