# dropFirst(_:)

**Framework**: Swift  
**Kind**: method

Returns a sequence containing all but the given number of initial elements.

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
func dropFirst(_ k: Int = 1) -> DropFirstSequence<Self>
```

#### Return Value

A sequence starting after the specified number of elements.

#### Discussion

If the number of elements to drop exceeds the number of elements in the sequence, the result is an empty sequence.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.dropFirst(2))
// Prints "[3, 4, 5]"
print(numbers.dropFirst(10))
// Prints "[]"
```

> **Note**: O(1), with O() deferred to each iteration of the result, where  is the number of elements to drop from the beginning of the sequence.

## Parameters

- `k`: The number of elements to drop from the beginning of   the sequence.   must be greater than or equal to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/indexingiterator/dropfirst(_:))*