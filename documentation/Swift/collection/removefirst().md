# removeFirst()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Removes and returns the first element of the collection.

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
@discardableResult
mutating func removeFirst() -> Self.Element
```

Available when `Self` is `Self.SubSequence`.

## Return Value

The first element of the collection.

## Discussion

The collection must not be empty.

> **Complexity**: O(1)

## See Also

### Selecting and Excluding Elements
- [func popFirst() -> Self.Element?](./popfirst%28%29.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](./removefirst%28_%29.md)
  Removes the specified number of elements from the beginning of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collection/removefirst())*