# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript

Returns a `MLDataColumn` containing only the elements for which the corresponding mask has a nonzero or non-default value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(mask: MLUntypedColumn) -> MLDataColumn<Element> { get }
```

#### Return Value

A MLUntypedColumn containing the subsequence of this MLUntypedColumn’s elements indicated by the mask MLUntypedColumn.

## Parameters

- `mask`: A MLUntypedColumn with the same element count as this MLUntypedColumn.

## See Also

- [subscript(MLDataColumn<Bool>) -> MLDataColumn<Element>](mldatacolumn/subscript(_:)-78irf.md)
  Creates a subset of the column by masking its elements with a column of Booleans.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/subscript(_:)-1n3x)*