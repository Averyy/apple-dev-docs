# dropFirst(_:)

**Framework**: Foundation  
**Kind**: method

Returns a subsequence containing all but the given number of initial elements.

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

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the number of elements to drop from the beginning of the collection.

## Parameters

- `k`: The number of elements to drop from the beginning of   the collection.   must be greater than or equal to zero.

## See Also

- [func dropLast(Int) -> Self.SubSequence](data/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](data/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func advanced(by: Int) -> Data](data/advanced(by:).md)
  Returns a new data buffer created by removing the given number of bytes from the front of the original buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/dropfirst(_:))*