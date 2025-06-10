# NSTextTable

**Framework**: AppKit  
**Kind**: class

An object that represents a text table as a whole.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSTextTable
```

#### Overview

A text table is responsible for laying out and drawing the text table blocks it contains, and it maintains the basic parameters of the table.

## Topics

### Getting and setting number of columns
- [var numberOfColumns: Int](nstexttable/numberofcolumns.md)
  The number of columns in the text table.
### Getting and setting layout algorithm
- [var layoutAlgorithm: NSTextTable.LayoutAlgorithm](nstexttable/layoutalgorithm-swift.property.md)
  The text table layout algorithm.
### Collapsing borders
- [var collapsesBorders: Bool](nstexttable/collapsesborders.md)
  A Boolean value indicating whether the text table borders are collapsible.
### Hiding empty cells
- [var hidesEmptyCells: Bool](nstexttable/hidesemptycells.md)
  A Boolean value indicating whether the text table hides empty cells.
### Determining layout rectangles
- [func rect(for: NSTextTableBlock, layoutAt: NSPoint, in: NSRect, textContainer: NSTextContainer, characterRange: NSRange) -> NSRect](nstexttable/rect(for:layoutat:in:textcontainer:characterrange:).md)
  Returns the rectangle within which glyphs should be laid out for a text table block.
- [func boundsRect(for: NSTextTableBlock, contentRect: NSRect, in: NSRect, textContainer: NSTextContainer, characterRange: NSRange) -> NSRect](nstexttable/boundsrect(for:contentrect:in:textcontainer:characterrange:).md)
  Returns the rectangle the text table block actually occupies, including padding, borders, and margins.
### Drawing the table
- [func drawBackground(for: NSTextTableBlock, withFrame: NSRect, in: NSView, characterRange: NSRange, layoutManager: NSLayoutManager)](nstexttable/drawbackground(for:withframe:in:characterrange:layoutmanager:).md)
  Draws any colors and other decorations for a text table block.
### Constants
- [NSTextTable.LayoutAlgorithm](nstexttable/layoutalgorithm-swift.enum.md)
  These constants, specifying the type of text table layout algorithm, are used with [`layoutAlgorithm`](nstexttable/layoutalgorithm-swift.property.md).

## Relationships

### Inherits From
- [NSTextBlock](nstextblock.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSParagraphStyle](nsparagraphstyle.md)
  The paragraph or ruler attributes for an attributed string.
- [class NSMutableParagraphStyle](nsmutableparagraphstyle.md)
  An object for changing the values of the subattributes in a paragraph style attribute.
- [class NSTextTab](nstexttab.md)
  A tab in a paragraph.
- [class NSTextList](nstextlist.md)
  A section of text that forms a single list.
- [class NSTextTableBlock](nstexttableblock.md)
  A text block that appears as a cell in a text table.
- [class NSTextBlock](nstextblock.md)
  A block of text laid out in a subregion of the text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexttable)*