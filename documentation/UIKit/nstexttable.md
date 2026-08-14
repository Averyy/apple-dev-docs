# NSTextTable

**Framework**: UIKit  
**Kind**: class

An object that represents a table of rows and columns in an attributed string.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSTextTable
```

## Mentions

- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md)

#### Overview

`NSTextTable` is a subclass of [`NSTextBlock`](nstextblock.md) that represents a complete table. You can configure the number of columns, whether adjacent cell borders collapse into one, and whether empty cells are hidden.

Each cell is an [`NSTextTableBlock`](nstexttableblock.md) that specifies its row, column, and span within the table. You don’t add cells directly to the table — instead, you apply each cell’s block to a paragraph using [`textBlocks`](nsparagraphstyle/textblocks.md).

Choose between two layout algorithms using the [`layoutAlgorithm`](nstexttable/layoutalgorithm-swift.property.md) property:

- [`NSTextTable.LayoutAlgorithm.automatic`](nstexttable/layoutalgorithm-swift.enum/automatic.md) distributes column widths based on content, similar to the HTML `auto` table layout.
- [`NSTextTable.LayoutAlgorithm.fixed`](nstexttable/layoutalgorithm-swift.enum/fixed.md) distributes column widths based on explicit values set on the first row of cells, similar to the HTML `fixed` table layout.

## Topics

### Configuring the table
- [var numberOfColumns: Int](nstexttable/numberofcolumns.md)
- [var layoutAlgorithm: NSTextTable.LayoutAlgorithm](nstexttable/layoutalgorithm-swift.property.md)
- [var collapsesBorders: Bool](nstexttable/collapsesborders.md)
- [var hidesEmptyCells: Bool](nstexttable/hidesemptycells.md)
- [NSTextTable.LayoutAlgorithm](nstexttable/layoutalgorithm-swift.enum.md)

## Relationships

### Inherits From
- [NSTextBlock](nstextblock.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md)
  Create and configure tables in attributed strings and display them in a text view.
- [class NSTextTableBlock](nstexttableblock.md)
  A text block that represents a single cell in a text table.
- [class NSTextBlock](nstextblock.md)
  An object that defines the size, spacing, and appearance of a block of text in an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstexttable)*