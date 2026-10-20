# RandomAccessCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Properties
- [var endIndex: AnyRandomAccessCollection<Element>.Index](./endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var startIndex: AnyRandomAccessCollection<Element>.Index](./startindex.md)
  The position of the first element in a non-empty collection.
### Instance Methods
- [func distance(from: AnyRandomAccessCollection<Element>.Index, to: AnyRandomAccessCollection<Element>.Index) -> Int](./distance%28from,to%29.md)
  Returns the distance between two indices.
- [func formIndex(after: inout AnyRandomAccessCollection<Element>.Index)](./formindex%28after%29.md)
  Replaces the given index with its successor.
- [func formIndex(before: inout AnyRandomAccessCollection<Element>.Index)](./formindex%28before%29.md)
  Replaces the given index with its predecessor.
- [func index(AnyRandomAccessCollection<Element>.Index, offsetBy: Int) -> AnyRandomAccessCollection<Element>.Index](./index%28_,offsetby%29.md)
  Returns an index that is the specified distance from the given index.
- [func index(AnyRandomAccessCollection<Element>.Index, offsetBy: Int, limitedBy: AnyRandomAccessCollection<Element>.Index) -> AnyRandomAccessCollection<Element>.Index?](./index%28_,offsetby,limitedby%29.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: AnyRandomAccessCollection<Element>.Index) -> AnyRandomAccessCollection<Element>.Index](./index%28after%29.md)
  Returns the position immediately after the given index.
- [func index(before: AnyRandomAccessCollection<Element>.Index) -> AnyRandomAccessCollection<Element>.Index](./index%28before%29.md)
  Returns the position immediately before the given index.
### Subscripts
- [subscript(AnyRandomAccessCollection<Element>.Index) -> Element](./subscript%28_%29-37hui.md)
  Accesses the element indicated by `position`.
- [subscript(Range<AnyRandomAccessCollection<Element>.Index>) -> AnyRandomAccessCollection<Element>.SubSequence](./subscript%28_%29-6jydx.md)
  Accesses a contiguous subrange of the collection’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyrandomaccesscollection/randomaccesscollection-implementations)*