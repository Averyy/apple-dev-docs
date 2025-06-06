# RandomAccessCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var endIndex: Int](arrayslice/endindex.md)
  The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var startIndex: Int](arrayslice/startindex.md)
  The position of the first element in a nonempty array.
### Instance Methods
- [func distance(from: Int, to: Int) -> Int](arrayslice/distance(from:to:).md)
  Returns the distance between two indices.
- [func formIndex(after: inout Int)](arrayslice/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(before: inout Int)](arrayslice/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Int, offsetBy: Int) -> Int](arrayslice/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Int, offsetBy: Int, limitedBy: Int) -> Int?](arrayslice/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Int) -> Int](arrayslice/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: Int) -> Int](arrayslice/index(before:).md)
  Returns the position immediately before the given index.
### Subscripts
- [subscript(Int) -> Element](arrayslice/subscript(_:)-4e8d9.md)
  Accesses the element at the specified position.
- [subscript(Range<Int>) -> ArraySlice<Element>](arrayslice/subscript(_:)-63qca.md)
  Accesses a contiguous subrange of the array’s elements.
### Type Aliases
- [ArraySlice.Index](arrayslice/index.md)
  The index type for arrays, `Int`.
- [ArraySlice.Indices](arrayslice/indices.md)
  The type that represents the indices that are valid for subscripting an array, in ascending order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/arrayslice/randomaccesscollection-implementations)*