# isEmpty

**Framework**: TabularData  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the data frame type is empty.

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
var isEmpty: Bool { get }
```

## See Also

### Inspecting a data frame
- [var shape: (rows: Int, columns: Int)](../dataframe/shape.md)
  The number of rows and columns in the data frame.
- [var columns: [AnyColumn]](../dataframe/columns.md)
  The entire data frame as a collection of columns.
- [var rows: DataFrame.Rows](../dataframe/rows-swift.property.md)
  The entire data frame as a collection of rows.
- [DataFrame.Rows](../dataframe/rows-swift.struct.md)
  A collection of rows in a data frame.
- [var base: DataFrame](../dataframe/base.md)
  The underlying data frame.
- [func containsColumn(String) -> Bool](../dataframe/containscolumn%28_%29-8spst.md)
  Returns a Boolean value indicating whether the data frame contains a column.
- [func containsColumn<T>(ColumnID<T>) -> Bool](../dataframe/containscolumn%28_%29-6nqfs.md)
  Returns a Boolean value indicating whether the data frame contains a column matching a column ID.
- [func containsColumn<T>(String, T.Type) -> Bool](../dataframe/containscolumn%28_,_%29.md)
  Returns a Boolean value indicating whether the data frame contains a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframeprotocol/isempty)*