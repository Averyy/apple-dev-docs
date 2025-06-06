# randomElement()

**Framework**: Create ML Components  
**Kind**: method

Returns a random element of the collection.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func randomElement() -> Self.Element?
```

#### Return Value

A random element from the collection. If the collection is empty, the method returns `nil`.

#### Discussion

Call `randomElement()` to select a random element from an array or another collection. This example picks a name at random from an array:

```None
let names = ["Zoey", "Chloe", "Amani", "Amaia"]
let randomName = names.randomElement()!
// randomName == "Amani"
```

This method is equivalent to calling `randomElement(using:)`, passing in the system’s default random generator.

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/slidingwindows/randomelement())*