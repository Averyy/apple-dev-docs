# enumerated()

**Framework**: Create ML  
**Kind**: method

Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

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

- [func forEach((Self.Element) throws -> Void) rethrows](mldatatable/rows-swift.struct/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func makeIterator() -> IndexingIterator<Self>](mldatatable/rows-swift.struct/makeiterator.md)
  Returns an iterator over the elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct/enumerated())*