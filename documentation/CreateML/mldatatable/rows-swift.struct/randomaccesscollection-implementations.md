# RandomAccessCollection Implementations

**Framework**: Create ML  
**Role**: API Collection

## Topics

### Instance Properties
- [var endIndex: Int](./endindex.md)
  The DataTable’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var startIndex: Int](./startindex.md)
  The position of the first row in a nonempty DataTable. If the DataTable is empty, `startIndex` is equal to `endIndex`.
### Subscripts
- [subscript(Int) -> MLDataTable.Rows.Element](./subscript%28_%29.md)
  Subscript by index. This returns a row in the data table.
### Type Aliases
- [MLDataTable.Rows.Element](./element.md)
  The Element of a DataTable is a Row. This is represented as a Dictionary-like type containing all Column names and their corresponding values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct/randomaccesscollection-implementations)*