# base

**Framework**: TabularData  
**Kind**: property  
**Role**: Instance Property

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

### Inspecting a Slice
- [var shape: (rows: Int, columns: Int)](./shape.md)
  The number of rows and columns in the slice.
- [var columns: [AnyColumnSlice]](./columns.md)
  The entire slice as a collection of columns.
- [var rows: DataFrame.Rows](./rows.md)
  The entire slice as a collection of rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/base)*