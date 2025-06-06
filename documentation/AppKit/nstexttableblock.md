# NSTextTableBlock

**Framework**: AppKit  
**Kind**: class

A text block that appears as a cell in a text table.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSTextTableBlock
```

## Topics

### Creation
- [init(table: NSTextTable, startingRow: Int, rowSpan: Int, startingColumn: Int, columnSpan: Int)](nstexttableblock/init(table:startingrow:rowspan:startingcolumn:columnspan:).md)
  Returns an initialized text table block.
### Getting the block’s enclosing table
- [var table: NSTextTable](nstexttableblock/table.md)
  Returns the table containing this text table block.
### Getting information about the block’s position in its enclosing table
- [var startingRow: Int](nstexttableblock/startingrow.md)
  Returns the table row at which this text table block starts.
- [var rowSpan: Int](nstexttableblock/rowspan.md)
  Returns the number of table rows spanned by this text table block.
- [var startingColumn: Int](nstexttableblock/startingcolumn.md)
  Returns the table column at which this text table block starts.
- [var columnSpan: Int](nstexttableblock/columnspan.md)
  Returns the number of table columns spanned by this text table block.

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

## See Also

- [class NSParagraphStyle](nsparagraphstyle.md)
  The paragraph or ruler attributes for an attributed string.
- [class NSMutableParagraphStyle](nsmutableparagraphstyle.md)
  An object for changing the values of the subattributes in a paragraph style attribute.
- [class NSTextTab](nstexttab.md)
  A tab in a paragraph.
- [class NSTextList](nstextlist.md)
  A section of text that forms a single list.
- [class NSTextTable](nstexttable.md)
  An object that represents a text table as a whole.
- [class NSTextBlock](nstextblock.md)
  A block of text laid out in a subregion of the text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexttableblock)*