# popLast()

**Framework**: Foundation  
**Kind**: method

Removes and returns the last element of the collection.

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
mutating func popLast() -> Self.Element?
```

#### Return Value

The last element of the collection if the collection has one or more elements; otherwise, `nil`.

#### Discussion

You can use `popLast()` to remove the last element of a collection that might be empty. The `removeLast()` method must be used only on a nonempty collection.

> **Note**: O(1)

O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/poplast()-149cz)*