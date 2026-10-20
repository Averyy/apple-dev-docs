# RangeReplaceableCollection

**Framework**: Swift  
**Kind**: protocol  
**Role**: Protocol

A collection that supports replacement of an arbitrary subrange of elements with the elements of another collection.

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
protocol RangeReplaceableCollection<Element> : Collection where Self.SubSequence : RangeReplaceableCollection
```

#### Overview

Range-replaceable collections provide operations that insert and remove elements. For example, you can add elements to an array of strings by calling any of the inserting or appending operations that the `RangeReplaceableCollection` protocol defines.

```swift
var bugs = ["Aphid", "Damselfly"]
bugs.append("Earwig")
bugs.insert(contentsOf: ["Bumblebee", "Cicada"], at: 1)
print(bugs)
// Prints "["Aphid", "Bumblebee", "Cicada", "Damselfly", "Earwig"]"
```

Likewise, `RangeReplaceableCollection` types can remove one or more elements using a single operation.

```swift
bugs.removeLast()
bugs.removeSubrange(1...2)
print(bugs)
// Prints "["Aphid", "Damselfly"]"

bugs.removeAll()
print(bugs)
// Prints "[]"
```

Lastly, use the eponymous `replaceSubrange(_:with:)` method to replace a subrange of elements with the contents of another collection. Here, three elements in the middle of an array of integers are replaced by the five elements of a `Repeated<Int>` instance.

```swift
 var nums = [10, 20, 30, 40, 50]
 nums.replaceSubrange(1...3, with: repeatElement(1, count: 5))
 print(nums)
 // Prints "[10, 1, 1, 1, 1, 1, 50]"
