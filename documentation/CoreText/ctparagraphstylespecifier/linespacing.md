# CTParagraphStyleSpecifier.lineSpacing

**Framework**: Core Text  
**Kind**: case

The space in points added between lines within the paragraph (commonly known as leading).

**Availability**:
- visionOS 1.0+

## Declaration

```swift
case lineSpacing
```

#### Discussion

Instead, use [`CTParagraphStyleSpecifier.maximumLineSpacing`](ctparagraphstylespecifier/maximumlinespacing.md), [`CTParagraphStyleSpecifier.minimumLineSpacing`](ctparagraphstylespecifier/minimumlinespacing.md), and [`CTParagraphStyleSpecifier.lineSpacingAdjustment`](ctparagraphstylespecifier/linespacingadjustment.md) to control space between lines. This value is always nonnegative. Type: [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct). Default value: `0.0`. Affects: [`CTFramesetter`](ctframesetter.md).

## See Also

- [CTParagraphStyleSpecifier.alignment](ctparagraphstylespecifier/alignment.md)
  The text alignment.
- [CTParagraphStyleSpecifier.firstLineHeadIndent](ctparagraphstylespecifier/firstlineheadindent.md)
  The distance, in points, from the leading margin of a frame to the beginning of the paragraph’s first line.
- [CTParagraphStyleSpecifier.headIndent](ctparagraphstylespecifier/headindent.md)
  The distance, in points, from the leading margin of a text container to the beginning of lines other than the first.
- [CTParagraphStyleSpecifier.tailIndent](ctparagraphstylespecifier/tailindent.md)
  The distance, in points, from the margin of a frame to the end of lines.
- [CTParagraphStyleSpecifier.tabStops](ctparagraphstylespecifier/tabstops.md)
  The text tab objects, sorted by location, that define the tab stops for the paragraph style.
- [CTParagraphStyleSpecifier.defaultTabInterval](ctparagraphstylespecifier/defaulttabinterval.md)
  The document-wide default tab interval.
- [CTParagraphStyleSpecifier.lineBreakMode](ctparagraphstylespecifier/linebreakmode.md)
  The mode that should be used to break lines when laying out the paragraph’s text.
- [CTParagraphStyleSpecifier.lineHeightMultiple](ctparagraphstylespecifier/lineheightmultiple.md)
  The line height multiple.
- [CTParagraphStyleSpecifier.maximumLineHeight](ctparagraphstylespecifier/maximumlineheight.md)
  The maximum height that any line in the frame will occupy, regardless of the font size or size of any attached graphic.
- [CTParagraphStyleSpecifier.minimumLineHeight](ctparagraphstylespecifier/minimumlineheight.md)
  The minimum height that any line in the frame will occupy, regardless of the font size or size of any attached graphic.
- [CTParagraphStyleSpecifier.paragraphSpacing](ctparagraphstylespecifier/paragraphspacing.md)
  The space added at the end of the paragraph to separate it from the following paragraph.
- [CTParagraphStyleSpecifier.paragraphSpacingBefore](ctparagraphstylespecifier/paragraphspacingbefore.md)
  The distance between the paragraph’s top and the beginning of its text content.
- [CTParagraphStyleSpecifier.baseWritingDirection](ctparagraphstylespecifier/basewritingdirection.md)
  The base writing direction of the lines.
- [CTParagraphStyleSpecifier.maximumLineSpacing](ctparagraphstylespecifier/maximumlinespacing.md)
  The maximum space in points between lines within the paragraph (commonly known as leading).
- [CTParagraphStyleSpecifier.minimumLineSpacing](ctparagraphstylespecifier/minimumlinespacing.md)
  The minimum space in points between lines within the paragraph (commonly known as leading).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/linespacing)*