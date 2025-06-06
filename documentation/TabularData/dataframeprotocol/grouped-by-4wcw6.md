# grouped(by:)

**Framework**: TabularData  
**Kind**: method

Creates a grouping from multiple columns you select by name.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func grouped(by columnNames: String...) -> some RowGroupingProtocol
```

## Parameters

- `columnNames`: A comma-separated, or variadic, list of column names.

## See Also

- [func grouped<T>(by: ColumnID<T>...) -> some RowGroupingProtocol](dataframeprotocol/grouped(by:)-6m6to.md)
  Creates a grouping from multiple columns that you select by column identifier.
- [func grouped<T0, T1>(by: ColumnID<T0>, ColumnID<T1>) -> some RowGroupingProtocol](dataframeprotocol/grouped(by:_:).md)
  Creates a grouping from two columns of different types.
- [func grouped<T0, T1, T2>(by: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>) -> some RowGroupingProtocol](dataframeprotocol/grouped(by:_:_:).md)
  Creates a grouping from three columns of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframeprotocol/grouped(by:)-4wcw6)*