# popLast()

**Framework**: Swift  
**Kind**: method

Removes and returns the last element of the collection.

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
mutating func popLast() -> Self.Element?
```

#### Return Value

The last element of the collection if the collection is not empty; otherwise, `nil`.

#### Discussion

Calling this method may invalidate all saved indices of this collection. Do not rely on a previously stored index value after altering a collection with any operation that can change its length.

> **Note**: O(1)

O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangereplaceablecollection/poplast()-253jb)*