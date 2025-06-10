# removeLast(_:)

**Framework**: MusicKit  
**Kind**: method

Removes the specified number of elements from the end of the collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
mutating func removeLast(_ k: Int)
```

#### Discussion

Attempting to remove more elements than exist in the collection triggers a runtime error.

Calling this method may invalidate all saved indices of this collection. Do not rely on a previously stored index value after altering a collection with any operation that can change its length.

> **Note**: O(), where  is the specified number of elements.

## Parameters

- `k`: The number of elements to remove from the collection.    must be greater than or equal to zero and must not exceed the   number of elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct/removelast(_:))*