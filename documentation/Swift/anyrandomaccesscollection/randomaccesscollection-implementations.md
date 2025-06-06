# RandomAccessCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var endIndex: AnyRandomAccessCollection<Element>.Index](anyrandomaccesscollection/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var startIndex: AnyRandomAccessCollection<Element>.Index](anyrandomaccesscollection/startindex.md)
  The position of the first element in a non-empty collection.
### Instance Methods
- [func distance(from: AnyRandomAccessCollection<Element>.Index, to: AnyRandomAccessCollection<Element>.Index) -> Int](anyrandomaccesscollection/distance(from:to:).md)
  Returns the distance between two indices.
- [func formIndex(after: inout AnyRandomAccessCollection<Element>.Index)](anyrandomaccesscollection/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(before: inout AnyRandomAccessCollection<Element>.Index)](anyrandomaccesscollection/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(AnyRandomAccessCollection<Element>.Index, offsetBy: Int) -> AnyRandomAccessCollection<Element>.Index](anyrandomaccesscollection/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(AnyRandomAccessCollection<Element>.Index, offsetBy: Int, limitedBy: AnyRandomAccessCollection<Element>.Index) -> AnyRandomAccessCollection<Element>.Index?](anyrandomaccesscollection/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: AnyRandomAccessCollection<Element>.Index) -> AnyRandomAccessCollection<Element>.Index](anyrandomaccesscollection/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: AnyRandomAccessCollection<Element>.Index) -> AnyRandomAccessCollection<Element>.Index](anyrandomaccesscollection/index(before:).md)
  Returns the position immediately before the given index.
### Subscripts
- [subscript(AnyRandomAccessCollection<Element>.Index) -> Element](anyrandomaccesscollection/subscript(_:)-37hui.md)
  Accesses the element indicated by `position`.
- [subscript(Range<AnyRandomAccessCollection<Element>.Index>) -> AnyRandomAccessCollection<Element>.SubSequence](anyrandomaccesscollection/subscript(_:)-6jydx.md)
  Accesses a contiguous subrange of the collection’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyrandomaccesscollection/randomaccesscollection-implementations)*