# TableHeaderRowContent

**Framework**: SwiftUI  
**Kind**: struct

A table row that displays a single view instead of columned content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct TableHeaderRowContent<Value, Content> where Value : Identifiable, Content : View
```

#### Overview

You do not create this type directly. The framework creates it on your behalf.

## Relationships

### Conforms To
- [TableRowContent](tablerowcontent.md)

## See Also

- [struct TableRow](tablerow.md)
  A row that represents a data value in a table.
- [protocol TableRowContent](tablerowcontent.md)
  A type used to represent table rows.
- [struct TupleTableRowContent](tupletablerowcontent.md)
  A type of table column content that creates table rows created from a Swift tuple of table rows.
- [struct TableForEachContent](tableforeachcontent.md)
  A type of table row content that creates table rows created by iterating over a collection.
- [struct EmptyTableRowContent](emptytablerowcontent.md)
  A table row content that doesn’t produce any rows.
- [protocol DynamicTableRowContent](dynamictablerowcontent.md)
  A type of table row content that generates table rows from an underlying collection of data.
- [struct TableRowBuilder](tablerowbuilder.md)
  A result builder that creates table row content from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tableheaderrowcontent)*