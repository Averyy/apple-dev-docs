# isEmpty

**Framework**: TabularData  
**Kind**: property

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

- [var shape: (rows: Int, columns: Int)](dataframeprotocol/shape.md)
  The number or rows and columns of the data frame type.
- [var columns: [Self.ColumnType]](dataframeprotocol/columns.md)
  The columns of the underlying data frame.
- [associatedtype ColumnType : AnyColumnProtocol](dataframeprotocol/columntype.md)
  A type that conforms to the type-erased column protocol.
- [var rows: DataFrame.Rows](dataframeprotocol/rows.md)
  The rows of the underlying data frame.
- [DataFrame.Rows](dataframe/rows-swift.struct.md)
  A collection of rows in a data frame.
- [var base: DataFrame](dataframeprotocol/base.md)
  The underlying data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframeprotocol/isempty)*