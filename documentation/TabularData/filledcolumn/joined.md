# joined()

**Framework**: TabularData  
**Kind**: method

Returns the elements of this sequence of sequences, concatenated.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func joined() -> FlattenSequence<Self>
```

#### Return Value

A flattened view of the elements of this sequence of sequences.

#### Discussion

In this example, an array of three ranges is flattened so that the elements of each range can be iterated in turn.

```None
let ranges = [0..<3, 8..<10, 15..<17]

// A for-in loop over 'ranges' accesses each range:
for range in ranges {
  print(range)
}
// Prints "0..<3"
// Prints "8..<10"
// Prints "15..<17"

// Use 'joined()' to access each element of each range:
for index in ranges.joined() {
    print(index, terminator: " ")
}
// Prints: "0 1 2 8 9 15 16"
```

## See Also

- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](filledcolumn/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](filledcolumn/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func prefix(Int) -> Self.SubSequence](filledcolumn/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](filledcolumn/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(through: Self.Index) -> Self.SubSequence](filledcolumn/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](filledcolumn/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(Int) -> Self.SubSequence](filledcolumn/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](filledcolumn/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](filledcolumn/joined(separator:)-1fxji.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [func joined(separator: String) -> String](filledcolumn/joined(separator:)-8wfe6.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func joined(separator: String) -> String](filledcolumn/joined(separator:)-9l6bv.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/joined())*