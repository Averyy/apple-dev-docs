# RandomAccessCollection Implementations

**Framework**: TabularData  
**Role**: API Collection

## Topics

### Instance Properties
- [var endIndex: Int](./endindex.md)
  The index of the final column in the row.
- [var startIndex: Int](./startindex.md)
  The index of the initial column in the row.
### Instance Methods
- [func index(after: Int) -> Int](./index%28after%29.md)
  Returns the column index immediately before a column index in the row.
- [func index(before: Int) -> Int](./index%28before%29.md)
  Returns the column index immediately after a column index in the row.
### Subscripts
- [subscript(Int) -> Any?](./subscript%28_%29-5tsj0.md)
  Accesses a value at a column index.
- [subscript(Range<Int>) -> Slice<DataFrame.Row>](./subscript%28_%29-9bmjj.md)
  Accesses a slice from a range of indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/row/randomaccesscollection-implementations)*