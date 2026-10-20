# RangeReplaceableCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Operators
- [static func + <Other>(Self, Other) -> Self](./plus%28_,_%29-298al.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func + <Other>(Other, Self) -> Self](./plus%28_,_%29-4resp.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](./plus%28_,_%29-99wuu.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func += <Other>(inout Self, Other)](./pluseq%28_,_%29.md)
  Appends the elements of a sequence to a range-replaceable collection.
### Initializers
- [init()](./init%28%29.md)
  Creates a new, empty collection.
- [init<S>(S)](./init%28_%29.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init<S>(S)](./init%28_%29-81eoy.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init(repeating: Base.Element, count: Int)](./init%28repeating,count%29.md)
  Creates a new collection containing the specified number of a single, repeated value.
- [init(repeating: Self.Element, count: Int)](./init%28repeating,count%29-6ps2q.md)
  Creates a new collection containing the specified number of a single, repeated value.
### Instance Methods
- [func append(Self.Element)](./append%28_%29.md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](./append%28contentsof%29.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func applying(CollectionDifference<Self.Element>) -> Self?](./applying%28_%29.md)
  Applies the given difference to this collection.
- [func filter<E>((Self.Element) throws(E) -> Bool) throws(E) -> Self](./filter%28_%29-9rk6d.md)
  Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [func insert(Base.Element, at: Slice<Base>.Index)](./insert%28_,at%29-6sg0.md)
  Inserts a new element into the collection at the specified position.
- [func insert(Self.Element, at: Self.Index)](./insert%28_,at%29-8i1dc.md)
  Inserts a new element into the collection at the specified position.
- [func insert<S>(contentsOf: S, at: Slice<Base>.Index)](./insert%28contentsof,at%29-25pep.md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](./insert%28contentsof,at%29-2xj4m.md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func popLast() -> Self.Element?](./poplast%28%29-30m9y.md)
  Removes and returns the last element of the collection.
- [func popLast() -> Self.Element?](./poplast%28%29-4rely.md)
  Removes and returns the last element of the collection.
- [func remove(at: Slice<Base>.Index) -> Base.Element](./remove%28at%29-7ep9e.md)
  Removes and returns the element at the specified position.
- [func remove(at: Self.Index) -> Self.Element](./remove%28at%29-7xja6.md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](./removeall%28keepingcapacity%29.md)
  Removes all elements from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](./removeall%28where%29-26lr3.md)
  Removes all the elements that satisfy the given predicate.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](./removeall%28where%29-9u7g.md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](./removefirst%28%29-1iayr.md)
  Removes and returns the first element of the collection.
- [func removeFirst() -> Self.Element](./removefirst%28%29-3eija.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](./removefirst%28_%29-1pxgx.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeFirst(Int)](./removefirst%28_%29-7hjja.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](./removelast%28%29-5mmgh.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](./removelast%28%29-wsbc.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](./removelast%28_%29-75mgx.md)
  Removes the specified number of elements from the end of the collection.
- [func removeLast(Int)](./removelast%28_%29-fxm2.md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange<R>(R)](./removesubrange%28_%29-1y2qo.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange(Range<Slice<Base>.Index>)](./removesubrange%28_%29-7s7x9.md)
  Removes the specified subrange of elements from the collection.
- [func removeSubrange(Range<Self.Index>)](./removesubrange%28_%29-8m66i.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubranges(RangeSet<Self.Index>)](./removesubranges%28_%29-2ncra.md)
  Removes the elements at the given indices.
- [func replaceSubrange<C>(Range<Self.Index>, with: C)](./replacesubrange%28_,with%29-8l6gb.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C, R>(R, with: C)](./replacesubrange%28_,with%29-9le44.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C>(Range<Slice<Base>.Index>, with: C)](./replacesubrange%28_,with%29-zwfk.md)
  Replaces the specified subrange of elements with the given collection.
- [func reserveCapacity(Int)](./reservecapacity%28_%29.md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/rangereplaceablecollection-implementations)*