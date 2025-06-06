# RangeReplaceableCollection Implementations

**Framework**: Swift

## Topics

### Operators
- [static func + <Other>(Self, Other) -> Self](arrayslice/+(_:_:)-2jvah.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func + <Other>(Other, Self) -> Self](arrayslice/+(_:_:)-3xq1b.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](arrayslice/+(_:_:)-8elcw.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func += <Other>(inout Self, Other)](arrayslice/+=(_:_:).md)
  Appends the elements of a sequence to a range-replaceable collection.
### Initializers
- [init()](arrayslice/init.md)
  Creates a new, empty array.
- [init<S>(S)](arrayslice/init(_:)-4qauj.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init(repeating: Element, count: Int)](arrayslice/init(repeating:count:).md)
  Creates a new array containing the specified number of a single, repeated value.
- [init(repeating: Self.Element, count: Int)](arrayslice/init(repeating:count:)-95f9t.md)
  Creates a new collection containing the specified number of a single, repeated value.
### Instance Methods
- [func append(Element)](arrayslice/append(_:).md)
  Adds a new element at the end of the array.
- [func append(Self.Element)](arrayslice/append(_:)-88nog.md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](arrayslice/append(contentsof:).md)
  Adds the elements of a sequence to the end of the array.
- [func append<S>(contentsOf: S)](arrayslice/append(contentsof:)-6pxfb.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func applying(CollectionDifference<Self.Element>) -> Self?](arrayslice/applying(_:).md)
  Applies the given difference to this collection.
- [func insert(Self.Element, at: Self.Index)](arrayslice/insert(_:at:)-2orxu.md)
  Inserts a new element into the collection at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](arrayslice/insert(contentsof:at:).md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func popLast() -> Self.Element?](arrayslice/poplast-225tk.md)
  Removes and returns the last element of the collection.
- [func popLast() -> Self.Element?](arrayslice/poplast-ftzx.md)
  Removes and returns the last element of the collection.
- [func remove(at: Self.Index) -> Self.Element](arrayslice/remove(at:)-8p8nf.md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](arrayslice/removeall(keepingcapacity:).md)
  Removes all elements from the array.
- [func removeAll(keepingCapacity: Bool)](arrayslice/removeall(keepingcapacity:)-1wh07.md)
  Removes all elements from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](arrayslice/removeall(where:)-10tcx.md)
  Removes all the elements that satisfy the given predicate.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](arrayslice/removeall(where:)-23c5i.md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](arrayslice/removefirst-60cu4.md)
  Removes and returns the first element of the collection.
- [func removeFirst() -> Self.Element](arrayslice/removefirst-svki.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](arrayslice/removefirst(_:)-285s6.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeFirst(Int)](arrayslice/removefirst(_:)-3up7n.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](arrayslice/removelast-67p7c.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](arrayslice/removelast-9iuw9.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](arrayslice/removelast(_:)-33c55.md)
  Removes the specified number of elements from the end of the collection.
- [func removeLast(Int)](arrayslice/removelast(_:)-5oepe.md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange<R>(R)](arrayslice/removesubrange(_:)-2zu9f.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange(Range<Self.Index>)](arrayslice/removesubrange(_:)-celt.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubranges(RangeSet<Self.Index>)](arrayslice/removesubranges(_:)-947o4.md)
  Removes the elements at the given indices.
- [func replaceSubrange<C>(Range<Int>, with: C)](arrayslice/replacesubrange(_:with:).md)
  Replaces a range of elements with the elements in the specified collection.
- [func replaceSubrange<C, R>(R, with: C)](arrayslice/replacesubrange(_:with:)-5g1qk.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C>(Range<Self.Index>, with: C)](arrayslice/replacesubrange(_:with:)-9rz4g.md)
  Replaces the specified subrange of elements with the given collection.
- [func reserveCapacity(Int)](arrayslice/reservecapacity(_:)-11kse.md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/arrayslice/rangereplaceablecollection-implementations)*