# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that uniquely identifies and creates table columns across updates based on the identity of the underlying data.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- visionOS 1.1+

## Declaration

```swift
init(_ data: Data, @TableColumnBuilder<TableColumnForEach<Data, ID, RowValue, Sort, Content>.TableRowValue, TableColumnForEach<Data, ID, RowValue, Sort, Content>.TableColumnSortComparator> content: @escaping (Data.Element) -> Content) where ID == Data.Element.ID, Data.Element : Identifiable
```

## Parameters

- `data`: The identified data that the   instance   uses to create table columns dynamically.
- `content`: The table column builder that creates columns dynamically   for each element.

## See Also

- [init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> Content)](tablecolumnforeach/init(_:id:content:).md)
  Creates an instance that uniquely identifies and creates table columns across updates based on the provided key path to the underlying data’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnforeach/init(_:content:))*