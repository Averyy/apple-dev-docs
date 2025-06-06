# RangeReplaceableCollection Implementations

**Framework**: Swift

## Topics

### Operators
- [static func + <Other>(Other, Self) -> Self](substring/unicodescalarview/+(_:_:)-1c1pd.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](substring/unicodescalarview/+(_:_:)-1p67y.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func + <Other>(Self, Other) -> Self](substring/unicodescalarview/+(_:_:)-9qjws.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func += <Other>(inout Self, Other)](substring/unicodescalarview/+=(_:_:).md)
  Appends the elements of a sequence to a range-replaceable collection.
### Initializers
- [init()](substring/unicodescalarview/init.md)
  Creates a new, empty collection.
- [init<S>(S)](substring/unicodescalarview/init(_:).md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init(repeating: Self.Element, count: Int)](substring/unicodescalarview/init(repeating:count:).md)
  Creates a new collection containing the specified number of a single, repeated value.
### Instance Methods
- [func append(Self.Element)](substring/unicodescalarview/append(_:).md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](substring/unicodescalarview/append(contentsof:).md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func applying(CollectionDifference<Self.Element>) -> Self?](substring/unicodescalarview/applying(_:).md)
  Applies the given difference to this collection.
- [func filter((Self.Element) throws -> Bool) rethrows -> Self](substring/unicodescalarview/filter(_:).md)
  Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [func insert(Self.Element, at: Self.Index)](substring/unicodescalarview/insert(_:at:).md)
  Inserts a new element into the collection at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](substring/unicodescalarview/insert(contentsof:at:).md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func popLast() -> Self.Element?](substring/unicodescalarview/poplast-46voy.md)
  Removes and returns the last element of the collection.
- [func popLast() -> Self.Element?](substring/unicodescalarview/poplast-7zgh4.md)
  Removes and returns the last element of the collection.
- [func remove(at: Self.Index) -> Self.Element](substring/unicodescalarview/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](substring/unicodescalarview/removeall(keepingcapacity:).md)
  Removes all elements from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](substring/unicodescalarview/removeall(where:).md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](substring/unicodescalarview/removefirst-2a3ja.md)
  Removes and returns the first element of the collection.
- [func removeFirst() -> Self.Element](substring/unicodescalarview/removefirst-5t2ib.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](substring/unicodescalarview/removefirst(_:)-2lfkb.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeFirst(Int)](substring/unicodescalarview/removefirst(_:)-5314w.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](substring/unicodescalarview/removelast-3izvn.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](substring/unicodescalarview/removelast-75qy7.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](substring/unicodescalarview/removelast(_:)-30fw5.md)
  Removes the specified number of elements from the end of the collection.
- [func removeLast(Int)](substring/unicodescalarview/removelast(_:)-74qgu.md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange<R>(R)](substring/unicodescalarview/removesubrange(_:)-2qm37.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange(Range<Self.Index>)](substring/unicodescalarview/removesubrange(_:)-5c1al.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubranges(RangeSet<Self.Index>)](substring/unicodescalarview/removesubranges(_:).md)
  Removes the elements at the given indices.
- [func replaceSubrange<C>(Range<Substring.UnicodeScalarView.Index>, with: C)](substring/unicodescalarview/replacesubrange(_:with:).md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C>(Range<Self.Index>, with: C)](substring/unicodescalarview/replacesubrange(_:with:)-4kmx6.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C, R>(R, with: C)](substring/unicodescalarview/replacesubrange(_:with:)-7xjpm.md)
  Replaces the specified subrange of elements with the given collection.
- [func reserveCapacity(Int)](substring/unicodescalarview/reservecapacity(_:).md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/unicodescalarview/rangereplaceablecollection-implementations)*