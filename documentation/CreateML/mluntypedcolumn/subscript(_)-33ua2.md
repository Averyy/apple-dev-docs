# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript  
**Role**: Instance Subscript

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
subscript(slice: Range<Int>) -> MLUntypedColumn { get }
```

**Other overloads**:

```swift
subscript(index: Int) -> MLDataValue { get }
```

```swift
subscript(mask: MLDataColumn<Bool>) -> MLUntypedColumn { get }
```

```swift
subscript(mask: MLUntypedColumn) -> MLUntypedColumn { get }
```

```swift
subscript<R>(slice: R) -> MLUntypedColumn where R : RangeExpression, R.Bound == Int { get }
```

#### Return Value

A new column.

## Parameters

- `slice`: A range of integers indicating which elements to include in the new column.

## See Also

### Selecting elements to generate an untyped column
- [subscript<R>(R) -> MLUntypedColumn](./subscript%28_%29-9dpy7.md)
  Creates a subset of the column, given a range expression of elements.
- [func prefix(Int) -> MLUntypedColumn](./prefix%28_%29.md)
  Creates a subset of the column, given a number of initial elements.
- [func suffix(Int) -> MLUntypedColumn](./suffix%28_%29.md)
  Creates a subset of the column, given a number of final elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/subscript(_:)-33ua2)*