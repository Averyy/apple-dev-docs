# popLast()

**Framework**: System  
**Kind**: method

Removes and returns the last element of the collection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/poplast())*