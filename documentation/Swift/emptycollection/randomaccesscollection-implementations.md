# RandomAccessCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Properties
- [var endIndex: EmptyCollection<Element>.Index](./endindex.md)
  Always zero, just like `startIndex`.
- [var indices: Range<Self.Index>](./indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: EmptyCollection<Element>.Index](./startindex.md)
  Always zero, just like `endIndex`.
### Instance Methods
- [func distance(from: EmptyCollection<Element>.Index, to: EmptyCollection<Element>.Index) -> Int](./distance%28from,to%29.md)
  The distance between two indexes (always zero).
- [func index(EmptyCollection<Element>.Index, offsetBy: Int) -> EmptyCollection<Element>.Index](./index%28_,offsetby%29.md)
  Returns an index that is the specified distance from the given index.
- [func index(EmptyCollection<Element>.Index, offsetBy: Int, limitedBy: EmptyCollection<Element>.Index) -> EmptyCollection<Element>.Index?](./index%28_,offsetby,limitedby%29.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: EmptyCollection<Element>.Index) -> EmptyCollection<Element>.Index](./index%28after%29.md)
  Always traps.
- [func index(before: EmptyCollection<Element>.Index) -> EmptyCollection<Element>.Index](./index%28before%29.md)
  Always traps.
### Subscripts
- [subscript(EmptyCollection<Element>.Index) -> Element](./subscript%28_%29-1wkfh.md)
  Accesses the element at the given position.
- [subscript(Range<EmptyCollection<Element>.Index>) -> EmptyCollection<Element>.SubSequence](./subscript%28_%29-5fxf8.md)
  Accesses a contiguous subrange of the collection’s elements.
### Type Aliases
- [EmptyCollection.Index](./index.md)
  A type that represents a valid position in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/emptycollection/randomaccesscollection-implementations)*