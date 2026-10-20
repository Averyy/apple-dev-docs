# Collection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Properties
- [var count: Int](./count.md)
  The number of elements in the collection.
- [var count: Int](./count-5qqod.md)
  The number of elements in the collection.
- [var endIndex: Base.Index](./endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: LazyMapSequence<Base, Element>.Indices](./indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](./isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var isEmpty: Bool](./isempty-75pes.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: Base.Index](./startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func distance(from: LazyMapSequence<Base, Element>.Index, to: LazyMapSequence<Base, Element>.Index) -> Int](./distance%28from,to%29.md)
  Returns the distance between two indices.
- [func distance(from: Self.Index, to: Self.Index) -> Int](./distance%28from,to%29-3i820.md)
  Returns the distance between two indices.
- [func firstIndex(of: Self.Element) -> Self.Index?](./firstindex%28of%29.md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](./firstindex%28where%29.md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](./formindex%28_,offsetby%29.md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](./formindex%28_,offsetby,limitedby%29.md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout LazyMapSequence<Base, Element>.Index)](./formindex%28after%29.md)
  Replaces the given index with its successor.
- [func formIndex(after: inout Self.Index)](./formindex%28after%29-6932e.md)
  Replaces the given index with its successor.
- [func index(LazyMapSequence<Base, Element>.Index, offsetBy: Int) -> LazyMapSequence<Base, Element>.Index](./index%28_,offsetby%29.md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](./index%28_,offsetby%29-78pdz.md)
  Returns an index that is the specified distance from the given index.
- [func index(LazyMapSequence<Base, Element>.Index, offsetBy: Int, limitedBy: LazyMapSequence<Base, Element>.Index) -> LazyMapSequence<Base, Element>.Index?](./index%28_,offsetby,limitedby%29.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](./index%28_,offsetby,limitedby%29-5uiel.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: LazyMapSequence<Base, Element>.Index) -> LazyMapSequence<Base, Element>.Index](./index%28after%29.md)
  Returns the position immediately after the given index.
- [func index(of: Self.Element) -> Self.Index?](./index%28of%29.md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](./indices%28of%29.md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](./indices%28where%29.md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](./map%28_%29-8qb3x.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(through: Self.Index) -> Self.SubSequence](./prefix%28through%29.md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](./prefix%28upto%29.md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func randomElement() -> Self.Element?](./randomelement%28%29.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](./randomelement%28using%29.md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](./removingsubranges%28_%29.md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](./split%28separator,maxsplits,omittingemptysubsequences%29-5eafc.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](./suffix%28from%29.md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(Base.Index) -> Element](./subscript%28_%29-36b2w.md)
  Accesses the element at `position`.
- [subscript<R>(R) -> Self.SubSequence](./subscript%28_%29-3hxz5.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(Range<Base.Index>) -> LazyMapSequence<Base, Element>.SubSequence](./subscript%28_%29-4qmx0.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](./subscript%28_%29-4tv8v.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript(UnboundedRange) -> Self.SubSequence](./subscript%28_%29-88114.md)
### Type Aliases
- [LazyMapSequence.Index](./index.md)
  A type that represents a position in the collection.
- [LazyMapSequence.Indices](./indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [LazyMapSequence.SubSequence](./subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazymapsequence/collection-implementations)*