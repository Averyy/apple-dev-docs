# RangeReplaceableCollection Implementations

**Framework**: Swift

## Topics

### Operators
- [static func + <Other>(Other, Self) -> Self](substring/+(_:_:)-6h592.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](substring/+(_:_:)-9fm63.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func + <Other>(Self, Other) -> Self](substring/+(_:_:)-n335.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func += <Other>(inout Self, Other)](substring/+=(_:_:).md)
  Appends the elements of a sequence to a range-replaceable collection.
### Initializers
- [init<S>(S)](substring/init(_:)-1ip9z.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init<S>(S)](substring/init(_:)-6lxbv.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init(repeating: Self.Element, count: Int)](substring/init(repeating:count:).md)
  Creates a new collection containing the specified number of a single, repeated value.
### Instance Methods
- [func append(Self.Element)](substring/append(_:).md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](substring/append(contentsof:).md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func append<S>(contentsOf: S)](substring/append(contentsof:)-9folw.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func applying(CollectionDifference<Self.Element>) -> Self?](substring/applying(_:).md)
  Applies the given difference to this collection.
- [func insert(Self.Element, at: Self.Index)](substring/insert(_:at:).md)
  Inserts a new element into the collection at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](substring/insert(contentsof:at:).md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func popLast() -> Self.Element?](substring/poplast-70a2x.md)
  Removes and returns the last element of the collection.
- [func popLast() -> Self.Element?](substring/poplast-nrp9.md)
  Removes and returns the last element of the collection.
- [func remove(at: Self.Index) -> Self.Element](substring/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](substring/removeall(keepingcapacity:).md)
  Removes all elements from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](substring/removeall(where:).md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](substring/removefirst-2cpd8.md)
  Removes and returns the first element of the collection.
- [func removeFirst() -> Self.Element](substring/removefirst-39om1.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](substring/removefirst(_:)-43evo.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeFirst(Int)](substring/removefirst(_:)-5s82s.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](substring/removelast-4kq76.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](substring/removelast-5b56p.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](substring/removelast(_:)-1xrzw.md)
  Removes the specified number of elements from the end of the collection.
- [func removeLast(Int)](substring/removelast(_:)-5ulmx.md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange(Range<Self.Index>)](substring/removesubrange(_:)-8mayj.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](substring/removesubrange(_:)-9twoc.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubranges(RangeSet<Self.Index>)](substring/removesubranges(_:).md)
  Removes the elements at the given indices.
- [func replaceSubrange<C>(Range<Self.Index>, with: C)](substring/replacesubrange(_:with:)-3hke2.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C>(Range<Substring.Index>, with: C)](substring/replacesubrange(_:with:)-5g58l.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C, R>(R, with: C)](substring/replacesubrange(_:with:)-7293b.md)
  Replaces the specified subrange of elements with the given collection.
- [func reserveCapacity(Int)](substring/reservecapacity(_:).md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/rangereplaceablecollection-implementations)*