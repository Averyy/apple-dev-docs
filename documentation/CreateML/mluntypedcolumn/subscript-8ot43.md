# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript

Creates a subset of the column by masking its elements with a data column of Booleans.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(mask: MLDataColumn<Bool>) -> MLUntypedColumn { get }
```

#### Return Value

A new column.

## Parameters

- `mask`: A Boolean column indicating whether elements should be kept   ( ) or removed ( ) in the derived column.

## See Also

- [subscript(MLUntypedColumn) -> MLUntypedColumn](mluntypedcolumn/subscript(_:)-9hr32.md)
  Creates a subset of the column by masking its elements with another untyped column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/subscript(_:)-8ot43)*