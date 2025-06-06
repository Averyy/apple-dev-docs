# BidirectionalCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var last: Self.Element?](lazyprefixwhilesequence/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](lazyprefixwhilesequence/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](lazyprefixwhilesequence/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: Self.Index, to: Self.Index) -> Int](lazyprefixwhilesequence/distance(from:to:)-4ezr7.md)
- [func formIndex(before: inout Self.Index)](lazyprefixwhilesequence/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](lazyprefixwhilesequence/index(_:offsetby:)-44ez2.md)
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](lazyprefixwhilesequence/index(_:offsetby:limitedby:)-3wev9.md)
- [func index(before: LazyPrefixWhileSequence<Base>.Index) -> LazyPrefixWhileSequence<Base>.Index](lazyprefixwhilesequence/index(before:).md)
  Returns the position immediately before the given index.
- [func joined(separator: String) -> String](lazyprefixwhilesequence/joined(separator:)-9atxk.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](lazyprefixwhilesequence/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](lazyprefixwhilesequence/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](lazyprefixwhilesequence/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazyprefixwhilesequence/bidirectionalcollection-implementations)*