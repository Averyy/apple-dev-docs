# RangeReplaceableCollection Implementations

**Framework**: Swift

## Topics

### Operators
- [static func + <Other>(Other, Self) -> Self](string/unicodescalarview/+(_:_:)-61ucr.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](string/unicodescalarview/+(_:_:)-8g18j.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func + <Other>(Self, Other) -> Self](string/unicodescalarview/+(_:_:)-929xp.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func += <Other>(inout Self, Other)](string/unicodescalarview/+=(_:_:).md)
  Appends the elements of a sequence to a range-replaceable collection.
### Initializers
- [init()](string/unicodescalarview/init.md)
  Creates an empty view instance.
- [init<S>(S)](string/unicodescalarview/init(_:).md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init(repeating: Self.Element, count: Int)](string/unicodescalarview/init(repeating:count:).md)
  Creates a new collection containing the specified number of a single, repeated value.
### Instance Methods
- [func append(Unicode.Scalar)](string/unicodescalarview/append(_:).md)
  Appends the given Unicode scalar to the view.
- [func append(Self.Element)](string/unicodescalarview/append(_:)-5uy8n.md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](string/unicodescalarview/append(contentsof:).md)
  Appends the Unicode scalar values in the given sequence to the view.
- [func append<S>(contentsOf: S)](string/unicodescalarview/append(contentsof:)-ton6.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func applying(CollectionDifference<Self.Element>) -> Self?](string/unicodescalarview/applying(_:).md)
  Applies the given difference to this collection.
- [func filter((Self.Element) throws -> Bool) rethrows -> Self](string/unicodescalarview/filter(_:).md)
  Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [func insert(Self.Element, at: Self.Index)](string/unicodescalarview/insert(_:at:).md)
  Inserts a new element into the collection at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](string/unicodescalarview/insert(contentsof:at:).md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func popLast() -> Self.Element?](string/unicodescalarview/poplast.md)
  Removes and returns the last element of the collection.
- [func remove(at: Self.Index) -> Self.Element](string/unicodescalarview/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](string/unicodescalarview/removeall(keepingcapacity:).md)
  Removes all elements from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](string/unicodescalarview/removeall(where:).md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](string/unicodescalarview/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](string/unicodescalarview/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](string/unicodescalarview/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](string/unicodescalarview/removelast(_:).md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange<R>(R)](string/unicodescalarview/removesubrange(_:)-62wlg.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange(Range<Self.Index>)](string/unicodescalarview/removesubrange(_:)-6rv02.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubranges(RangeSet<Self.Index>)](string/unicodescalarview/removesubranges(_:).md)
  Removes the elements at the given indices.
- [func replaceSubrange<C>(Range<String.UnicodeScalarView.Index>, with: C)](string/unicodescalarview/replacesubrange(_:with:).md)
  Replaces the elements within the specified bounds with the given Unicode scalar values.
- [func replaceSubrange<C, R>(R, with: C)](string/unicodescalarview/replacesubrange(_:with:)-5z8uw.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C>(Range<Self.Index>, with: C)](string/unicodescalarview/replacesubrange(_:with:)-914bq.md)
  Replaces the specified subrange of elements with the given collection.
- [func reserveCapacity(Int)](string/unicodescalarview/reservecapacity(_:).md)
  Reserves enough space in the view’s underlying storage to store the specified number of ASCII characters.
- [func reserveCapacity(Int)](string/unicodescalarview/reservecapacity(_:)-4ygoa.md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/unicodescalarview/rangereplaceablecollection-implementations)*