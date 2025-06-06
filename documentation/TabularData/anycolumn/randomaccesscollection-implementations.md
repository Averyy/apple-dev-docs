# RandomAccessCollection Implementations

**Framework**: TabularData

## Topics

### Instance Properties
- [var endIndex: Int](anycolumn/endindex.md)
  The index of the final element in the column.
- [var startIndex: Int](anycolumn/startindex.md)
  The index of the initial element in the column.
### Instance Methods
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](anycolumn/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Int) -> Int](anycolumn/index(after:).md)
  Returns the index immediately after an element index.
- [func index(before: Int) -> Int](anycolumn/index(before:).md)
  Returns the index immediately before an element index.
### Subscripts
- [subscript(Range<Int>) -> AnyColumnSlice](anycolumn/subscript(_:)-1n9t9.md)
  Accesses a contiguous subrange of the elements.
- [subscript(Int) -> Any?](anycolumn/subscript(_:)-6z1b5.md)
  Accesses an element at an index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/randomaccesscollection-implementations)*