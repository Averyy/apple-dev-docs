# RandomAccessCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var endIndex: Repeated<Element>.Index](repeated/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: Range<Self.Index>](repeated/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: Repeated<Element>.Index](repeated/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Self.Index.Stride](repeated/distance(from:to:).md)
  Returns the distance between two indices.
- [func index(Self.Index, offsetBy: Self.Index.Stride) -> Self.Index](repeated/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](repeated/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Self.Index) -> Self.Index](repeated/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: Self.Index) -> Self.Index](repeated/index(before:).md)
  Returns the position immediately after the given index.
### Subscripts
- [subscript(Int) -> Element](repeated/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias Index](repeated/index.md)
  A type that represents a valid position in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/repeated/randomaccesscollection-implementations)*