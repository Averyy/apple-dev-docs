# reverse()

**Framework**: Foundation  
**Kind**: method

Reverses the elements of the collection in place.

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
mutating func reverse()
```

#### Discussion

The following example reverses the elements of an array of characters:

```None
var characters: [Character] = ["C", "a", "f", "é"]
characters.reverse()
print(characters)
// Prints "["é", "f", "a", "C"]"
```

> **Note**: O(), where  is the number of elements in the collection.

O(), where  is the number of elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/reverse())*