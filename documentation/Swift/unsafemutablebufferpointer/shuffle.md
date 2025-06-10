# shuffle()

**Framework**: Swift  
**Kind**: method

Shuffles the collection in place.

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
mutating func shuffle()
```

#### Discussion

Use the `shuffle()` method to randomly reorder the elements of an array.

```swift
var names = ["Alejandro", "Camila", "Diego", "Luciana", "Luis", "Sofía"]
names.shuffle()
// names == ["Luis", "Camila", "Luciana", "Sofía", "Alejandro", "Diego"]
```

This method is equivalent to calling `shuffle(using:)`, passing in the system’s default random generator.

> **Note**: O(), where  is the length of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/shuffle())*