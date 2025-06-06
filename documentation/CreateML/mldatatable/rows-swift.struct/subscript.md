# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript

Subscript by index. This returns a row in the data table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(index: Int) -> MLDataTable.Rows.Element { get }
```

## See Also

- [var first: Self.Element?](mldatatable/rows-swift.struct/first.md)
  The first element of the collection.
- [var last: Self.Element?](mldatatable/rows-swift.struct/last.md)
  The last element of the collection.
- [func randomElement() -> Self.Element?](mldatatable/rows-swift.struct/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](mldatatable/rows-swift.struct/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct/subscript(_:))*