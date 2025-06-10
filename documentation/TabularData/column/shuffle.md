# shuffle()

**Framework**: TabularData  
**Kind**: method

Shuffles the collection in place.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

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

## See Also

- [func shuffle<T>(using: inout T)](column/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/shuffle())*