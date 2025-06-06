# removeAll(where:)

**Framework**: MusicKit  
**Kind**: method

Removes all the elements that satisfy the given predicate.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
mutating func removeAll(where shouldBeRemoved: (Self.Element) throws -> Bool) rethrows
```

#### Discussion

Use this method to remove every element in a collection that meets particular criteria. The order of the remaining elements is preserved. This example removes all the odd values from an array of numbers:

```swift
var numbers = [5, 6, 7, 8, 9, 10, 11]
numbers.removeAll(where: { $0 % 2 != 0 })
// numbers == [6, 8, 10]
```

> **Note**: O(), where  is the length of the collection.

O(), where  is the length of the collection.

## Parameters

- `shouldBeRemoved`: A closure that takes an element of the   sequence as its argument and returns a Boolean value indicating   whether the element should be removed from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct/removeall(where:)-2qnp6)*