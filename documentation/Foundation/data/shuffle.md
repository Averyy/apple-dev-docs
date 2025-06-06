# shuffle()

**Framework**: Foundation  
**Kind**: method

Shuffles the collection in place.

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
mutating func shuffle()
```

#### Discussion

Use the `shuffle()` method to randomly reorder the elements of an array.

```None
var names = ["Alejandro", "Camila", "Diego", "Luciana", "Luis", "Sofía"]
names.shuffle()
// names == ["Luis", "Camila", "Luciana", "Sofía", "Alejandro", "Diego"]
```

This method is equivalent to calling `shuffle(using:)`, passing in the system’s default random generator.

> **Note**: O(), where  is the length of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/shuffle())*