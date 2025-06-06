# append(_:)

**Framework**: MusicKit  
**Kind**: method

Adds an element to the end of the collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
mutating func append(_ newElement: Self.Element)
```

#### Discussion

If the collection does not have sufficient capacity for another element, additional storage is allocated before appending `newElement`. The following example adds a new number to an array of integers:

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.append(100)

print(numbers)
// Prints "[1, 2, 3, 4, 5, 100]"
```

> **Note**: O(1) on average, over many calls to `append(_:)` on the same collection.

O(1) on average, over many calls to `append(_:)` on the same collection.

## Parameters

- `newElement`: The element to append to the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct/append(_:))*