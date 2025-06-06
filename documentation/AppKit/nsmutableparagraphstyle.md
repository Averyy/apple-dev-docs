# NSMutableParagraphStyle

**Framework**: AppKit  
**Kind**: class

An object for changing the values of the subattributes in a paragraph style attribute.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class NSMutableParagraphStyle
```

#### Overview

The [`NSMutableParagraphStyle`](nsmutableparagraphstyle.md) class adds methods to its superclass, [`NSParagraphStyle`](nsparagraphstyle.md), for changing the values of the subattributes in a paragraph style attribute. For more information, see [`NSParagraphStyle`](nsparagraphstyle.md) and [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString).

> ❗ **Important**:  Don’t mutate a paragraph style object after adding it to an attributed string. Doing so can cause your app to crash.

 Don’t mutate a paragraph style object after adding it to an attributed string. Doing so can cause your app to crash.

## Topics

### Setting style information
- [func setParagraphStyle(NSParagraphStyle)](nsmutableparagraphstyle/setparagraphstyle(_:).md)
  Replaces the subattributes of the paragraph with those in the specified paragraph style object.
- [var alignment: NSTextAlignment](nsmutableparagraphstyle/alignment.md)
  The text alignment of the paragraph.
- [var firstLineHeadIndent: CGFloat](nsmutableparagraphstyle/firstlineheadindent.md)
  The indentation of the first line of the paragraph.
- [var headIndent: CGFloat](nsmutableparagraphstyle/headindent.md)
  The indentation of the paragraph’s lines other than the first.
- [var tailIndent: CGFloat](nsmutableparagraphstyle/tailindent.md)
  The trailing indentation of the paragraph.
- [var lineHeightMultiple: CGFloat](nsmutableparagraphstyle/lineheightmultiple.md)
  The line height multiple.
- [var maximumLineHeight: CGFloat](nsmutableparagraphstyle/maximumlineheight.md)
  The paragraph’s maximum line height.
- [var minimumLineHeight: CGFloat](nsmutableparagraphstyle/minimumlineheight.md)
  The paragraph’s minimum line height.
- [var lineSpacing: CGFloat](nsmutableparagraphstyle/linespacing.md)
  The distance in points between the bottom of one line fragment and the top of the next.
- [var paragraphSpacing: CGFloat](nsmutableparagraphstyle/paragraphspacing.md)
  The space after the end of the paragraph.
- [var paragraphSpacingBefore: CGFloat](nsmutableparagraphstyle/paragraphspacingbefore.md)
  The distance between the paragraph’s top and the beginning of its text content.
- [var baseWritingDirection: NSWritingDirection](nsmutableparagraphstyle/basewritingdirection.md)
  The base writing direction for the paragraph.
### Specifying tab information
- [func addTabStop(NSTextTab)](nsmutableparagraphstyle/addtabstop(_:).md)
  Adds the specified tab stop to the paragraph.
- [func removeTabStop(NSTextTab)](nsmutableparagraphstyle/removetabstop(_:).md)
  Removes the first text tab with a location and type equal to the specified tab stop.
- [var tabStops: [NSTextTab]!](nsmutableparagraphstyle/tabstops.md)
  The text tab objects that represent the paragraph’s tab stops.
- [var defaultTabInterval: CGFloat](nsmutableparagraphstyle/defaulttabinterval.md)
  A number used as the document’s default tab spacing.
### Setting text blocks and lists
- [var textBlocks: [NSTextBlock]](nsmutableparagraphstyle/textblocks.md)
  The text blocks that contain the paragraph.
- [var textLists: [NSTextList]](nsmutableparagraphstyle/textlists.md)
  The text lists that contain the paragraph.
### Setting line-break information
- [var lineBreakMode: NSLineBreakMode](nsmutableparagraphstyle/linebreakmode.md)
  The mode for breaking lines in the paragraph.
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](nsmutableparagraphstyle/linebreakstrategy.md)
  The strategies that the text system may use to break lines while laying out the paragraph.
- [var hyphenationFactor: Float](nsmutableparagraphstyle/hyphenationfactor.md)
  The paragraph’s threshold for hyphenation.
- [var usesDefaultHyphenation: Bool](nsmutableparagraphstyle/usesdefaulthyphenation.md)
- [var tighteningFactorForTruncation: Float](nsmutableparagraphstyle/tighteningfactorfortruncation.md)
  The threshold for using tightening as an alternative to truncation.
- [var allowsDefaultTighteningForTruncation: Bool](nsmutableparagraphstyle/allowsdefaulttighteningfortruncation.md)
  A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.
### Setting HTML header level
- [var headerLevel: Int](nsmutableparagraphstyle/headerlevel.md)
  The paragraph’s header level for HTML generation.

## Relationships

### Inherits From
- [NSParagraphStyle](nsparagraphstyle.md)
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

- [class NSParagraphStyle](nsparagraphstyle.md)
  The paragraph or ruler attributes for an attributed string.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle)*