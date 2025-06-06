# RangeReplaceableCollection Implementations

**Framework**: Swift

## Topics

### Operators
- [static func + <Other>(Other, Self) -> Self](string/+(_:_:)-6h59y.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](string/+(_:_:)-9fm57.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func + <Other>(Self, Other) -> Self](string/+(_:_:)-n329.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func += <Other>(inout Self, Other)](string/+=(_:_:)-676gx.md)
  Appends the elements of a sequence to a range-replaceable collection.
### Initializers
- [init<S>(S)](string/init(_:)-1ip93.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init<S>(S)](string/init(_:)-8og6g.md)
  Creates a new string containing the characters in the given sequence.
- [init(repeating: Character, count: Int)](string/init(repeating:count:)-11bpi.md)
  Creates a string representing the given character repeated the specified number of times.
- [init(repeating: Self.Element, count: Int)](string/init(repeating:count:)-5y5em.md)
  Creates a new collection containing the specified number of a single, repeated value.
### Instance Methods
- [func append(Self.Element)](string/append(_:)-1re5n.md)
  Adds an element to the end of the collection.
- [func append(Character)](string/append(_:)-4xi3j.md)
  Appends the given character to the string.
- [func append<S>(contentsOf: S)](string/append(contentsof:)-7est5.md)
  Appends the characters in the given sequence to the string.
- [func append<S>(contentsOf: S)](string/append(contentsof:)-9foms.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func applying(CollectionDifference<Self.Element>) -> Self?](string/applying(_:).md)
  Applies the given difference to this collection.
- [func filter((Self.Element) throws -> Bool) rethrows -> Self](string/filter(_:).md)
  Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [func insert(Character, at: String.Index)](string/insert(_:at:).md)
  Inserts a new character at the specified position.
- [func insert(Self.Element, at: Self.Index)](string/insert(_:at:)-88yqh.md)
  Inserts a new element into the collection at the specified position.
- [func insert<S>(contentsOf: S, at: String.Index)](string/insert(contentsof:at:).md)
  Inserts a collection of characters at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](string/insert(contentsof:at:)-rdu9.md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func popLast() -> Self.Element?](string/poplast.md)
  Removes and returns the last element of the collection.
- [func remove(at: String.Index) -> Character](string/remove(at:).md)
  Removes and returns the character at the specified position.
- [func remove(at: Self.Index) -> Self.Element](string/remove(at:)-5g0wm.md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](string/removeall(keepingcapacity:).md)
  Replaces this string with the empty string.
- [func removeAll(keepingCapacity: Bool)](string/removeall(keepingcapacity:)-6xw7h.md)
  Removes all elements from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](string/removeall(where:).md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](string/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](string/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](string/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](string/removelast(_:).md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange(Range<String.Index>)](string/removesubrange(_:).md)
  Removes the characters in the given range.
- [func removeSubrange(Range<Self.Index>)](string/removesubrange(_:)-8maxn.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](string/removesubrange(_:)-9twng.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubranges(RangeSet<Self.Index>)](string/removesubranges(_:).md)
  Removes the elements at the given indices.
- [func replaceSubrange<C>(Range<String.Index>, with: C)](string/replacesubrange(_:with:).md)
  Replaces the text within the specified bounds with the given characters.
- [func replaceSubrange<C>(Range<Self.Index>, with: C)](string/replacesubrange(_:with:)-3hkd6.md)
  Replaces the specified subrange of elements with the given collection.
- [func replaceSubrange<C, R>(R, with: C)](string/replacesubrange(_:with:)-72947.md)
  Replaces the specified subrange of elements with the given collection.
- [func reserveCapacity(Int)](string/reservecapacity(_:).md)
  Reserves enough space in the string’s underlying storage to store the specified number of ASCII characters.
- [func reserveCapacity(Int)](string/reservecapacity(_:)-8lw57.md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/rangereplaceablecollection-implementations)*