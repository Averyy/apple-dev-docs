# base

**Framework**: TabularData  
**Kind**: property

The underlying data frame.

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
var base: DataFrame { get }
```

## See Also

- [var isEmpty: Bool](dataframe/slice/isempty.md)
  A Boolean that indicates whether the data frame type is empty.
- [var shape: (rows: Int, columns: Int)](dataframe/slice/shape.md)
  The number of rows and columns in the slice.
- [var columns: [AnyColumnSlice]](dataframe/slice/columns.md)
  The entire slice as a collection of columns.
- [var rows: DataFrame.Rows](dataframe/slice/rows.md)
  The entire slice as a collection of rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/base)*