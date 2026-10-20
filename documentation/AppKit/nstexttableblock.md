# NSTextTableBlock

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A text block that appears as a cell in a text table.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class NSTextTableBlock
```

```objc
@interface NSTextTableBlock : NSTextBlock
```

## Topics

### Creation
- [init(table: NSTextTable, startingRow: Int, rowSpan: Int, startingColumn: Int, columnSpan: Int)](./nstexttableblock/init%28table,startingrow,rowspan,startingcolumn,columnspan%29.md)
  Returns an initialized text table block.
### Getting the block’s enclosing table
- [var table: NSTextTable](./nstexttableblock/table.md)
  Returns the table containing this text table block.
### Getting information about the block’s position in its enclosing table
- [var startingRow: Int](./nstexttableblock/startingrow.md)
  Returns the table row at which this text table block starts.
- [var rowSpan: Int](./nstexttableblock/rowspan.md)
  Returns the number of table rows spanned by this text table block.
- [var startingColumn: Int](./nstexttableblock/startingcolumn.md)
  Returns the table column at which this text table block starts.
- [var columnSpan: Int](./nstexttableblock/columnspan.md)
  Returns the number of table columns spanned by this text table block.
### Initializers
- [init?(coder: NSCoder)](./nstexttableblock/init%28coder%29.md)

## Relationships

### Inherits From
- [NSTextBlock](./nstextblock.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Tables
- [class NSTextTable](./nstexttable.md)
  An object that represents a text table as a whole.
- [class NSTextBlock](./nstextblock.md)
  A block of text laid out in a subregion of the text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexttableblock)*