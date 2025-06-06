# randomElement()

**Framework**: TabularData  
**Kind**: method

Returns a random element of the collection.

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

## See Also

- [var first: Self.Element?](rowgrouping/first.md)
  The first element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](rowgrouping/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/randomelement())*