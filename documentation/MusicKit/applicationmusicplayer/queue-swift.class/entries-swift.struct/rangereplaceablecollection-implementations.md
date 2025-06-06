# RangeReplaceableCollection Implementations

**Framework**: MusicKit

## Topics

### Operators
- [static func + <Other>(Other, Self) -> Self](applicationmusicplayer/queue-swift.class/entries-swift.struct/+(_:_:)-6e1kk.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](applicationmusicplayer/queue-swift.class/entries-swift.struct/+(_:_:)-qk55.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func + <Other>(Self, Other) -> Self](applicationmusicplayer/queue-swift.class/entries-swift.struct/+(_:_:)-xw4q.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func += <Other>(inout Self, Other)](applicationmusicplayer/queue-swift.class/entries-swift.struct/+=(_:_:).md)
  Appends the elements of a sequence to a range-replaceable collection.
### Initializers
- [init<S>(S)](applicationmusicplayer/queue-swift.class/entries-swift.struct/init(_:).md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init(repeating: Self.Element, count: Int)](applicationmusicplayer/queue-swift.class/entries-swift.struct/init(repeating:count:).md)
  Creates a new collection containing the specified number of a single, repeated value.
### Instance Methods
- [func append(Self.Element)](applicationmusicplayer/queue-swift.class/entries-swift.struct/append(_:).md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](applicationmusicplayer/queue-swift.class/entries-swift.struct/append(contentsof:).md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func applying(CollectionDifference<Self.Element>) -> Self?](applicationmusicplayer/queue-swift.class/entries-swift.struct/applying(_:).md)
  Applies the given difference to this collection.
- [func filter((Self.Element) throws -> Bool) rethrows -> Self](applicationmusicplayer/queue-swift.class/entries-swift.struct/filter(_:).md)
  Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [func insert(Self.Element, at: Self.Index)](applicationmusicplayer/queue-swift.class/entries-swift.struct/insert(_:at:).md)
  Inserts a new element into the collection at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](applicationmusicplayer/queue-swift.class/entries-swift.struct/insert(contentsof:at:).md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func popLast() -> Self.Element?](applicationmusicplayer/queue-swift.class/entries-swift.struct/poplast.md)
  Removes and returns the last element of the collection.
- [func remove(at: Self.Index) -> Self.Element](applicationmusicplayer/queue-swift.class/entries-swift.struct/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](applicationmusicplayer/queue-swift.class/entries-swift.struct/removeall(keepingcapacity:).md)
  Removes all elements from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](applicationmusicplayer/queue-swift.class/entries-swift.struct/removeall(where:)-2qnp6.md)
  Removes all the elements that satisfy the given predicate.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](applicationmusicplayer/queue-swift.class/entries-swift.struct/removeall(where:)-8bt3v.md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](applicationmusicplayer/queue-swift.class/entries-swift.struct/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](applicationmusicplayer/queue-swift.class/entries-swift.struct/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](applicationmusicplayer/queue-swift.class/entries-swift.struct/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](applicationmusicplayer/queue-swift.class/entries-swift.struct/removelast(_:).md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange(Range<Self.Index>)](applicationmusicplayer/queue-swift.class/entries-swift.struct/removesubrange(_:)-37gem.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](applicationmusicplayer/queue-swift.class/entries-swift.struct/removesubrange(_:)-8htwl.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubranges(RangeSet<Self.Index>)](applicationmusicplayer/queue-swift.class/entries-swift.struct/removesubranges(_:)-5z4vv.md)
  Removes the elements at the given indices.
- [func replace<C, Replacement>(C, with: Replacement, maxReplacements: Int)](applicationmusicplayer/queue-swift.class/entries-swift.struct/replace(_:with:maxreplacements:).md)
  Replaces all occurrences of a target sequence with a given collection
- [func replaceSubrange<C>(Range<Self.Index>, with: C)](applicationmusicplayer/queue-swift.class/entries-swift.struct/replacesubrange(_:with:)-21xgu.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C, R>(R, with: C)](applicationmusicplayer/queue-swift.class/entries-swift.struct/replacesubrange(_:with:)-5vg0h.md)
  Replaces the specified subrange of elements with the given collection.
- [func replacing<C, Replacement>(C, with: Replacement, maxReplacements: Int) -> Self](applicationmusicplayer/queue-swift.class/entries-swift.struct/replacing(_:with:maxreplacements:).md)
  Returns a new collection in which all occurrences of a target sequence are replaced by another collection.
- [func replacing<C, Replacement>(C, with: Replacement, subrange: Range<Self.Index>, maxReplacements: Int) -> Self](applicationmusicplayer/queue-swift.class/entries-swift.struct/replacing(_:with:subrange:maxreplacements:).md)
  Returns a new collection in which all occurrences of a target sequence are replaced by another collection.
- [func reserveCapacity(Int)](applicationmusicplayer/queue-swift.class/entries-swift.struct/reservecapacity(_:).md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.
- [func trimPrefix<Prefix>(Prefix)](applicationmusicplayer/queue-swift.class/entries-swift.struct/trimprefix(_:).md)
  Removes `prefix` from the start of the collection.
- [func trimPrefix(while: (Self.Element) throws -> Bool) rethrows](applicationmusicplayer/queue-swift.class/entries-swift.struct/trimprefix(while:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct/rangereplaceablecollection-implementations)*