# DataFrame.Rows

**Framework**: TabularData  
**Kind**: struct  
**Role**: Structure

A collection of rows in a data frame.

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
struct Rows
```

## Topics

### Inspecting a Row Collection
- [var count: Int](./rows-swift.struct/count.md)
  The number of rows in the collection.
### Accessing Elements
- [subscript(Int) -> DataFrame.Row](./rows-swift.struct/subscript%28_%29-3f938.md)
  Accesses a row at an index.
- [subscript(Range<Int>) -> DataFrame.Rows](./rows-swift.struct/subscript%28_%29-2qzx7.md)
  Returns a row collection from an index range.

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [MutableCollection](../../Swift/mutablecollection.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Inspecting a Data Frame
- [var shape: (rows: Int, columns: Int)](./shape.md)
  The number of rows and columns in the data frame.
- [var columns: [AnyColumn]](./columns.md)
  The entire data frame as a collection of columns.
- [var rows: DataFrame.Rows](./rows-swift.property.md)
  The entire data frame as a collection of rows.
- [var base: DataFrame](./base.md)
  The underlying data frame.
- [func containsColumn<T>(String, T.Type) -> Bool](./containscolumn%28_,_%29.md)
  Returns a Boolean value indicating whether the data frame contains a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/rows-swift.struct)*