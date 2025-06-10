# dropFirst(_:)

**Framework**: TabularData  
**Kind**: method

Returns a subsequence containing all but the given number of initial elements.

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
func dropFirst(_ k: Int = 1) -> Self.SubSequence
```

#### Return Value

A subsequence starting after the specified number of elements.

#### Discussion

If the number of elements to drop exceeds the number of elements in the collection, the result is an empty subsequence.

```None
let numbers = [1, 2, 3, 4, 5]
print(numbers.dropFirst(2))
// Prints "[3, 4, 5]"
print(numbers.dropFirst(10))
// Prints "[]"
```

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the number of elements to drop from the beginning of the collection.

## Parameters

- `k`: The number of elements to drop from the beginning of   the collection.   must be greater than or equal to zero.

## See Also

- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](filledcolumn/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
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
- [func joined() -> FlattenSequence<Self>](filledcolumn/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](filledcolumn/joined(separator:)-1fxji.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [func joined(separator: String) -> String](filledcolumn/joined(separator:)-8wfe6.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func joined(separator: String) -> String](filledcolumn/joined(separator:)-9l6bv.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/dropfirst(_:))*