# shape

**Framework**: TabularData  
**Kind**: property  
**Role**: Instance Property

The number of rows and columns in the data frame.

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
var shape: (rows: Int, columns: Int) { get }
```

## Parameters

- `rows`: The number of rows in the data frame.
- `columns`: The number of columns in the data frame.

## See Also

### Inspecting a Data Frame
- [var columns: [AnyColumn]](./columns.md)
  The entire data frame as a collection of columns.
- [var rows: DataFrame.Rows](./rows-swift.property.md)
  The entire data frame as a collection of rows.
- [DataFrame.Rows](./rows-swift.struct.md)
  A collection of rows in a data frame.
- [var base: DataFrame](./base.md)
  The underlying data frame.
- [func containsColumn<T>(String, T.Type) -> Bool](./containscolumn%28_,_%29.md)
  Returns a Boolean value indicating whether the data frame contains a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/shape)*