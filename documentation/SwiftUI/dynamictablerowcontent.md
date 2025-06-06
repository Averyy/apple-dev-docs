# DynamicTableRowContent

**Framework**: SwiftUI  
**Kind**: protocol

A type of table row content that generates table rows from an underlying collection of data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
protocol DynamicTableRowContent : TableRowContent
```

#### Overview

This table row content type provides drag-and-drop support for tables. Use the [`onInsert(of:perform:)`](dynamictablerowcontent/oninsert(of:perform:).md) modifier to add an action to call when the table inserts new contents into its underlying collection.

## Topics

### Getting row data
- [var data: Self.Data](dynamictablerowcontent/data-swift.property.md)
  The collection of underlying data.
- [associatedtype Data : Collection](dynamictablerowcontent/data-swift.associatedtype.md)
  The type of the underlying collection of data.
### Inserting rows
- [func onInsert(of: [UTType], perform: (Int, [NSItemProvider]) -> Void) -> ModifiedContent<Self, OnInsertTableRowModifier>](dynamictablerowcontent/oninsert(of:perform:).md)
  Sets the insert action for the dynamic table rows.
- [struct OnInsertTableRowModifier](oninserttablerowmodifier.md)
  A table row modifier that adds the ability to insert data in some base row content.
### Supporting drag and drop
- [func dropDestination<T>(for: T.Type, action: (Int, [T]) -> Void) -> ModifiedContent<Self, OnInsertTableRowModifier>](dynamictablerowcontent/dropdestination(for:action:).md)
  Sets the insert action for the dynamic table rows.

## Relationships

### Inherits From
- [TableRowContent](tablerowcontent.md)
### Conforming Types
- [ForEach](foreach.md)
- [ModifiedContent](modifiedcontent.md)

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
- [struct EmptyTableRowContent](emptytablerowcontent.md)
  A table row content that doesn’t produce any rows.
- [struct TableRowBuilder](tablerowbuilder.md)
  A result builder that creates table row content from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dynamictablerowcontent)*