# <=(_:_:)

**Framework**: Create ML  
**Kind**: op

Creates a column of Booleans by testing whether the given value is less than or equal to each element in the given column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func <= (a: Element, b: MLDataColumn<Element>) -> MLDataColumn<Bool>
```

#### Return Value

A new column of Booleans.

## Parameters

- `a`: A value of the same type as the elements of the column.
- `b`: A column.

## See Also

- [static func == (Element, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/==(_:_:)-6zz2o.md)
  Creates a column of Booleans by testing whether the given value is equal to each element in the given column.
- [static func != (Element, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/!=(_:_:)-4477j.md)
  Creates a column of Booleans by testing whether the given value is not equal to each element in the given column.
- [static func < (Element, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/_(_:_:)-33lwa.md)
  Creates a column of Booleans by testing whether the given value is less than each element in the given column.
- [static func > (Element, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/_(_:_:)-6irjn.md)
  Creates a column of Booleans by testing whether the given value is greater than each element in the given column.
- [static func >= (Element, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/_=(_:_:)-8e3ur.md)
  Creates a column of Booleans by testing whether the given value is greater than or equal to each element in the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/_=(_:_:)-3fx6w)*