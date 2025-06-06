# RangeReplaceableCollection Implementations

**Framework**: Swift

## Topics

### Operators
- [static func + <Other>(Self, Other) -> Self](slice/+(_:_:)-298al.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func + <Other>(Other, Self) -> Self](slice/+(_:_:)-4resp.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](slice/+(_:_:)-99wuu.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func += <Other>(inout Self, Other)](slice/+=(_:_:).md)
  Appends the elements of a sequence to a range-replaceable collection.
### Initializers
- [init()](slice/init.md)
  Creates a new, empty collection.
- [init<S>(S)](slice/init(_:).md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init<S>(S)](slice/init(_:)-81eoy.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init(repeating: Base.Element, count: Int)](slice/init(repeating:count:).md)
  Creates a new collection containing the specified number of a single, repeated value.
- [init(repeating: Self.Element, count: Int)](slice/init(repeating:count:)-6ps2q.md)
  Creates a new collection containing the specified number of a single, repeated value.
### Instance Methods
- [func append(Self.Element)](slice/append(_:).md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](slice/append(contentsof:).md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func applying(CollectionDifference<Self.Element>) -> Self?](slice/applying(_:).md)
  Applies the given difference to this collection.
- [func insert(Base.Element, at: Slice<Base>.Index)](slice/insert(_:at:)-6sg0.md)
  Inserts a new element into the collection at the specified position.
- [func insert(Self.Element, at: Self.Index)](slice/insert(_:at:)-8i1dc.md)
  Inserts a new element into the collection at the specified position.
- [func insert<S>(contentsOf: S, at: Slice<Base>.Index)](slice/insert(contentsof:at:)-25pep.md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](slice/insert(contentsof:at:)-2xj4m.md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func popLast() -> Self.Element?](slice/poplast-30m9y.md)
  Removes and returns the last element of the collection.
- [func popLast() -> Self.Element?](slice/poplast-4rely.md)
  Removes and returns the last element of the collection.
- [func remove(at: Slice<Base>.Index) -> Base.Element](slice/remove(at:)-7ep9e.md)
  Removes and returns the element at the specified position.
- [func remove(at: Self.Index) -> Self.Element](slice/remove(at:)-7xja6.md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](slice/removeall(keepingcapacity:).md)
  Removes all elements from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](slice/removeall(where:)-26lr3.md)
  Removes all the elements that satisfy the given predicate.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](slice/removeall(where:)-9u7g.md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](slice/removefirst-1iayr.md)
  Removes and returns the first element of the collection.
- [func removeFirst() -> Self.Element](slice/removefirst-3eija.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](slice/removefirst(_:)-1pxgx.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeFirst(Int)](slice/removefirst(_:)-7hjja.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](slice/removelast-5mmgh.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](slice/removelast-wsbc.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](slice/removelast(_:)-75mgx.md)
  Removes the specified number of elements from the end of the collection.
- [func removeLast(Int)](slice/removelast(_:)-fxm2.md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange<R>(R)](slice/removesubrange(_:)-1y2qo.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange(Range<Slice<Base>.Index>)](slice/removesubrange(_:)-7s7x9.md)
  Removes the specified subrange of elements from the collection.
- [func removeSubrange(Range<Self.Index>)](slice/removesubrange(_:)-8m66i.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubranges(RangeSet<Self.Index>)](slice/removesubranges(_:)-2ncra.md)
  Removes the elements at the given indices.
- [func replaceSubrange<C>(Range<Self.Index>, with: C)](slice/replacesubrange(_:with:)-8l6gb.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C, R>(R, with: C)](slice/replacesubrange(_:with:)-9le44.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C>(Range<Slice<Base>.Index>, with: C)](slice/replacesubrange(_:with:)-zwfk.md)
  Replaces the specified subrange of elements with the given collection.
- [func reserveCapacity(Int)](slice/reservecapacity(_:).md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/rangereplaceablecollection-implementations)*