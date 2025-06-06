# RandomAccessCollection Implementations

**Framework**: MusicKit

## Topics

### Instance Properties
- [var indices: MusicItemCollection<MusicItemType>.Indices](musicitemcollection/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
### Instance Methods
- [func distance(from: MusicItemCollection<MusicItemType>.Index, to: MusicItemCollection<MusicItemType>.Index) -> Int](musicitemcollection/distance(from:to:).md)
  Returns the distance between two indices.
- [func formIndex(after: inout MusicItemCollection<MusicItemType>.Index)](musicitemcollection/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(before: inout MusicItemCollection<MusicItemType>.Index)](musicitemcollection/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(MusicItemCollection<MusicItemType>.Index, offsetBy: Int) -> MusicItemCollection<MusicItemType>.Index](musicitemcollection/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(MusicItemCollection<MusicItemType>.Index, offsetBy: Int, limitedBy: MusicItemCollection<MusicItemType>.Index) -> MusicItemCollection<MusicItemType>.Index?](musicitemcollection/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: MusicItemCollection<MusicItemType>.Index) -> MusicItemCollection<MusicItemType>.Index](musicitemcollection/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: MusicItemCollection<MusicItemType>.Index) -> MusicItemCollection<MusicItemType>.Index](musicitemcollection/index(before:).md)
  Returns the position immediately before the given index.
### Subscripts
- [subscript(Range<MusicItemCollection<MusicItemType>.Index>) -> MusicItemCollection<MusicItemType>.SubSequence](musicitemcollection/subscript(_:)-1h5iv.md)
  Accesses a contiguous subrange of the collection’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicitemcollection/randomaccesscollection-implementations)*