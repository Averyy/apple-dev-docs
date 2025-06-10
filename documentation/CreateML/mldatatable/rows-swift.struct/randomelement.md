# randomElement()

**Framework**: Create ML  
**Kind**: method

Returns a random element of the collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

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

## See Also

- [subscript(Int) -> MLDataTable.Rows.Element](mldatatable/rows-swift.struct/subscript(_:).md)
  Subscript by index. This returns a row in the data table.
- [var first: Self.Element?](mldatatable/rows-swift.struct/first.md)
  The first element of the collection.
- [var last: Self.Element?](mldatatable/rows-swift.struct/last.md)
  The last element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](mldatatable/rows-swift.struct/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct/randomelement())*