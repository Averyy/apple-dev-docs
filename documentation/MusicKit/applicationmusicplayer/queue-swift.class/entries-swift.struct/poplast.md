# popLast()

**Framework**: MusicKit  
**Kind**: method

Removes and returns the last element of the collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
mutating func popLast() -> Self.Element?
```

#### Return Value

The last element of the collection if the collection is not empty; otherwise, `nil`.

#### Discussion

Calling this method may invalidate all saved indices of this collection. Do not rely on a previously stored index value after altering a collection with any operation that can change its length.

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct/poplast())*