# RandomAccessCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var endIndex: Int](unicode/scalar/utf8view/endindex.md)
  The “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: Range<Self.Index>](unicode/scalar/utf8view/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: Int](unicode/scalar/utf8view/startindex.md)
  The position of the first code unit.
### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Self.Index.Stride](unicode/scalar/utf8view/distance(from:to:).md)
  Returns the distance between two indices.
- [func index(Self.Index, offsetBy: Self.Index.Stride) -> Self.Index](unicode/scalar/utf8view/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](unicode/scalar/utf8view/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Self.Index) -> Self.Index](unicode/scalar/utf8view/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: Self.Index) -> Self.Index](unicode/scalar/utf8view/index(before:).md)
  Returns the position immediately after the given index.
### Subscripts
- [subscript(Int) -> UTF8.CodeUnit](unicode/scalar/utf8view/subscript(_:).md)
  Accesses the code unit at the specified position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/utf8view/randomaccesscollection-implementations)*