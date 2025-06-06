# popFirst()

**Framework**: Swift  
**Kind**: method

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
mutating func popFirst() -> Self.Element?
```

#### Return Value

The first element of the collection if the collection is not empty; otherwise, `nil`.

#### Discussion

> **Note**: O(1)

## See Also

- [func removeFirst() -> Self.Element](collection/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](collection/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collection/popfirst())*