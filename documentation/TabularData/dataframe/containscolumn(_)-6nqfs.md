# containsColumn(_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the data frame contains a column matching a column ID.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
func containsColumn<T>(_ id: ColumnID<T>) -> Bool
```

## Parameters

- `id`: A column ID.

## See Also

### Inspecting a data frame
- [var shape: (rows: Int, columns: Int)](./shape.md)
  The number of rows and columns in the data frame.
- [var columns: [AnyColumn]](./columns.md)
  The entire data frame as a collection of columns.
- [var rows: DataFrame.Rows](./rows-swift.property.md)
  The entire data frame as a collection of rows.
- [DataFrame.Rows](./rows-swift.struct.md)
  A collection of rows in a data frame.
- [var base: DataFrame](./base.md)
  The underlying data frame.
- [func containsColumn(String) -> Bool](./containscolumn%28_%29-8spst.md)
  Returns a Boolean value indicating whether the data frame contains a column.
- [func containsColumn<T>(String, T.Type) -> Bool](./containscolumn%28_,_%29.md)
  Returns a Boolean value indicating whether the data frame contains a column.
- [var isEmpty: Bool](../dataframeprotocol/isempty.md)
  A Boolean that indicates whether the data frame type is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/containscolumn(_:)-6nqfs)*