# DataFrame.Rows

**Framework**: TabularData  
**Kind**: struct

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
- [var count: Int](dataframe/rows-swift.struct/count.md)
  The number of rows in the collection.
### Accessing Elements
- [subscript(Int) -> DataFrame.Row](dataframe/rows-swift.struct/subscript(_:)-3f938.md)
  Accesses a row at an index.
- [subscript(Range<Int>) -> DataFrame.Rows](dataframe/rows-swift.struct/subscript(_:)-2qzx7.md)
  Returns a row collection from an index range.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [var shape: (rows: Int, columns: Int)](dataframe/shape.md)
  The number of rows and columns in the data frame.
- [var columns: [AnyColumn]](dataframe/columns.md)
  The entire data frame as a collection of columns.
- [var rows: DataFrame.Rows](dataframe/rows-swift.property.md)
  The entire data frame as a collection of rows.
- [var base: DataFrame](dataframe/base.md)
  The underlying data frame.
- [func containsColumn<T>(String, T.Type) -> Bool](dataframe/containscolumn(_:_:).md)
  Returns a Boolean value indicating whether the data frame contains a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/rows-swift.struct)*