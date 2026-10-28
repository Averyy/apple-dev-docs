# CTParagraphStyleSpecifier.tailIndent

**Framework**: Core Text  
**Kind**: case  
**Role**: Case

The distance, in points, from the margin of a frame to the end of lines.

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
case tailIndent
```

```c
kCTParagraphStyleSpecifierTailIndent
```

## Discussion

If positive, this value is the distance from the leading margin (for example, the left margin in left-to-right text). If `0` or negative, it’s the distance from the trailing margin. Type: [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md). Default value: `0.0`. Affects: [`CTFramesetter`](../ctframesetter.md).

## See Also

### Constants
- [CTParagraphStyleSpecifier.alignment](./alignment.md)
  The text alignment.
- [CTParagraphStyleSpecifier.firstLineHeadIndent](./firstlineheadindent.md)
  The distance, in points, from the leading margin of a frame to the beginning of the paragraph’s first line.
- [CTParagraphStyleSpecifier.headIndent](./headindent.md)
  The distance, in points, from the leading margin of a text container to the beginning of lines other than the first.
- [CTParagraphStyleSpecifier.tabStops](./tabstops.md)
  The text tab objects, sorted by location, that define the tab stops for the paragraph style.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/tailindent)*