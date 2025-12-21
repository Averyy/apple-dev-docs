# BidirectionalCollection Implementations

**Framework**: TabularData

## Topics

### Instance Properties
- [var endIndex: Int](column/endindex.md)
  The index of the final element in the column.
- [var startIndex: Int](column/startindex.md)
  The index of the initial element in the column.
### Instance Methods
- [func index(after: Int) -> Int](column/index(after:).md)
  Returns the index immediately after an element index.
- [func index(before: Int) -> Int](column/index(before:).md)
  Returns the index immediately before an element index.
### Subscripts
- [subscript(Range<Int>) -> ColumnSlice<WrappedElement>](column/subscript(_:)-gne9.md)
  Accesses a contiguous range of elements.
- [subscript(Int) -> Column<WrappedElement>.Element](column/subscript(_:)-qm4d.md)
  Accesses an element at an index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/bidirectionalcollection-implementations)*