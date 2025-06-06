# NSParagraphStyle

**Framework**: AppKit  
**Kind**: class

The paragraph or ruler attributes for an attributed string.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class NSParagraphStyle
```

#### Overview

An [`NSParagraphStyle`](nsparagraphstyle.md) object stores formatting information for a paragraph of text. The formatting information includes the amount of space between lines, indentations for lines of text, line heights, tab-stop positions, and more. Apply paragraph styles to the text of an attributed string by adding the [`paragraphStyle`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1527910-paragraphstyle) attribute and setting its value to an instance of this class. The text-rendering system uses the paragraph style information in an attributed string to lay out and render the text.

The [`NSParagraphStyle`](nsparagraphstyle.md) class manages an immutable set of style information, but you can create an [`NSMutableParagraphStyle`](nsmutableparagraphstyle.md) when you want to modify the style information before applying it to your text.

## Topics

### Creating a paragraph style
- [class var `default`: NSParagraphStyle](nsparagraphstyle/default.md)
  The default paragraph style.
### Accessing style information
- [var alignment: NSTextAlignment](nsparagraphstyle/alignment.md)
  The text alignment of the paragraph.
- [enum NSTextAlignment](nstextalignment.md)
  Constants that specify text alignment.
- [var firstLineHeadIndent: CGFloat](nsparagraphstyle/firstlineheadindent.md)
  The indentation of the first line of the paragraph.
- [var headIndent: CGFloat](nsparagraphstyle/headindent.md)
  The indentation of the paragraph’s lines other than the first.
- [var tailIndent: CGFloat](nsparagraphstyle/tailindent.md)
  The trailing indentation of the paragraph.
- [var lineHeightMultiple: CGFloat](nsparagraphstyle/lineheightmultiple.md)
  The line height multiple.
- [var maximumLineHeight: CGFloat](nsparagraphstyle/maximumlineheight.md)
  The paragraph’s maximum line height.
- [var minimumLineHeight: CGFloat](nsparagraphstyle/minimumlineheight.md)
  The paragraph’s minimum line height.
- [var lineSpacing: CGFloat](nsparagraphstyle/linespacing.md)
  The distance in points between the bottom of one line fragment and the top of the next.
- [var paragraphSpacing: CGFloat](nsparagraphstyle/paragraphspacing.md)
  Distance between the bottom of this paragraph and top of next.
- [var paragraphSpacingBefore: CGFloat](nsparagraphstyle/paragraphspacingbefore.md)
  The distance between the paragraph’s top and the beginning of its text content.
### Accessing tab information
- [var tabStops: [NSTextTab]](nsparagraphstyle/tabstops.md)
  The text tab objects that represent the paragraph’s tab stops.
- [NSParagraphStyle.TextTabType](nsparagraphstyle/texttabtype.md)
  Constants that specify the type of tab stop.
- [var defaultTabInterval: CGFloat](nsparagraphstyle/defaulttabinterval.md)
  The documentwide default tab interval.
### Getting text block and list information
- [var textBlocks: [NSTextBlock]](nsparagraphstyle/textblocks.md)
  The text blocks that contain the paragraph.
- [var textLists: [NSTextList]](nsparagraphstyle/textlists.md)
  The text lists that contain the paragraph.
### Getting line-break information
- [var lineBreakMode: NSLineBreakMode](nsparagraphstyle/linebreakmode.md)
  The mode for breaking lines in the paragraph that don’t fit within a container.
- [enum NSLineBreakMode](nslinebreakmode.md)
  Constants that specify what happens when a line is too long for a container.
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](nsparagraphstyle/linebreakstrategy-swift.property.md)
  The strategy for breaking lines while laying out paragraphs.
- [NSParagraphStyle.LineBreakStrategy](nsparagraphstyle/linebreakstrategy-swift.struct.md)
  Constants that specify how the text system breaks lines while laying out paragraphs.
- [var hyphenationFactor: Float](nsparagraphstyle/hyphenationfactor.md)
  The paragraph’s threshold for hyphenation.
- [var usesDefaultHyphenation: Bool](nsparagraphstyle/usesdefaulthyphenation.md)
  A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [var tighteningFactorForTruncation: Float](nsparagraphstyle/tighteningfactorfortruncation.md)
  The threshold for using tightening as an alternative to truncation.
- [var allowsDefaultTighteningForTruncation: Bool](nsparagraphstyle/allowsdefaulttighteningfortruncation.md)
  A Boolean value that indicates whether the system tightens character spacing before truncating text.
### Getting the html header level
- [var headerLevel: Int](nsparagraphstyle/headerlevel.md)
  The paragraph’s header level for HTML generation.
### Determining writing direction
- [class func defaultWritingDirection(forLanguage: String?) -> NSWritingDirection](nsparagraphstyle/defaultwritingdirection(forlanguage:).md)
  Returns the default writing direction for the specified language.
- [var baseWritingDirection: NSWritingDirection](nsparagraphstyle/basewritingdirection.md)
  The base writing direction for the paragraph.
- [enum NSWritingDirection](nswritingdirection.md)
  Constants that specify the writing direction.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSMutableParagraphStyle](nsmutableparagraphstyle.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NSMutableParagraphStyle](nsmutableparagraphstyle.md)
  An object for changing the values of the subattributes in a paragraph style attribute.
- [class NSTextTab](nstexttab.md)
  A tab in a paragraph.
- [class NSTextList](nstextlist.md)
  A section of text that forms a single list.
- [class NSTextTable](nstexttable.md)
  An object that represents a text table as a whole.
- [class NSTextTableBlock](nstexttableblock.md)
  A text block that appears as a cell in a text table.
- [class NSTextBlock](nstextblock.md)
  A block of text laid out in a subregion of the text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle)*