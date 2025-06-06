# randomElement()

**Framework**: Swift  
**Kind**: method

Returns a random element of the collection.

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
func randomElement() -> Self.Element?
```

#### Return Value

A random element from the collection. If the collection is empty, the method returns `nil`.

#### Discussion

Call `randomElement()` to select a random element from an array or another collection. This example picks a name at random from an array:

```swift
let names = ["Zoey", "Chloe", "Amani", "Amaia"]
let randomName = names.randomElement()!
// randomName == "Amani"
```

This method is equivalent to calling `randomElement(using:)`, passing in the system’s default random generator.

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

## See Also

- [subscript(Int) -> Element](array/subscript(_:)-25iat.md)
  Accesses the element at the specified position.
- [var first: Self.Element?](array/first.md)
  The first element of the collection.
- [var last: Self.Element?](array/last.md)
  The last element of the collection.
- [subscript(Range<Int>) -> ArraySlice<Element>](array/subscript(_:)-53fvb.md)
  Accesses a contiguous subrange of the array’s elements.
- [subscript<R>(R) -> Self.SubSequence](array/subscript(_:)-3kwny.md)
- [subscript<R>(R) -> Self.SubSequence](array/subscript(_:)-4h7rl.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](array/subscript(_:)-3pmfg.md)
- [func randomElement<T>(using: inout T) -> Self.Element?](array/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/randomelement())*