# BidirectionalCollection Implementations

**Framework**: TabularData  
**Role**: API Collection

## Topics

### Instance Properties
- [var endIndex: Int](./endindex.md)
  The index of the final element in the column slice.
- [var startIndex: Int](./startindex.md)
  The index of the initial element in the column slice.
### Instance Methods
- [func index(after: Int) -> Int](./index%28after%29.md)
  Returns the index immediately after an element index.
- [func index(before: Int) -> Int](./index%28before%29.md)
  Returns the index immediately before an element index.
### Subscripts
- [subscript(Range<Int>) -> DiscontiguousColumnSlice<WrappedElement>](./subscript%28_%29-8rd2f.md)
  Accesses a contiguous range of elements.
- [subscript(Int) -> DiscontiguousColumnSlice<WrappedElement>.Element](./subscript%28_%29-9y37v.md)
  Accesses an element at an index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/bidirectionalcollection-implementations)*