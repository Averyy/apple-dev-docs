# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript

Accesses the element at the given position.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(index: Int) -> MLDataValue { get }
```

#### Return Value

The value at the given index.

## Parameters

- `index`: The index of an element in the column.

## See Also

- [subscript(MLDataColumn<Bool>) -> MLUntypedColumn](mluntypedcolumn/subscript(_:)-8ot43.md)
  Creates a subset of the column by masking its elements with a data column of Booleans.
- [subscript(MLUntypedColumn) -> MLUntypedColumn](mluntypedcolumn/subscript(_:)-9hr32.md)
  Creates a subset of the column by masking its elements with another untyped column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/subscript(_:))*