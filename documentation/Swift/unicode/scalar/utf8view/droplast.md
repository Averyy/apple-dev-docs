# dropLast(_:)

**Framework**: Swift  
**Kind**: method

Returns a subsequence containing all but the specified number of final elements.

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
func dropLast(_ k: Int) -> Self.SubSequence
```

#### Return Value

A subsequence that leaves off `k` elements from the end.

#### Discussion

If the number of elements to drop exceeds the number of elements in the collection, the result is an empty subsequence.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.dropLast(2))
// Prints "[1, 2, 3]"
print(numbers.dropLast(10))
// Prints "[]"
```

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the number of elements to drop.

## Parameters

- `k`: The number of elements to drop off the end of the   collection.   must be greater than or equal to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/utf8view/droplast(_:))*