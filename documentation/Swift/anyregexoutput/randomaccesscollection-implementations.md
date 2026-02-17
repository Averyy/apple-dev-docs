# RandomAccessCollection Implementations

**Framework**: Swift

## Topics

### Structures
- [AnyRegexOutput.Element](anyregexoutput/element.md)
  An individual match output value.
### Instance Properties
- [var indices: Range<Self.Index>](anyregexoutput/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Self.Index.Stride](anyregexoutput/distance(from:to:).md)
  Returns the distance between two indices.
- [func index(Self.Index, offsetBy: Self.Index.Stride) -> Self.Index](anyregexoutput/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](anyregexoutput/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Int) -> Int](anyregexoutput/index(after:).md)
  Returns the position immediately after the given index.
- [func index(after: Self.Index) -> Self.Index](anyregexoutput/index(after:)-6xh6a.md)
  Returns the position immediately after the given index.
- [func index(before: Int) -> Int](anyregexoutput/index(before:).md)
  Returns the position immediately before the given index.
- [func index(before: Self.Index) -> Self.Index](anyregexoutput/index(before:)-87bgk.md)
  Returns the position immediately after the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyregexoutput/randomaccesscollection-implementations)*