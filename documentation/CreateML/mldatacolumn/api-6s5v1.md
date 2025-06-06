# <=(_:_:)

**Framework**: Create ML  
**Kind**: op

Creates a column of Booleans by testing whether each element in the first column is less than or equal to the corresponding element in the second column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func <= (a: MLDataColumn<Element>, b: MLDataColumn<Element>) -> MLDataColumn<Bool>
```

#### Return Value

A new column of Booleans if the columns are the same size; otherwise an invalid column.

## Parameters

- `a`: A column.
- `b`: A column.

## See Also

- [static func == (MLDataColumn<Element>, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/==(_:_:)-9e3tx.md)
  Creates a column of Booleans by testing whether each element in the first column is equal to the corresponding element in the second column.
- [static func != (MLDataColumn<Element>, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/!=(_:_:)-1vu4e.md)
  Creates a column of Booleans by testing whether each element in the first column is not equal to the corresponding element in the second column.
- [static func < (MLDataColumn<Element>, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/_(_:_:)-3om6w.md)
  Creates a column of Booleans by testing whether each element in the first column is less than the corresponding element in the second column.
- [static func > (MLDataColumn<Element>, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/_(_:_:)-2dym4.md)
  Creates a column of Booleans by testing whether each element in the first column is greater than the corresponding element in the second column.
- [static func >= (MLDataColumn<Element>, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/_=(_:_:)-4w60p.md)
  Creates a column of Booleans by testing whether each element in the first column is greater than or equal to the corresponding element in the second column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/_=(_:_:)-6s5v1)*