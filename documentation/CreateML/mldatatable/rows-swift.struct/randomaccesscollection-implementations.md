# RandomAccessCollection Implementations

**Framework**: Create ML

## Topics

### Instance Properties
- [var endIndex: Int](mldatatable/rows-swift.struct/endindex.md)
  The DataTable’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var startIndex: Int](mldatatable/rows-swift.struct/startindex.md)
  The position of the first row in a nonempty DataTable. If the DataTable is empty, `startIndex` is equal to `endIndex`.
### Instance Methods
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](mldatatable/rows-swift.struct/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
### Subscripts
- [subscript(Int) -> MLDataTable.Rows.Element](mldatatable/rows-swift.struct/subscript(_:).md)
  Subscript by index. This returns a row in the data table.
### Type Aliases
- [MLDataTable.Rows.Element](mldatatable/rows-swift.struct/element.md)
  The Element of a DataTable is a Row. This is represented as a Dictionary-like type containing all Column names and their corresponding values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct/randomaccesscollection-implementations)*