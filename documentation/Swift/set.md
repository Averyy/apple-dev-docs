# Set

**Framework**: Swift  
**Kind**: struct

An unordered collection of unique elements.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
struct Set<Element> where Element : Hashable
```

#### Overview

You use a set instead of an array when you need to test efficiently for membership and you aren’t concerned with the order of the elements in the collection, or when you need to ensure that each element appears only once in a collection.

You can create a set with any element type that conforms to the `Hashable` protocol. By default, most types in the standard library are hashable, including strings, numeric and Boolean types, enumeration cases without associated values, and even sets themselves.

Swift makes it as easy to create a new set as to create a new array. Simply assign an array literal to a variable or constant with the `Set` type specified.

```swift
let ingredients: Set = ["cocoa beans", "sugar", "cocoa butter", "salt"]
if ingredients.contains("sugar") {
    print("No thanks, too sweet.")
}
// Prints "No thanks, too sweet."
```

### Set Operations

Sets provide a suite of mathematical set operations. For example, you can efficiently test a set for membership of an element or check its intersection with another set:

- Use the `contains(_:)` method to test whether a set contains a specific element.
- Use the “equal to” operator (`==`) to test whether two sets contain the same elements.
- Use the `isSubset(of:)` method to test whether a set contains all the elements of another set or sequence.
- Use the `isSuperset(of:)` method to test whether all elements of a set are contained in another set or sequence.
- Use the `isStrictSubset(of:)` and `isStrictSuperset(of:)` methods to test whether a set is a subset or superset of, but not equal to, another set.
- Use the `isDisjoint(with:)` method to test whether a set has any elements in common with another set.

You can also combine, exclude, or subtract the elements of two sets:

- Use the `union(_:)` method to create a new set with the elements of a set and another set or sequence.
- Use the `intersection(_:)` method to create a new set with only the elements common to a set and another set or sequence.
- Use the `symmetricDifference(_:)` method to create a new set with the elements that are in either a set or another set or sequence, but not in both.
- Use the `subtracting(_:)` method to create a new set with the elements of a set that are not also in another set or sequence.

You can modify a set in place by using these methods’ mutating counterparts: `formUnion(_:)`, `formIntersection(_:)`, `formSymmetricDifference(_:)`, and `subtract(_:)`.

Set operations are not limited to use with other sets. Instead, you can perform set operations with another set, an array, or any other sequence type.

```swift
var primes: Set = [2, 3, 5, 7]

// Tests whether primes is a subset of a Range<Int>
print(primes.isSubset(of: 0..<10))
// Prints "true"

// Performs an intersection with an Array<Int>
let favoriteNumbers = [5, 7, 15, 21]
print(primes.intersection(favoriteNumbers))
// Prints "[5, 7]"
```

### Sequence and Collection Operations

In addition to the `Set` type’s set operations, you can use any nonmutating sequence or collection methods with a set.

```swift
if primes.isEmpty {
    print("No primes!")
} else {
    print("We have \(primes.count) primes.")
}
// Prints "We have 4 primes."

let primesSum = primes.reduce(0, +)
// 'primesSum' == 17

