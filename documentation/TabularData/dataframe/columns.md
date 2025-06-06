# columns

**Framework**: TabularData  
**Kind**: property

The entire data frame as a collection of columns.

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
var columns: [AnyColumn] { get }
```

## See Also

- [var isEmpty: Bool](dataframe/isempty.md)
  A Boolean that indicates whether the data frame type is empty.
- [var shape: (rows: Int, columns: Int)](dataframe/shape.md)
  The number of rows and columns in the data frame.
- [var rows: DataFrame.Rows](dataframe/rows-swift.property.md)
  The entire data frame as a collection of rows.
- [DataFrame.Rows](dataframe/rows-swift.struct.md)
  A collection of rows in a data frame.
- [var base: DataFrame](dataframe/base.md)
  The underlying data frame.
- [func containsColumn<T>(String, T.Type) -> Bool](dataframe/containscolumn(_:_:).md)
  Returns a Boolean value indicating whether the data frame contains a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/columns)*