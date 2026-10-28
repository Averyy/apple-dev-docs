# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that computes table columns on demand over a given constant range.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- visionOS 1.1+

## Declaration

```swift
nonisolated
init(_ data: Range<Int>, @TableColumnBuilder<TableColumnForEach<Range<Int>, Int, RowValue, Sort, Content>.TableRowValue, TableColumnForEach<Range<Int>, Int, RowValue, Sort, Content>.TableColumnSortComparator> content: @escaping (Int) -> Content) where Data == Range<Int>, ID == Int
```

**Other overloads**:

```swift
nonisolated
init(_ data: Data, @TableColumnBuilder<TableColumnForEach<Data, ID, RowValue, Sort, Content>.TableRowValue, TableColumnForEach<Data, ID, RowValue, Sort, Content>.TableColumnSortComparator> content: @escaping (Data.Element) -> Content) where ID == Data.Element.ID, Data.Element : Identifiable
```

## Discussion

The instance only reads the initial value of the provided `data` and doesn’t need to identify columns across updates. To compute columns on demand over a dynamic range, use [`init(_:id:content:)`](./init%28_,id,content%29.md).

## Parameters

- `data`: A constant range.
- `content`: The table column builder that creates columns based on the range index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnforeach/init(_:content:)-e05a)*