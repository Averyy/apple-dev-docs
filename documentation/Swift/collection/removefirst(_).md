# removeFirst(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Removes the specified number of elements from the beginning of the collection.

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
mutating func removeFirst(_ k: Int)
```

Available when `Self` is `Self.SubSequence`.

#### Discussion

> **Complexity**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(*k*), where *k* is the specified number of elements.

## Parameters

- `k`: The number of elements to remove. `k` must be greater than or equal to zero, and must be less than or equal to the number of elements in the collection.

## See Also

### Selecting and Excluding Elements
- [func popFirst() -> Self.Element?](./popfirst%28%29.md)
  Removes and returns the first element of the collection.
- [func removeFirst() -> Self.Element](./removefirst%28%29.md)
  Removes and returns the first element of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collection/removefirst(_:))*