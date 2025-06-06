# TableColumnAlignment

**Framework**: SwiftUI  
**Kind**: struct

Describes the alignment of the content of a table column.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct TableColumnAlignment
```

#### Overview

The alignment of a column applies to both its header label as well as the default alignment of its content view for each row.

## Topics

### Getting the alignment
- [static var automatic: TableColumnAlignment](tablecolumnalignment/automatic.md)
  The default column alignment.
- [static var leading: TableColumnAlignment](tablecolumnalignment/leading.md)
  Leading column alignment.
- [static var center: TableColumnAlignment](tablecolumnalignment/center.md)
  Center column alignment.
- [static var trailing: TableColumnAlignment](tablecolumnalignment/trailing.md)
  Trailing column alignment.
- [static var numeric: TableColumnAlignment](tablecolumnalignment/numeric.md)
  Column alignment appropriate for numeric content.
- [static func numeric(Locale.NumberingSystem) -> TableColumnAlignment](tablecolumnalignment/numeric(_:).md)
  Column alignment appropriate for numeric content.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct TableColumn](tablecolumn.md)
  A column that displays a view for each row in a table.
- [protocol TableColumnContent](tablecolumncontent.md)
  A type used to represent columns within a table.
- [struct TableColumnBuilder](tablecolumnbuilder.md)
  A result builder that creates table column content from closures.
- [struct TableColumnForEach](tablecolumnforeach.md)
  A structure that computes columns on demand from an underlying collection of identified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnalignment)*