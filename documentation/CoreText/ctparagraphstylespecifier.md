# CTParagraphStyleSpecifier

**Framework**: Core Text  
**Kind**: enum

Constants used to query and modify a paragraph style object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CTParagraphStyleSpecifier
```

#### Overview

Each specifier has a type and a default value associated with it. The type must always be observed when setting or fetching the value from the `CTParagraphStyle` object. In addition, some specifiers affect the behavior of both the framesetter and the typesetter, and others affect the behavior of only the framesetter, as noted in the constant descriptions.

## Topics

### Constants
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
- [CTParagraphStyleSpecifier.lineSpacing](ctparagraphstylespecifier/linespacing.md)
  The space in points added between lines within the paragraph (commonly known as leading).
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
- [CTParagraphStyleSpecifier.lineSpacingAdjustment](ctparagraphstylespecifier/linespacingadjustment.md)
  The space in points added between lines within the paragraph (commonly known as leading).
- [CTParagraphStyleSpecifier.count](ctparagraphstylespecifier/count.md)
  The number of style specifiers.
### Enumeration Cases
- [CTParagraphStyleSpecifier.lineBoundsOptions](ctparagraphstylespecifier/lineboundsoptions.md)
  Options that control the alignment of the line edges with the leading and trailing margins.
### Initializers
- [init?(rawValue: UInt32)](ctparagraphstylespecifier/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum CTTextAlignment](cttextalignment.md)
  Constants that specify text alignment.
- [enum CTLineBreakMode](ctlinebreakmode.md)
  These constants specify what happens when a line is too long for its frame.
- [enum CTWritingDirection](ctwritingdirection.md)
  These constants specify the writing direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier)*