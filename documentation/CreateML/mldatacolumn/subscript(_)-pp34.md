# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript

Creates a subset of the column, given a range of elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(slice: Range<Int>) -> MLDataColumn<Element> { get }
```

#### Return Value

A new column.

## Parameters

- `slice`: A range of integers indicating which elements to include in the new column.

## See Also

- [subscript<R>(R) -> MLDataColumn<Element>](mldatacolumn/subscript(_:)-5mczv.md)
  Creates a subset of the column, given a range expression of elements.
- [func prefix(Int) -> MLDataColumn<Element>](mldatacolumn/prefix(_:).md)
  Creates a subset of the column, given a number of initial elements.
- [func suffix(Int) -> MLDataColumn<Element>](mldatacolumn/suffix(_:).md)
  Creates a subset of the column, given a number of final elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/subscript(_:)-pp34)*