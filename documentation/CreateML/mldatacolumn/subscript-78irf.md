# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript

Creates a subset of the column by masking its elements with a column of Booleans.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(mask: MLDataColumn<Bool>) -> MLDataColumn<Element> { get }
```

#### Return Value

A new column.

## Parameters

- `mask`: A Boolean column indicating whether elements should be kept ( ) or removed ( ) in the   derived column.

## See Also

- [subscript(MLUntypedColumn) -> MLDataColumn<Element>](mldatacolumn/subscript(_:)-1n3x.md)
  Returns a `MLDataColumn` containing only the elements for which the corresponding mask has a nonzero or non-default value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/subscript(_:)-78irf)*