```

### Conforming to the RangeReplaceableCollection Protocol

To add `RangeReplaceableCollection` conformance to your custom collection, add an empty initializer and the `replaceSubrange(_:with:)` method to your custom type. `RangeReplaceableCollection` provides default implementations of all its other methods using this initializer and method. For example, the `removeSubrange(_:)` method is implemented by calling `replaceSubrange(_:with:)` with an empty collection for the `newElements` parameter. You can override any of the protocol’s required methods to provide your own custom implementation.

## Topics

### Creating a New Collection
- [init()](./rangereplaceablecollection/init%28%29.md)
  Creates a new, empty collection.
### Adding Elements
- [func insert<S>(contentsOf: S, at: Self.Index)](./rangereplaceablecollection/insert%28contentsof,at%29.md)
  Inserts the elements of a sequence into the collection at the specified position.
### Operators
- [static func + <Other>(Self, Other) -> Self](./rangereplaceablecollection/plus%28_,_%29-2n67q.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func + <Other>(Other, Self) -> Self](./rangereplaceablecollection/plus%28_,_%29-2t6em.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](./rangereplaceablecollection/plus%28_,_%29-5rv8e.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func += <Other>(inout Self, Other)](./rangereplaceablecollection/pluseq%28_,_%29.md)
  Appends the elements of a sequence to a range-replaceable collection.
### Associated Types
- [associatedtype SubSequence](./rangereplaceablecollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Initializers
- [init<S>(S)](./rangereplaceablecollection/init%28_%29.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init(repeating: Self.Element, count: Int)](./rangereplaceablecollection/init%28repeating,count%29.md)
  Creates a new collection containing the specified number of a single, repeated value.
### Instance Methods
- [func append(Self.Element)](./rangereplaceablecollection/append%28_%29.md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](./rangereplaceablecollection/append%28contentsof%29.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func applying(CollectionDifference<Self.Element>) -> Self?](./rangereplaceablecollection/applying%28_%29.md)
  Applies the given difference to this collection.
- [func filter<E>((Self.Element) throws(E) -> Bool) throws(E) -> Self](./rangereplaceablecollection/filter%28_%29.md)
  Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [func insert(Self.Element, at: Self.Index)](./rangereplaceablecollection/insert%28_,at%29.md)
  Inserts a new element into the collection at the specified position.
- [func popLast() -> Self.Element?](./rangereplaceablecollection/poplast%28%29-253jb.md)
  Removes and returns the last element of the collection.
- [func popLast() -> Self.Element?](./rangereplaceablecollection/poplast%28%29-7kbf5.md)
  Removes and returns the last element of the collection.
- [func remove(at: Self.Index) -> Self.Element](./rangereplaceablecollection/remove%28at%29.md)
  Removes and returns the element at the specified position.
- [func remove(atOffsets: IndexSet)](./rangereplaceablecollection/remove%28atoffsets%29.md)
  Removes all the elements at the specified offsets from the collection.
- [func removeAll(keepingCapacity: Bool)](./rangereplaceablecollection/removeall%28keepingcapacity%29.md)
  Removes all elements from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](./rangereplaceablecollection/removeall%28where%29.md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](./rangereplaceablecollection/removefirst%28%29.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](./rangereplaceablecollection/removefirst%28_%29.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](./rangereplaceablecollection/removelast%28%29-1tnw.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](./rangereplaceablecollection/removelast%28%29-6e2v1.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](./rangereplaceablecollection/removelast%28_%29-66xv1.md)
  Removes the specified number of elements from the end of the collection.
- [func removeLast(Int)](./rangereplaceablecollection/removelast%28_%29-n550.md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange(Range<Self.Index>)](./rangereplaceablecollection/removesubrange%28_%29.md)
  Removes the specified subrange of elements from the collection.
- [func removeSubranges(RangeSet<Self.Index>)](./rangereplaceablecollection/removesubranges%28_%29.md)
  Removes the elements at the given indices.
- [func replace<Output, Replacement>(some RegexComponent, maxReplacements: Int, with: (Regex<Output>.Match) throws -> Replacement) rethrows](./rangereplaceablecollection/replace%28_,maxreplacements,with%29.md)
  Replaces all occurrences of the sequence matching the given regex with a given collection.
- [func replace<Replacement>(some RegexComponent, with: Replacement, maxReplacements: Int)](./rangereplaceablecollection/replace%28_,with,maxreplacements%29-20ctz.md)
  Replaces all occurrences of the sequence matching the given regex with a given collection.
- [func replace<C, Replacement>(C, with: Replacement, maxReplacements: Int)](./rangereplaceablecollection/replace%28_,with,maxreplacements%29-5u0yu.md)
  Replaces all occurrences of a target sequence with a given collection
- [func replace<Output, Replacement>(maxReplacements: Int, content: () -> some RegexComponent, with: (Regex<Output>.Match) throws -> Replacement) rethrows](./rangereplaceablecollection/replace%28maxreplacements,content,with%29.md)
  Replaces all matches for the regex in this collection, using the given closures to create the replacement and the regex.
- [func replace<Replacement>(with: Replacement, maxReplacements: Int, content: () -> some RegexComponent)](./rangereplaceablecollection/replace%28with,maxreplacements,content%29.md)
  Replaces all matches for the regex in this collection, using the given closure to create the regex.
- [func replaceSubrange<C>(Range<Self.Index>, with: C)](./rangereplaceablecollection/replacesubrange%28_,with%29.md)
  Replaces the specified subrange of elements with the given collection.
- [func replacing<Output, Replacement>(some RegexComponent, maxReplacements: Int, with: (Regex<Output>.Match) throws -> Replacement) rethrows -> Self](./rangereplaceablecollection/replacing%28_,maxreplacements,with%29.md)
  Returns a new collection in which all occurrences of a sequence matching the given regex are replaced by another collection.
- [func replacing<Output, Replacement>(some RegexComponent, subrange: Range<Self.Index>, maxReplacements: Int, with: (Regex<Output>.Match) throws -> Replacement) rethrows -> Self](./rangereplaceablecollection/replacing%28_,subrange,maxreplacements,with%29.md)
  Returns a new collection in which all occurrences of a sequence matching the given regex are replaced by another regex match.
- [func replacing<Replacement>(some RegexComponent, with: Replacement, maxReplacements: Int) -> Self](./rangereplaceablecollection/replacing%28_,with,maxreplacements%29-1tg5u.md)
  Returns a new collection in which all occurrences of a sequence matching the given regex are replaced by another collection.
- [func replacing<C, Replacement>(C, with: Replacement, maxReplacements: Int) -> Self](./rangereplaceablecollection/replacing%28_,with,maxreplacements%29-6y22p.md)
  Returns a new collection in which all occurrences of a target sequence are replaced by another collection.
- [func replacing<C, Replacement>(C, with: Replacement, subrange: Range<Self.Index>, maxReplacements: Int) -> Self](./rangereplaceablecollection/replacing%28_,with,subrange,maxreplacements%29-1uswm.md)
  Returns a new collection in which all occurrences of a target sequence are replaced by another collection.
- [func replacing<Replacement>(some RegexComponent, with: Replacement, subrange: Range<Self.Index>, maxReplacements: Int) -> Self](./rangereplaceablecollection/replacing%28_,with,subrange,maxreplacements%29-5mdsz.md)
  Returns a new collection in which all occurrences of a sequence matching the given regex are replaced by another collection.
- [func replacing<Output, Replacement>(maxReplacements: Int, content: () -> some RegexComponent, with: (Regex<Output>.Match) throws -> Replacement) rethrows -> Self](./rangereplaceablecollection/replacing%28maxreplacements,content,with%29.md)
  Returns a new collection in which all matches for the regex are replaced, using the given closures to create the replacement and the regex.
- [func replacing<Output, Replacement>(subrange: Range<Self.Index>, maxReplacements: Int, content: () -> some RegexComponent, with: (Regex<Output>.Match) throws -> Replacement) rethrows -> Self](./rangereplaceablecollection/replacing%28subrange,maxreplacements,content,with%29.md)
  Returns a new collection in which all matches for the regex are replaced, using the given closures to create the replacement and the regex.
- [func replacing<Replacement>(with: Replacement, maxReplacements: Int, content: () -> some RegexComponent) -> Self](./rangereplaceablecollection/replacing%28with,maxreplacements,content%29.md)
  Returns a new collection in which all matches for the regex are replaced, using the given closure to create the regex.
- [func replacing<Replacement>(with: Replacement, subrange: Range<Self.Index>, maxReplacements: Int, content: () -> some RegexComponent) -> Self](./rangereplaceablecollection/replacing%28with,subrange,maxreplacements,content%29.md)
  Returns a new collection in which all matches for the regex are replaced, using the given closure to create the regex.
- [func reserveCapacity(Int)](./rangereplaceablecollection/reservecapacity%28_%29.md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.
- [func trimPrefix(() -> some RegexComponent)](./rangereplaceablecollection/trimprefix%28_%29-2hzf1.md)
  Removes the initial elements matching the regex from the start of this collection, if the initial elements match, using the given closure to create the regex.
- [func trimPrefix(some RegexComponent)](./rangereplaceablecollection/trimprefix%28_%29-2s3lb.md)
  Removes the initial elements that matches the given regex.
- [func trimPrefix<Prefix>(Prefix)](./rangereplaceablecollection/trimprefix%28_%29-3t4tj.md)
  Removes `prefix` from the start of the collection.
- [func trimPrefix(while: (Self.Element) throws -> Bool) rethrows](./rangereplaceablecollection/trimprefix%28while%29.md)
### Subscripts
- [subscript(Self.Index) -> Self.Element](./rangereplaceablecollection/subscript%28_%29-1x7vz.md)
  Accesses the element at the specified position.
- [subscript(Range<Self.Index>) -> Self.SubSequence](./rangereplaceablecollection/subscript%28_%29-3h0y3.md)

## Relationships

### Inherits From
- [Collection](./collection.md)
- [Sequence](./sequence.md)
### Conforming Types
- [Array](./array.md)
- [ArraySlice](./arrayslice.md)
- [ContiguousArray](./contiguousarray.md)
- [Slice](./slice.md)
- [String](./string.md)
- [String.UnicodeScalarView](./string/unicodescalarview.md)
- [Substring](./substring.md)
- [Substring.UnicodeScalarView](./substring/unicodescalarview.md)

## See Also

### Collection Mutability
- [protocol MutableCollection](./mutablecollection.md)
  A collection that supports subscript assignment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangereplaceablecollection)*