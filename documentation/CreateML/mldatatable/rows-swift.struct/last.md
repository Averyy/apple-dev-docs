# last

**Framework**: Create ML  
**Kind**: property

The last element of the collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var last: Self.Element? { get }
```

#### Discussion

If the collection is empty, the value of this property is `nil`.

```None
let numbers = [10, 20, 30, 40, 50]
if let lastNumber = numbers.last {
    print(lastNumber)
}
// Prints "50"
```

> **Note**: O(1)

O(1)

## See Also

- [subscript(Int) -> MLDataTable.Rows.Element](mldatatable/rows-swift.struct/subscript(_:).md)
  Subscript by index. This returns a row in the data table.
- [var first: Self.Element?](mldatatable/rows-swift.struct/first.md)
  The first element of the collection.
- [func randomElement() -> Self.Element?](mldatatable/rows-swift.struct/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](mldatatable/rows-swift.struct/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct/last)*