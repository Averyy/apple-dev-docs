# RandomAccessCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var endIndex: Int](contiguousarray/endindex.md)
  The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var startIndex: Int](contiguousarray/startindex.md)
  The position of the first element in a nonempty array.
### Instance Methods
- [func distance(from: Int, to: Int) -> Int](contiguousarray/distance(from:to:).md)
  Returns the distance between two indices.
- [func formIndex(after: inout Int)](contiguousarray/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(before: inout Int)](contiguousarray/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Int, offsetBy: Int) -> Int](contiguousarray/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Int, offsetBy: Int, limitedBy: Int) -> Int?](contiguousarray/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Int) -> Int](contiguousarray/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: Int) -> Int](contiguousarray/index(before:).md)
  Returns the position immediately before the given index.
### Subscripts
- [subscript(Range<Int>) -> ArraySlice<Element>](contiguousarray/subscript(_:)-41wt7.md)
  Accesses a contiguous subrange of the array’s elements.
- [subscript(Int) -> Element](contiguousarray/subscript(_:)-899p6.md)
  Accesses the element at the specified position.
### Type Aliases
- [ContiguousArray.Index](contiguousarray/index.md)
  The index type for arrays, `Int`.
- [ContiguousArray.Indices](contiguousarray/indices.md)
  The type that represents the indices that are valid for subscripting an array, in ascending order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/randomaccesscollection-implementations)*