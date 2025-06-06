# TableOutlineGroupContent

**Framework**: SwiftUI  
**Kind**: struct

An opaque table row type created by a table’s hierarchical initializers.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct TableOutlineGroupContent<Data> where Data : RandomAccessCollection, Data.Element : Identifiable
```

#### Overview

This row content is created by `Table.init(_:,children:,...)` initializers as the table’s `Rows` generic type.

To explicitly create hierarchical rows, use [`OutlineGroup`](outlinegroup.md) instead.

## Relationships

### Conforms To
- [TableRowContent](tablerowcontent.md)

## See Also

- [struct DisclosureTableRow](disclosuretablerow.md)
  A kind of table row that shows or hides additional rows based on the state of a disclosure control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tableoutlinegroupcontent)*