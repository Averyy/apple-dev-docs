# dropFirst(_:)

**Framework**: RealityKit  
**Kind**: method

Returns a subsequence containing all but the given number of initial elements.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewentitycollection/dropfirst(_:))*