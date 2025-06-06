# enumerated()

**Framework**: Realitykit  
**Kind**: method

Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func enumerated() -> EnumeratedSequence<Self>
```

#### Return Value

A sequence of pairs enumerating the sequence.

#### Discussion

This example enumerates the characters of the string “Swift” and prints each character along with its place in the string.

```None
for (n, c) in "Swift".enumerated() {
    print("\(n): '\(c)'")
}
// Prints "0: 'S'"
// Prints "1: 'w'"
// Prints "2: 'i'"
// Prints "3: 'f'"
// Prints "4: 't'"
```

When you enumerate a collection, the integer part of each pair is a counter for the enumeration, but is not necessarily the index of the paired value. These counters can be used as indices only in instances of zero-based, integer-indexed collections, such as `Array` and `ContiguousArray`. For other collections the counters may be out of range or of the wrong type to use as an index. To iterate over the elements of a collection with its indices, use the `zip(_:_:)` function.

This example iterates over the indices and elements of a set, building a list consisting of indices of names with five or fewer letters.

```None
let names: Set = ["Sofia", "Camilla", "Martina", "Mateo", "Nicolás"]
var shorterIndices: [Set<String>.Index] = []
for (i, name) in zip(names.indices, names) {
    if name.count <= 5 {
        shorterIndices.append(i)
    }
}
```

Now that the `shorterIndices` array holds the indices of the shorter names in the `names` set, you can use those indices to access elements in the set.

```None
for i in shorterIndices {
    print(names[i])
}
// Prints "Sofia"
// Prints "Mateo"
```

> **Note**: O(1)

## See Also

- [subscript(JointTransforms.Index) -> Transform](jointtransforms/subscript(_:).md)
  Accesses a single joint transform in the collection at the given index.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](jointtransforms/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](jointtransforms/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func contains(Self.Element) -> Bool](jointtransforms/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](jointtransforms/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](jointtransforms/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](jointtransforms/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: Self.Index, to: Self.Index) -> Int](jointtransforms/distance(from:to:).md)
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](jointtransforms/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](jointtransforms/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](jointtransforms/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](jointtransforms/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](jointtransforms/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](jointtransforms/filter(_:).md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](jointtransforms/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/jointtransforms/enumerated())*