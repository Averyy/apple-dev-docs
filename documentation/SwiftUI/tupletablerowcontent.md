# TupleTableRowContent

**Framework**: SwiftUI  
**Kind**: struct

A type of table column content that creates table rows created from a Swift tuple of table rows.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@frozen
struct TupleTableRowContent<Value, T> where Value : Identifiable
```

#### Overview

Don’t use this type directly; instead, SwiftUI uses this type as the return value from the various `buildBlock` methods in [`TableRowBuilder`](tablerowbuilder.md). The size of the tuple corresponds to how many columns you create in the `rows` closure you provide to the [`Table`](table.md) initializer.

## Topics

### Accessing the value
- [var value: T](tupletablerowcontent/value.md)

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
- [struct TableForEachContent](tableforeachcontent.md)
  A type of table row content that creates table rows created by iterating over a collection.
- [struct EmptyTableRowContent](emptytablerowcontent.md)
  A table row content that doesn’t produce any rows.
- [protocol DynamicTableRowContent](dynamictablerowcontent.md)
  A type of table row content that generates table rows from an underlying collection of data.
- [struct TableRowBuilder](tablerowbuilder.md)
  A result builder that creates table row content from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tupletablerowcontent)*