let primeStrings = primes.sorted().map(String.init)
// 'primeStrings' == ["2", "3", "5", "7"]
```

You can iterate through a set’s unordered elements with a `for`-`in` loop.

```swift
for number in primes {
    print(number)
}
// Prints "5"
// Prints "7"
// Prints "2"
// Prints "3"
```

Many sequence and collection operations return an array or a type-erasing collection wrapper instead of a set. To restore efficient set operations, create a new set from the result.

```swift
let primesStrings = primes.map(String.init)
// 'primesStrings' is of type Array<String>
let primesStringsSet = Set(primes.map(String.init))
// 'primesStringsSet' is of type Set<String>
```

### Bridging Between Set and Nsset

You can bridge between `Set` and `NSSet` using the `as` operator. For bridging to be possible, the `Element` type of a set must be a class, an `@objc` protocol (a protocol imported from Objective-C or marked with the `@objc` attribute), or a type that bridges to a Foundation type.

Bridging from `Set` to `NSSet` always takes O(1) time and space. When the set’s `Element` type is neither a class nor an `@objc` protocol, any required bridging of elements occurs at the first access of each element, so the first operation that uses the contents of the set (for example, a membership test) can take O().

Bridging from `NSSet` to `Set` first calls the `copy(with:)` method (`- copyWithZone:` in Objective-C) on the set to get an immutable copy and then performs additional Swift bookkeeping work that takes O(1) time. For instances of `NSSet` that are already immutable, `copy(with:)` returns the same set in constant time; otherwise, the copying performance is unspecified. The instances of `NSSet` and `Set` share buffer using the same copy-on-write optimization that is used when two instances of `Set` share buffer.

## Topics

### Creating a Set
- [init()](set/init.md)
  Creates an empty set.
- [init(minimumCapacity: Int)](set/init(minimumcapacity:).md)
  Creates an empty set with preallocated space for at least the specified number of elements.
- [init<S>(S)](set/init(_:)-9cgks.md)
  Creates a new set from a finite sequence of items.
- [init<Source>(Source)](set/init(_:).md)
  Creates a new set from a finite sequence of items.
### Inspecting a Set
- [var isEmpty: Bool](set/isempty.md)
  A Boolean value that indicates whether the set is empty.
- [var count: Int](set/count.md)
  The number of elements in the set.
- [var capacity: Int](set/capacity.md)
  The total number of elements that the set can contain without allocating new storage.
### Testing for Membership
- [func contains(Element) -> Bool](set/contains(_:).md)
  Returns a Boolean value that indicates whether the given element exists in the set.
### Adding Elements
- [func insert(Element) -> (inserted: Bool, memberAfterInsert: Element)](set/insert(_:)-nads.md)
  Inserts the given element in the set if it is not already present.
- [func insert<ConcreteElement>(ConcreteElement) -> (inserted: Bool, memberAfterInsert: ConcreteElement)](set/insert(_:)-yar4.md)
- [func update(with: Element) -> Element?](set/update(with:)-2n6tk.md)
  Inserts the given element into the set unconditionally.
- [func update<ConcreteElement>(with: ConcreteElement) -> ConcreteElement?](set/update(with:)-7r2g.md)
- [func reserveCapacity(Int)](set/reservecapacity(_:).md)
  Reserves enough space to store the specified number of elements.
### Removing Elements
- [func filter((Element) throws -> Bool) rethrows -> Set<Element>](set/filter(_:).md)
  Returns a new set containing the elements of the set that satisfy the given predicate.
- [func remove(Element) -> Element?](set/remove(_:)-8p2tv.md)
  Removes the specified element from the set.
- [func remove<ConcreteElement>(ConcreteElement) -> ConcreteElement?](set/remove(_:)-4d3i1.md)
- [func removeFirst() -> Element](set/removefirst.md)
  Removes the first element of the set.
- [func remove(at: Set<Element>.Index) -> Element](set/remove(at:).md)
  Removes the element at the given index of the set.
- [func removeAll(keepingCapacity: Bool)](set/removeall(keepingcapacity:).md)
  Removes all members from the set.
### Combining Sets
- [func union<S>(S) -> Set<Element>](set/union(_:).md)
  Returns a new set with the elements of both this set and the given sequence.
- [func formUnion<S>(S)](set/formunion(_:).md)
  Inserts the elements of the given sequence into the set.
- [func intersection(Set<Element>) -> Set<Element>](set/intersection(_:)-1zh8f.md)
  Returns a new set with the elements that are common to both this set and the given sequence.
- [func intersection<S>(S) -> Set<Element>](set/intersection(_:)-6uts9.md)
  Returns a new set with the elements that are common to both this set and the given sequence.
- [func formIntersection<S>(S)](set/formintersection(_:).md)
  Removes the elements of the set that aren’t also in the given sequence.
- [func symmetricDifference<S>(S) -> Set<Element>](set/symmetricdifference(_:).md)
  Returns a new set with the elements that are either in this set or in the given sequence, but not in both.
- [func formSymmetricDifference(Set<Element>)](set/formsymmetricdifference(_:)-22p0m.md)
  Removes the elements of the set that are also in the given sequence and adds the members of the sequence that are not already in the set.
- [func formSymmetricDifference<S>(S)](set/formsymmetricdifference(_:)-5u38b.md)
  Replace this set with the elements contained in this set or the given set, but not both.
- [func subtract(Set<Element>)](set/subtract(_:)-8gc48.md)
  Removes the elements of the given set from this set.
- [func subtract<S>(S)](set/subtract(_:)-7cd3y.md)
  Removes the elements of the given sequence from the set.
- [func subtracting(Set<Element>) -> Set<Element>](set/subtracting(_:)-3n4lc.md)
  Returns a new set containing the elements of this set that do not occur in the given set.
- [func subtracting<S>(S) -> Set<Element>](set/subtracting(_:)-2qge3.md)
  Returns a new set containing the elements of this set that do not occur in the given sequence.
### Comparing Sets
- [static func == (Set<Element>, Set<Element>) -> Bool](set/==(_:_:).md)
  Returns a Boolean value indicating whether two sets have equal elements.
- [static func != (Self, Self) -> Bool](set/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func isSubset(of: Set<Element>) -> Bool](set/issubset(of:)-1d7pp.md)
  Returns a Boolean value that indicates whether this set is a subset of the given set.
- [func isSubset<S>(of: S) -> Bool](set/issubset(of:)-6qyo5.md)
  Returns a Boolean value that indicates whether the set is a subset of the given sequence.
- [func isStrictSubset(of: Set<Element>) -> Bool](set/isstrictsubset(of:)-96vc3.md)
  Returns a Boolean value that indicates whether the set is a strict subset of the given sequence.
- [func isStrictSubset<S>(of: S) -> Bool](set/isstrictsubset(of:)-787sx.md)
  Returns a Boolean value that indicates whether the set is a strict subset of the given sequence.
- [func isSuperset(of: Set<Element>) -> Bool](set/issuperset(of:)-9iz62.md)
  Returns a Boolean value that indicates whether this set is a superset of the given set.
- [func isSuperset<S>(of: S) -> Bool](set/issuperset(of:)-90hri.md)
  Returns a Boolean value that indicates whether the set is a superset of the given sequence.
- [func isStrictSuperset(of: Set<Element>) -> Bool](set/isstrictsuperset(of:)-4d27m.md)
  Returns a Boolean value that indicates whether the set is a strict superset of the given sequence.
- [func isStrictSuperset<S>(of: S) -> Bool](set/isstrictsuperset(of:)-58ejg.md)
  Returns a Boolean value that indicates whether the set is a strict superset of the given sequence.
- [func isDisjoint(with: Set<Element>) -> Bool](set/isdisjoint(with:)-8ngmk.md)
  Returns a Boolean value that indicates whether this set has no members in common with the given set.
- [func isDisjoint<S>(with: S) -> Bool](set/isdisjoint(with:)-2onid.md)
  Returns a Boolean value that indicates whether the set has no members in common with the given sequence.
### Accessing Individual Elements
- [var first: Self.Element?](set/first.md)
  The first element of the collection.
- [func randomElement() -> Self.Element?](set/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](set/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
### Finding Elements
- [subscript(Set<Element>.Index) -> Element](set/subscript(_:).md)
  Accesses the member at the given position.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](set/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](set/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](set/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func firstIndex(of: Element) -> Set<Element>.Index?](set/firstindex(of:).md)
  Returns the index of the given element in the set, or `nil` if the element is not a member of the set.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](set/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func index(of: Self.Element) -> Self.Index?](set/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func min() -> Self.Element?](set/min.md)
  Returns the minimum element in the sequence.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](set/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func max() -> Self.Element?](set/max.md)
  Returns the maximum element in the sequence.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](set/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
### Transforming a Set
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](set/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](set/flatmap(_:)-i3my.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](set/flatmap(_:)-6chuh.md)
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](set/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](set/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func sorted() -> [Self.Element]](set/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](set/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func shuffled() -> [Self.Element]](set/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](set/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [var lazy: LazySequence<Self>](set/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
### Iterating over a Set
- [func enumerated() -> EnumeratedSequence<Self>](set/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func forEach((Self.Element) throws -> Void) rethrows](set/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func makeIterator() -> Set<Element>.Iterator](set/makeiterator.md)
  Returns an iterator over the members of the set.
- [var underestimatedCount: Int](set/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Performing Collection Operations
- [Order Dependent Operations on Set](order-dependent-operations-on-set.md)
  Perform order-dependent operations common to all collections, as implemented for `Set`.
### Encoding and Decoding
- [func encode(to: any Encoder) throws](set/encode(to:).md)
  Encodes the elements of this set into the given encoder in an unkeyed container.
- [init(from: any Decoder) throws](set/init(from:).md)
  Creates a new set by decoding from the given decoder.
### Describing a Set
- [func hash(into: inout Hasher)](set/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var description: String](set/description.md)
  A string that represents the contents of the set.
- [var debugDescription: String](set/debugdescription.md)
  A string that represents the contents of the set, suitable for debugging.
- [var customMirror: Mirror](set/custommirror.md)
  A mirror that reflects the set.
### Reference Types
- [class NSSet](../Foundation/NSSet.md)
  A static, unordered collection of unique objects.
- [class NSMutableSet](../Foundation/NSMutableSet.md)
  A dynamic unordered collection of unique objects.
### Supporting Types
- [struct Index](set/index.md)
  The position of an element in a set.
- [struct Iterator](set/iterator.md)
  An iterator over the members of a `Set<Element>`.
### Infrequently Used Functionality
- [init(arrayLiteral: Element...)](set/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](set/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
### Type Aliases
- [typealias Specification](set/specification.md)
- [typealias UnderlyingSequence](set/underlyingsequence.md)
- [typealias UnwrappedType](set/unwrappedtype.md)
- [typealias ValueType](set/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](set/defaultresolverspecification.md)
### Default Implementations
- [Collection Implementations](set/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](set/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](set/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](set/customstringconvertible-implementations.md)
- [Decodable Implementations](set/decodable-implementations.md)
- [Encodable Implementations](set/encodable-implementations.md)
- [Equatable Implementations](set/equatable-implementations.md)
- [ExpressibleByArrayLiteral Implementations](set/expressiblebyarrayliteral-implementations.md)
- [Hashable Implementations](set/hashable-implementations.md)
- [Sequence Implementations](set/sequence-implementations.md)
- [SetAlgebra Implementations](set/setalgebra-implementations.md)

## Relationships

### Conforms To
- [CVarArg](cvararg.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [ExpressibleByArrayLiteral](expressiblebyarrayliteral.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [Sequence](sequence.md)
- [SetAlgebra](setalgebra.md)

## See Also

- [protocol OptionSet](optionset.md)
  A type that presents a mathematical set interface to a bit set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set)*