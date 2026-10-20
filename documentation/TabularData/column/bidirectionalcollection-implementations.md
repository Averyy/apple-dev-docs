# BidirectionalCollection Implementations

**Framework**: TabularData  
**Role**: API Collection

## Topics

### Instance Properties
- [var endIndex: Int](./endindex.md)
  The index of the final element in the column.
- [var startIndex: Int](./startindex.md)
  The index of the initial element in the column.
### Instance Methods
- [func index(after: Int) -> Int](./index%28after%29.md)
  Returns the index immediately after an element index.
- [func index(before: Int) -> Int](./index%28before%29.md)
  Returns the index immediately before an element index.
### Subscripts
- [subscript(Range<Int>) -> ColumnSlice<WrappedElement>](./subscript%28_%29-gne9.md)
  Accesses a contiguous range of elements.
- [subscript(Int) -> Column<WrappedElement>.Element](./subscript%28_%29-qm4d.md)
  Accesses an element at an index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/bidirectionalcollection-implementations)*