# RangeReplaceableCollection Implementations

**Framework**: Swift

## Topics

### Operators
- [static func + <Other>(Self, Other) -> Self](contiguousarray/+(_:_:)-1rz1t.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func + <Other>(Other, Self) -> Self](contiguousarray/+(_:_:)-3ntif.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](contiguousarray/+(_:_:)-5igl.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func += <Other>(inout Self, Other)](contiguousarray/+=(_:_:).md)
  Appends the elements of a sequence to a range-replaceable collection.
### Initializers
- [init()](contiguousarray/init.md)
  Creates a new, empty array.
- [init<S>(S)](contiguousarray/init(_:)-19zub.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init(repeating: Element, count: Int)](contiguousarray/init(repeating:count:).md)
  Creates a new array containing the specified number of a single, repeated value.
- [init(repeating: Self.Element, count: Int)](contiguousarray/init(repeating:count:)-47x84.md)
  Creates a new collection containing the specified number of a single, repeated value.
### Instance Methods
- [func append(Element)](contiguousarray/append(_:).md)
  Adds a new element at the end of the array.
- [func append(Self.Element)](contiguousarray/append(_:)-4na3g.md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](contiguousarray/append(contentsof:).md)
  Adds the elements of a sequence to the end of the array.
- [func append<S>(contentsOf: S)](contiguousarray/append(contentsof:)-66qjk.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func applying(CollectionDifference<Self.Element>) -> Self?](contiguousarray/applying(_:).md)
  Applies the given difference to this collection.
- [func insert(Self.Element, at: Self.Index)](contiguousarray/insert(_:at:)-81ye7.md)
  Inserts a new element into the collection at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](contiguousarray/insert(contentsof:at:).md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func popLast() -> Self.Element?](contiguousarray/poplast.md)
  Removes and returns the last element of the collection.
- [func remove(at: Self.Index) -> Self.Element](contiguousarray/remove(at:)-6yx8z.md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](contiguousarray/removeall(keepingcapacity:).md)
  Removes all elements from the array.
- [func removeAll(keepingCapacity: Bool)](contiguousarray/removeall(keepingcapacity:)-2onkd.md)
  Removes all elements from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](contiguousarray/removeall(where:)-3or72.md)
  Removes all the elements that satisfy the given predicate.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](contiguousarray/removeall(where:)-44y75.md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](contiguousarray/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](contiguousarray/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](contiguousarray/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](contiguousarray/removelast(_:).md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange(Range<Self.Index>)](contiguousarray/removesubrange(_:)-3k98x.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](contiguousarray/removesubrange(_:)-8cd5m.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubranges(RangeSet<Self.Index>)](contiguousarray/removesubranges(_:)-147en.md)
  Removes the elements at the given indices.
- [func replaceSubrange<C>(Range<Int>, with: C)](contiguousarray/replacesubrange(_:with:).md)
  Replaces a range of elements with the elements in the specified collection.
- [func replaceSubrange<C, R>(R, with: C)](contiguousarray/replacesubrange(_:with:)-4iomk.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C>(Range<Self.Index>, with: C)](contiguousarray/replacesubrange(_:with:)-95xhb.md)
  Replaces the specified subrange of elements with the given collection.
- [func reserveCapacity(Int)](contiguousarray/reservecapacity(_:)-4601w.md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/rangereplaceablecollection-implementations)*