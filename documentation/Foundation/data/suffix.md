# suffix(_:)

**Framework**: Foundation  
**Kind**: method

Returns a subsequence, up to the given maximum length, containing the final elements of the collection.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func suffix(_ maxLength: Int) -> Self.SubSequence
```

#### Return Value

A subsequence terminating at the end of the collection with at most `maxLength` elements.

#### Discussion

If the maximum length exceeds the number of elements in the collection, the result contains the entire collection.

```None
let numbers = [1, 2, 3, 4, 5]
print(numbers.suffix(2))
// Prints "[4, 5]"
print(numbers.suffix(10))
// Prints "[1, 2, 3, 4, 5]"
```

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is equal to `maxLength`.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is equal to `maxLength`.

## Parameters

- `maxLength`: The maximum number of elements to return.    must be greater than or equal to zero.

## See Also

- [func filter((Self.Element) throws -> Bool) rethrows -> Self](data/filter(_:).md)
  Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [func prefix(Int) -> Self.SubSequence](data/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](data/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](data/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](data/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(from: Self.Index) -> Self.SubSequence](data/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/suffix(_:))*