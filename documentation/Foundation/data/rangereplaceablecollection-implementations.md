# RangeReplaceableCollection Implementations

**Framework**: Foundation

## Topics

### Operators
- [static func + <Other>(Self, Other) -> Self](data/+(_:_:)-6ztpr.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func + <Other>(Self, Other) -> Self](data/+(_:_:)-7pdqb.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func + <Other>(Other, Self) -> Self](data/+(_:_:)-8bhq4.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func += <Other>(inout Self, Other)](data/+=(_:_:).md)
  Appends the elements of a sequence to a range-replaceable collection.
### Initializers
- [init<S>(S)](data/init(_:).md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init(repeating: Self.Element, count: Int)](data/init(repeating:count:)-l9uo.md)
  Creates a new collection containing the specified number of a single, repeated value.
### Instance Methods
- [func append(Self.Element)](data/append(_:)-4z9b6.md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](data/append(contentsof:)-6dmhm.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func applying(CollectionDifference<Self.Element>) -> Self?](data/applying(_:).md)
  Applies the given difference to this collection.
- [func filter((Self.Element) throws -> Bool) rethrows -> Self](data/filter(_:).md)
  Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [func insert(Self.Element, at: Self.Index)](data/insert(_:at:).md)
  Inserts a new element into the collection at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](data/insert(contentsof:at:).md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func popLast() -> Self.Element?](data/poplast-9cem9.md)
  Removes and returns the last element of the collection.
- [func popLast() -> Self.Element?](data/poplast-onja.md)
  Removes and returns the last element of the collection.
- [func remove(at: Self.Index) -> Self.Element](data/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](data/removeall(keepingcapacity:).md)
  Removes all elements from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](data/removeall(where:)-3z895.md)
  Removes all the elements that satisfy the given predicate.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](data/removeall(where:)-7bkav.md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](data/removefirst-2zs4w.md)
  Removes and returns the first element of the collection.
- [func removeFirst() -> Self.Element](data/removefirst-4xots.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](data/removefirst(_:)-327eg.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeFirst(Int)](data/removefirst(_:)-4xnt2.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](data/removelast-3932k.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](data/removelast-6h42v.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](data/removelast(_:)-247mb.md)
  Removes the specified number of elements from the end of the collection.
- [func removeLast(Int)](data/removelast(_:)-8wba8.md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange<R>(R)](data/removesubrange(_:)-5oyti.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange(Range<Self.Index>)](data/removesubrange(_:)-8ohtp.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubranges(RangeSet<Self.Index>)](data/removesubranges(_:)-6ikpd.md)
  Removes the elements at the given indices.
- [func replace<C, Replacement>(C, with: Replacement, maxReplacements: Int)](data/replace(_:with:maxreplacements:).md)
  Replaces all occurrences of a target sequence with a given collection
- [func replaceSubrange<C>(Range<Self.Index>, with: C)](data/replacesubrange(_:with:)-3pbr2.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C, R>(R, with: C)](data/replacesubrange(_:with:)-6ukp0.md)
  Replaces the specified subrange of elements with the given collection.
- [func replacing<C, Replacement>(C, with: Replacement, maxReplacements: Int) -> Self](data/replacing(_:with:maxreplacements:).md)
  Returns a new collection in which all occurrences of a target sequence are replaced by another collection.
- [func replacing<C, Replacement>(C, with: Replacement, subrange: Range<Self.Index>, maxReplacements: Int) -> Self](data/replacing(_:with:subrange:maxreplacements:).md)
  Returns a new collection in which all occurrences of a target sequence are replaced by another collection.
- [func reserveCapacity(Int)](data/reservecapacity(_:).md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.
- [func trimPrefix<Prefix>(Prefix)](data/trimprefix(_:)-s2c0.md)
  Removes `prefix` from the start of the collection.
- [func trimPrefix(while: (Self.Element) throws -> Bool) rethrows](data/trimprefix(while:)-20u46.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/rangereplaceablecollection-implementations)*