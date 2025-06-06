# containsColumn(_:_:)

**Framework**: TabularData  
**Kind**: method

Returns a Boolean value indicating whether the data frame contains a column.

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
func containsColumn<T>(_ name: String, _ type: T.Type) -> Bool
```

## Parameters

- `name`: A column name.
- `type`: An element type.

## See Also

- [var isEmpty: Bool](dataframe/isempty.md)
  A Boolean that indicates whether the data frame type is empty.
- [var shape: (rows: Int, columns: Int)](dataframe/shape.md)
  The number of rows and columns in the data frame.
- [var columns: [AnyColumn]](dataframe/columns.md)
  The entire data frame as a collection of columns.
- [var rows: DataFrame.Rows](dataframe/rows-swift.property.md)
  The entire data frame as a collection of rows.
- [DataFrame.Rows](dataframe/rows-swift.struct.md)
  A collection of rows in a data frame.
- [var base: DataFrame](dataframe/base.md)
  The underlying data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/containscolumn(_:_:))*