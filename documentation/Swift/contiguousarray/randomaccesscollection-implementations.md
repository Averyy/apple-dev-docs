# RandomAccessCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Properties
- [var endIndex: Int](./endindex.md)
  The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: Range<Self.Index>](./indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: Int](./startindex.md)
  The position of the first element in a nonempty array.
### Instance Methods
- [func distance(from: Int, to: Int) -> Int](./distance%28from,to%29.md)
  Returns the distance between two indices.
- [func formIndex(after: inout Int)](./formindex%28after%29.md)
  Replaces the given index with its successor.
- [func formIndex(before: inout Int)](./formindex%28before%29.md)
  Replaces the given index with its predecessor.
- [func index(Int, offsetBy: Int) -> Int](./index%28_,offsetby%29.md)
  Returns an index that is the specified distance from the given index.
- [func index(Int, offsetBy: Int, limitedBy: Int) -> Int?](./index%28_,offsetby,limitedby%29.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Int) -> Int](./index%28after%29.md)
  Returns the position immediately after the given index.
- [func index(before: Int) -> Int](./index%28before%29.md)
  Returns the position immediately before the given index.
### Subscripts
- [subscript(Range<Int>) -> ArraySlice<Element>](./subscript%28_%29-41wt7.md)
  Accesses a contiguous subrange of the array’s elements.
- [subscript(Int) -> Element](./subscript%28_%29-899p6.md)
  Accesses the element at the specified position.
### Type Aliases
- [ContiguousArray.Index](./index.md)
  The index type for arrays, `Int`.
- [ContiguousArray.Indices](./indices.md)
  The type that represents the indices that are valid for subscripting an array, in ascending order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/randomaccesscollection-implementations)*