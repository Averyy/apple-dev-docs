# EmptyTableRowContent

**Framework**: SwiftUI  
**Kind**: struct

A table row content that doesn’t produce any rows.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct EmptyTableRowContent<Value> where Value : Identifiable
```

#### Overview

You will rarely, if ever, need to create an `EmptyTableRowContent` directly. Instead, `EmptyTableRowContent` represents the absence of a row.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
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
- [struct TableForEachContent](tableforeachcontent.md)
  A type of table row content that creates table rows created by iterating over a collection.
- [protocol DynamicTableRowContent](dynamictablerowcontent.md)
  A type of table row content that generates table rows from an underlying collection of data.
- [struct TableRowBuilder](tablerowbuilder.md)
  A result builder that creates table row content from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/emptytablerowcontent)*