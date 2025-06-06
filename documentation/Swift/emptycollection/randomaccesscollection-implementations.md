# RandomAccessCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var endIndex: EmptyCollection<Element>.Index](emptycollection/endindex.md)
  Always zero, just like `startIndex`.
- [var startIndex: EmptyCollection<Element>.Index](emptycollection/startindex.md)
  Always zero, just like `endIndex`.
### Instance Methods
- [func distance(from: EmptyCollection<Element>.Index, to: EmptyCollection<Element>.Index) -> Int](emptycollection/distance(from:to:).md)
  The distance between two indexes (always zero).
- [func index(EmptyCollection<Element>.Index, offsetBy: Int) -> EmptyCollection<Element>.Index](emptycollection/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(EmptyCollection<Element>.Index, offsetBy: Int, limitedBy: EmptyCollection<Element>.Index) -> EmptyCollection<Element>.Index?](emptycollection/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: EmptyCollection<Element>.Index) -> EmptyCollection<Element>.Index](emptycollection/index(after:).md)
  Always traps.
- [func index(before: EmptyCollection<Element>.Index) -> EmptyCollection<Element>.Index](emptycollection/index(before:).md)
  Always traps.
### Subscripts
- [subscript(EmptyCollection<Element>.Index) -> Element](emptycollection/subscript(_:)-1wkfh.md)
  Accesses the element at the given position.
- [subscript(Range<EmptyCollection<Element>.Index>) -> EmptyCollection<Element>.SubSequence](emptycollection/subscript(_:)-5fxf8.md)
  Accesses a contiguous subrange of the collection’s elements.
### Type Aliases
- [EmptyCollection.Index](emptycollection/index.md)
  A type that represents a valid position in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/emptycollection/randomaccesscollection-implementations)*