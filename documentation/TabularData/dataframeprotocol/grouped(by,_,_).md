# grouped(by:_:_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Creates a grouping from three columns of different types.

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
func grouped<T0, T1, T2>(by column0: ColumnID<T0>, _ column1: ColumnID<T1>, _ column2: ColumnID<T2>) -> some RowGroupingProtocol where T0 : Hashable, T1 : Hashable, T2 : Hashable
```

## Parameters

- `column0`: A column identifier.
- `column1`: A second column identifier.
- `column2`: A third column identifier.

## See Also

### Creating a Row Grouping by Multiple Columns
- [func grouped(by: String...) -> some RowGroupingProtocol](./grouped%28by%29-4wcw6.md)
  Creates a grouping from multiple columns you select by name.
- [func grouped<T>(by: ColumnID<T>...) -> some RowGroupingProtocol](./grouped%28by%29-6m6to.md)
  Creates a grouping from multiple columns that you select by column identifier.
- [func grouped<T0, T1>(by: ColumnID<T0>, ColumnID<T1>) -> some RowGroupingProtocol](./grouped%28by,_%29.md)
  Creates a grouping from two columns of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframeprotocol/grouped(by:_:_:))*