# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript

Creates a subset of the column, given a range expression of elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript<R>(slice: R) -> MLUntypedColumn where R : RangeExpression, R.Bound == Int { get }
```

#### Return Value

A new column.

## Parameters

- `slice`: An interger range expression indicating which elements to include in the new column.

## See Also

- [subscript(Range<Int>) -> MLUntypedColumn](mluntypedcolumn/subscript(_:)-33ua2.md)
  Creates a subset of the column, given a range of elements.
- [func prefix(Int) -> MLUntypedColumn](mluntypedcolumn/prefix(_:).md)
  Creates a subset of the column, given a number of initial elements.
- [func suffix(Int) -> MLUntypedColumn](mluntypedcolumn/suffix(_:).md)
  Creates a subset of the column, given a number of final elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/subscript(_:)-9dpy7)*