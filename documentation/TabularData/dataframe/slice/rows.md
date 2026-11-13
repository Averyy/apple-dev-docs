# rows

**Framework**: TabularData  
**Kind**: property  
**Role**: Instance Property

The entire slice as a collection of rows.

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
var rows: DataFrame.Rows { get set }
```

## See Also

### Inspecting a slice
- [var shape: (rows: Int, columns: Int)](./shape.md)
  The number of rows and columns in the slice.
- [var columns: [AnyColumnSlice]](./columns.md)
  The entire slice as a collection of columns.
- [var base: DataFrame](./base.md)
  The underlying data frame.
- [var isEmpty: Bool](../../dataframeprotocol/isempty.md)
  A Boolean that indicates whether the data frame type is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/rows)*