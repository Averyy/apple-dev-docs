# RangeReplaceableCollection Implementations

**Framework**: System

## Topics

### Operators
- [static func + <Other>(Self, Other) -> Self](filepath/componentview/+(_:_:)-4pqh7.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func + <Other>(Self, Other) -> Self](filepath/componentview/+(_:_:)-6noxc.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func + <Other>(Other, Self) -> Self](filepath/componentview/+(_:_:)-8qw31.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func += <Other>(inout Self, Other)](filepath/componentview/+=(_:_:).md)
  Appends the elements of a sequence to a range-replaceable collection.
### Initializers
- [init()](filepath/componentview/init.md)
  Creates a new, empty collection.
- [init<S>(S)](filepath/componentview/init(_:).md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init(repeating: Self.Element, count: Int)](filepath/componentview/init(repeating:count:).md)
  Creates a new collection containing the specified number of a single, repeated value.
### Instance Methods
- [func append(Self.Element)](filepath/componentview/append(_:).md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](filepath/componentview/append(contentsof:).md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func applying(CollectionDifference<Self.Element>) -> Self?](filepath/componentview/applying(_:).md)
  Applies the given difference to this collection.
- [func filter((Self.Element) throws -> Bool) rethrows -> Self](filepath/componentview/filter(_:).md)
  Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [func insert(Self.Element, at: Self.Index)](filepath/componentview/insert(_:at:).md)
  Inserts a new element into the collection at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](filepath/componentview/insert(contentsof:at:).md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func popLast() -> Self.Element?](filepath/componentview/poplast.md)
  Removes and returns the last element of the collection.
- [func remove(at: Self.Index) -> Self.Element](filepath/componentview/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](filepath/componentview/removeall(keepingcapacity:).md)
  Removes all elements from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](filepath/componentview/removeall(where:).md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](filepath/componentview/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](filepath/componentview/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](filepath/componentview/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](filepath/componentview/removelast(_:).md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange(Range<Self.Index>)](filepath/componentview/removesubrange(_:)-4c2tk.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](filepath/componentview/removesubrange(_:)-6mqn1.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubranges(RangeSet<Self.Index>)](filepath/componentview/removesubranges(_:).md)
  Removes the elements at the given indices.
- [func replace<C, Replacement>(C, with: Replacement, maxReplacements: Int)](filepath/componentview/replace(_:with:maxreplacements:).md)
  Replaces all occurrences of a target sequence with a given collection
- [func replaceSubrange<C>(Range<FilePath.ComponentView.Index>, with: C)](filepath/componentview/replacesubrange(_:with:).md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C, R>(R, with: C)](filepath/componentview/replacesubrange(_:with:)-6ztd8.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C>(Range<Self.Index>, with: C)](filepath/componentview/replacesubrange(_:with:)-9mv34.md)
  Replaces the specified subrange of elements with the given collection.
- [func replacing<C, Replacement>(C, with: Replacement, maxReplacements: Int) -> Self](filepath/componentview/replacing(_:with:maxreplacements:).md)
  Returns a new collection in which all occurrences of a target sequence are replaced by another collection.
- [func replacing<C, Replacement>(C, with: Replacement, subrange: Range<Self.Index>, maxReplacements: Int) -> Self](filepath/componentview/replacing(_:with:subrange:maxreplacements:).md)
  Returns a new collection in which all occurrences of a target sequence are replaced by another collection.
- [func reserveCapacity(Int)](filepath/componentview/reservecapacity(_:).md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.
- [func trimPrefix<Prefix>(Prefix)](filepath/componentview/trimprefix(_:).md)
  Removes `prefix` from the start of the collection.
- [func trimPrefix(while: (Self.Element) throws -> Bool) rethrows](filepath/componentview/trimprefix(while:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/rangereplaceablecollection-implementations)*