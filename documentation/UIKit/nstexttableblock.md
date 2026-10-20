# NSTextTableBlock

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A text block that represents a single cell in a text table.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSTextTableBlock
```

```objc
@interface NSTextTableBlock : NSTextBlock
```

## Mentions

- [Adding tables to attributed strings in UIKit](./adding-tables-to-attributed-strings.md)

#### Overview

`NSTextTableBlock` is a subclass of [`NSTextBlock`](./nstextblock.md) that places a paragraph in a cell of an [`NSTextTable`](./nstexttable.md). When you create an `NSTextTableBlock`, you specify the table it belongs to, the cell’s starting row and column, and how many rows and columns the cell spans.

To build a table, create an [`NSTextTable`](./nstexttable.md), then create an `NSTextTableBlock` for each cell. Assign each block to a paragraph by setting [`textBlocks`](./nsparagraphstyle/textblocks.md) on an [`NSMutableParagraphStyle`](./nsmutableparagraphstyle.md) and applying that style to the paragraph’s range in your attributed string.

## Topics

### Creating a text table block
- [init(table: NSTextTable, startingRow: Int, rowSpan: Int, startingColumn: Int, columnSpan: Int)](./nstexttableblock/init%28table,startingrow,rowspan,startingcolumn,columnspan%29.md)
- [init?(coder: NSCoder)](./nstexttableblock/init%28coder%29.md)
### Accessing the parent table
- [var table: NSTextTable](./nstexttableblock/table.md)
### Accessing cell position
- [var startingRow: Int](./nstexttableblock/startingrow.md)
- [var rowSpan: Int](./nstexttableblock/rowspan.md)
- [var startingColumn: Int](./nstexttableblock/startingcolumn.md)
- [var columnSpan: Int](./nstexttableblock/columnspan.md)

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
- [Adding tables to attributed strings in UIKit](./adding-tables-to-attributed-strings.md)
  Create and configure tables in attributed strings and display them in a text view.
- [class NSTextTable](./nstexttable.md)
  An object that represents a table of rows and columns in an attributed string.
- [class NSTextBlock](./nstextblock.md)
  An object that defines the size, spacing, and appearance of a block of text in an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstexttableblock)*