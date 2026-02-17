# RandomAccessCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var indices: UInt128.Words.Indices](uint128/words-swift.struct/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Self.Index.Stride](uint128/words-swift.struct/distance(from:to:).md)
  Returns the distance between two indices.
- [func index(Self.Index, offsetBy: Self.Index.Stride) -> Self.Index](uint128/words-swift.struct/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](uint128/words-swift.struct/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Int) -> Int](uint128/words-swift.struct/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: Int) -> Int](uint128/words-swift.struct/index(before:).md)
  Returns the position immediately before the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint128/words-swift.struct/randomaccesscollection-implementations)*