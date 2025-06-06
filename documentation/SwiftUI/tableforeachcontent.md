# TableForEachContent

**Framework**: SwiftUI  
**Kind**: struct

A type of table row content that creates table rows created by iterating over a collection.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct TableForEachContent<Data> where Data : RandomAccessCollection, Data.Element : Identifiable
```

#### Overview

You don’t use this type directly. The various `Table.init(_:,...)` initializers create this type as the table’s `Rows` generic type.

To explicitly create dynamic collection-based rows, use [`ForEach`](foreach.md) instead.

## Relationships

### Conforms To
- [TableRowContent](tablerowcontent.md)

## See Also

- [struct TableRow](tablerow.md)
  A row that represents a data value in a table.
- [protocol TableRowContent](tablerowcontent.md)
  A type used to represent table rows.
- [struct TableHeaderRowContent](tableheaderrowcontent.md)
  A table row that displays a single view instead of columned content.
- [struct TupleTableRowContent](tupletablerowcontent.md)
  A type of table column content that creates table rows created from a Swift tuple of table rows.
- [struct EmptyTableRowContent](emptytablerowcontent.md)
  A table row content that doesn’t produce any rows.
- [protocol DynamicTableRowContent](dynamictablerowcontent.md)
  A type of table row content that generates table rows from an underlying collection of data.
- [struct TableRowBuilder](tablerowbuilder.md)
  A result builder that creates table row content from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tableforeachcontent)*