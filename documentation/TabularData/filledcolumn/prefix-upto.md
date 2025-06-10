# prefix(upTo:)

**Framework**: TabularData  
**Kind**: method

Returns a subsequence from the start of the collection up to, but not including, the specified position.

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
func prefix(upTo end: Self.Index) -> Self.SubSequence
```

#### Return Value

A subsequence up to, but not including, the `end` position.

#### Discussion

The resulting subsequence  the element at the position `end`. The following example searches for the index of the number `40` in an array of integers, and then prints the prefix of the array up to, but not including, that index:

```None
let numbers = [10, 20, 30, 40, 50, 60]
if let i = numbers.firstIndex(of: 40) {
    print(numbers.prefix(upTo: i))
}
// Prints "[10, 20, 30]"
```

Passing the collection’s starting index as the `end` parameter results in an empty subsequence.

```None
print(numbers.prefix(upTo: numbers.startIndex))
// Prints "[]"
```

Using the `prefix(upTo:)` method is equivalent to using a partial half-open range as the collection’s subscript. The subscript notation is preferred over `prefix(upTo:)`.

```None
if let i = numbers.firstIndex(of: 40) {
    print(numbers[..<i])
}
// Prints "[10, 20, 30]"
```

> **Note**: O(1)

## Parameters

- `end`: The “past the end” index of the resulting subsequence.    must be a valid index of the collection.

## See Also

- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](filledcolumn/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](filledcolumn/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func prefix(Int) -> Self.SubSequence](filledcolumn/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
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

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/prefix(upto:))*