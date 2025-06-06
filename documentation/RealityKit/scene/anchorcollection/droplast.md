# dropLast(_:)

**Framework**: Realitykit  
**Kind**: method

Returns a subsequence containing all but the specified number of final elements.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func dropLast(_ k: Int = 1) -> Self.SubSequence
```

#### Return Value

A subsequence that leaves off the specified number of elements at the end.

#### Discussion

If the number of elements to drop exceeds the number of elements in the collection, the result is an empty subsequence.

```None
let numbers = [1, 2, 3, 4, 5]
print(numbers.dropLast(2))
// Prints "[1, 2, 3]"
print(numbers.dropLast(10))
// Prints "[]"
```

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

## Parameters

- `k`: The number of elements to drop off the end of the   collection.   must be greater than or equal to zero.

## See Also

- [func dropFirst(Int) -> Self.SubSequence](scene/anchorcollection/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](scene/anchorcollection/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/droplast(_:))*