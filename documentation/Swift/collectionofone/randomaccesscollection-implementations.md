# RandomAccessCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var endIndex: CollectionOfOne<Element>.Index](collectionofone/endindex.md)
  The “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var startIndex: CollectionOfOne<Element>.Index](collectionofone/startindex.md)
  The position of the first element.
### Instance Methods
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](collectionofone/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: CollectionOfOne<Element>.Index) -> CollectionOfOne<Element>.Index](collectionofone/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: CollectionOfOne<Element>.Index) -> CollectionOfOne<Element>.Index](collectionofone/index(before:).md)
  Returns the position immediately before the given index.
### Subscripts
- [subscript(Range<Int>) -> CollectionOfOne<Element>.SubSequence](collectionofone/subscript(_:)-16mfr.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(Int) -> Element](collectionofone/subscript(_:)-876qi.md)
  Accesses the element at the specified position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collectionofone/randomaccesscollection-implementations)*