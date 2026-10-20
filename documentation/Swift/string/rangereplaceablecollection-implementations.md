# RangeReplaceableCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Operators
- [static func + <Other>(Other, Self) -> Self](./plus%28_,_%29-6h59y.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](./plus%28_,_%29-9fm57.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func + <Other>(Self, Other) -> Self](./plus%28_,_%29-n329.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func += <Other>(inout Self, Other)](./pluseq%28_,_%29-676gx.md)
  Appends the elements of a sequence to a range-replaceable collection.
### Initializers
- [init<S>(S)](./init%28_%29-1ip93.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init<S>(S)](./init%28_%29-8og6g.md)
  Creates a new string containing the characters in the given sequence.
- [init(repeating: Character, count: Int)](./init%28repeating,count%29-11bpi.md)
  Creates a string representing the given character repeated the specified number of times.
- [init(repeating: Self.Element, count: Int)](./init%28repeating,count%29-5y5em.md)
  Creates a new collection containing the specified number of a single, repeated value.
### Instance Methods
- [func append(Self.Element)](./append%28_%29-1re5n.md)
  Adds an element to the end of the collection.
- [func append(Character)](./append%28_%29-4xi3j.md)
  Appends the given character to the string.
- [func append<S>(contentsOf: S)](./append%28contentsof%29-7est5.md)
  Appends the characters in the given sequence to the string.
- [func append<S>(contentsOf: S)](./append%28contentsof%29-9foms.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func applying(CollectionDifference<Self.Element>) -> Self?](./applying%28_%29.md)
  Applies the given difference to this collection.
- [func filter<E>((Self.Element) throws(E) -> Bool) throws(E) -> Self](./filter%28_%29-66nw7.md)
  Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [func insert(Character, at: String.Index)](./insert%28_,at%29.md)
  Inserts a new character at the specified position.
- [func insert(Self.Element, at: Self.Index)](./insert%28_,at%29-88yqh.md)
  Inserts a new element into the collection at the specified position.
- [func insert<S>(contentsOf: S, at: String.Index)](./insert%28contentsof,at%29.md)
  Inserts a collection of characters at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](./insert%28contentsof,at%29-rdu9.md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func popLast() -> Self.Element?](./poplast%28%29.md)
  Removes and returns the last element of the collection.
- [func remove(at: String.Index) -> Character](./remove%28at%29.md)
  Removes and returns the character at the specified position.
- [func remove(at: Self.Index) -> Self.Element](./remove%28at%29-5g0wm.md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](./removeall%28keepingcapacity%29.md)
  Replaces this string with the empty string.
- [func removeAll(keepingCapacity: Bool)](./removeall%28keepingcapacity%29-6xw7h.md)
  Removes all elements from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](./removeall%28where%29.md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](./removefirst%28%29.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](./removefirst%28_%29.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](./removelast%28%29.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](./removelast%28_%29.md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange(Range<String.Index>)](./removesubrange%28_%29.md)
  Removes the characters in the given range.
- [func removeSubrange(Range<Self.Index>)](./removesubrange%28_%29-8maxn.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](./removesubrange%28_%29-9twng.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubranges(RangeSet<Self.Index>)](./removesubranges%28_%29.md)
  Removes the elements at the given indices.
- [func replaceSubrange<C>(Range<String.Index>, with: C)](./replacesubrange%28_,with%29.md)
  Replaces the text within the specified bounds with the given characters.
- [func replaceSubrange<C>(Range<Self.Index>, with: C)](./replacesubrange%28_,with%29-3hkd6.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C, R>(R, with: C)](./replacesubrange%28_,with%29-72947.md)
  Replaces the specified subrange of elements with the given collection.
- [func reserveCapacity(Int)](./reservecapacity%28_%29.md)
  Reserves enough space in the string’s underlying storage to store the specified number of ASCII characters.
- [func reserveCapacity(Int)](./reservecapacity%28_%29-8lw57.md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/rangereplaceablecollection-implementations)*