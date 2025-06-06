# RangeReplaceableCollection Implementations

**Framework**: Swift

## Topics

### Operators
- [static func + <Other>(Other, Self) -> Self](array/+(_:_:)-6h58k.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](array/+(_:_:)-9fm5l.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func + <Other>(Self, Other) -> Self](array/+(_:_:)-n33n.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func += <Other>(inout Self, Other)](array/+=(_:_:)-676ib.md)
  Appends the elements of a sequence to a range-replaceable collection.
### Initializers
- [init()](array/init.md)
  Creates a new, empty array.
- [init<S>(S)](array/init(_:)-1ip9h.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init(repeating: Element, count: Int)](array/init(repeating:count:).md)
  Creates a new array containing the specified number of a single, repeated value.
- [init(repeating: Self.Element, count: Int)](array/init(repeating:count:)-5y5f0.md)
  Creates a new collection containing the specified number of a single, repeated value.
### Instance Methods
- [func append(Element)](array/append(_:).md)
  Adds a new element at the end of the array.
- [func append(Self.Element)](array/append(_:)-1re55.md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](array/append(contentsof:).md)
  Adds the elements of a sequence to the end of the array.
- [func append<S>(contentsOf: S)](array/append(contentsof:)-9foli.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func applying(CollectionDifference<Self.Element>) -> Self?](array/applying(_:).md)
  Applies the given difference to this collection.
- [func insert(Self.Element, at: Self.Index)](array/insert(_:at:)-88yqz.md)
  Inserts a new element into the collection at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](array/insert(contentsof:at:).md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func popLast() -> Self.Element?](array/poplast.md)
  Removes and returns the last element of the collection.
- [func remove(at: Self.Index) -> Self.Element](array/remove(at:)-5g0x0.md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](array/removeall(keepingcapacity:).md)
  Removes all elements from the array.
- [func removeAll(keepingCapacity: Bool)](array/removeall(keepingcapacity:)-6xw8v.md)
  Removes all elements from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](array/removeall(where:)-5k61r.md)
  Removes all the elements that satisfy the given predicate.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](array/removeall(where:)-6bd6r.md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](array/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](array/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](array/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](array/removelast(_:).md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange(Range<Self.Index>)](array/removesubrange(_:)-8may1.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](array/removesubrange(_:)-9twou.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubranges(RangeSet<Self.Index>)](array/removesubranges(_:)-5xi38.md)
  Removes the elements at the given indices.
- [func replaceSubrange<C>(Range<Int>, with: C)](array/replacesubrange(_:with:).md)
  Replaces a range of elements with the elements in the specified collection.
- [func replaceSubrange<C>(Range<Self.Index>, with: C)](array/replacesubrange(_:with:)-3hkdk.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C, R>(R, with: C)](array/replacesubrange(_:with:)-7293p.md)
  Replaces the specified subrange of elements with the given collection.
- [func reserveCapacity(Int)](array/reservecapacity(_:)-8lw3t.md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/rangereplaceablecollection-implementations)*