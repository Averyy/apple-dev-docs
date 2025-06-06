# reverse()

**Framework**: MusicKit  
**Kind**: method

Reverses the elements of the collection in place.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
mutating func reverse()
```

#### Discussion

The following example reverses the elements of an array of characters:

```swift
var characters: [Character] = ["C", "a", "f", "é"]
characters.reverse()
print(characters)
// Prints "["é", "f", "a", "C"]"
```

> **Note**: O(), where  is the number of elements in the collection.

O(), where  is the number of elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct/reverse())*