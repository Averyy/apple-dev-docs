# RangeReplaceableCollection Implementations

**Framework**: RealityKit

## Topics

### Operators
- [static func + <Other>(Self, Other) -> Self](physicsjoints/+(_:_:)-15x1i.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func + <Other>(Self, Other) -> Self](physicsjoints/+(_:_:)-1i2xu.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func + <Other>(Other, Self) -> Self](physicsjoints/+(_:_:)-8yudc.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func += <Other>(inout Self, Other)](physicsjoints/+=(_:_:).md)
  Appends the elements of a sequence to a range-replaceable collection.
### Initializers
- [init<S>(S)](physicsjoints/init(_:)-9xnhj.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init(repeating: Self.Element, count: Int)](physicsjoints/init(repeating:count:).md)
  Creates a new collection containing the specified number of a single, repeated value.
### Instance Methods
- [func append(Self.Element)](physicsjoints/append(_:).md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](physicsjoints/append(contentsof:).md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func applying(CollectionDifference<Self.Element>) -> Self?](physicsjoints/applying(_:).md)
  Applies the given difference to this collection.
- [func filter((Self.Element) throws -> Bool) rethrows -> Self](physicsjoints/filter(_:).md)
  Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [func insert(Self.Element, at: Self.Index)](physicsjoints/insert(_:at:).md)
  Inserts a new element into the collection at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](physicsjoints/insert(contentsof:at:).md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func popLast() -> Self.Element?](physicsjoints/poplast.md)
  Removes and returns the last element of the collection.
- [func remove(at: Self.Index) -> Self.Element](physicsjoints/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](physicsjoints/removeall(keepingcapacity:).md)
  Removes all elements from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](physicsjoints/removeall(where:)-4sfj.md)
  Removes all the elements that satisfy the given predicate.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](physicsjoints/removeall(where:)-7w7sy.md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](physicsjoints/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](physicsjoints/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](physicsjoints/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](physicsjoints/removelast(_:).md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange(Range<Self.Index>)](physicsjoints/removesubrange(_:)-38eqc.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](physicsjoints/removesubrange(_:)-81ykj.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubranges(RangeSet<Self.Index>)](physicsjoints/removesubranges(_:)-2n5d2.md)
  Removes the elements at the given indices.
- [func replaceSubrange<C, R>(R, with: C)](physicsjoints/replacesubrange(_:with:)-5fqy9.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C>(Range<Self.Index>, with: C)](physicsjoints/replacesubrange(_:with:)-71jw9.md)
  Replaces the specified subrange of elements with the given collection.
- [func reserveCapacity(Int)](physicsjoints/reservecapacity(_:).md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.
- [func trimPrefix(while: (Self.Element) throws -> Bool) rethrows](physicsjoints/trimprefix(while:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsjoints/rangereplaceablecollection-implementations)*