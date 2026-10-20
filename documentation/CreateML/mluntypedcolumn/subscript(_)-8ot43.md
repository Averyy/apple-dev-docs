# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript  
**Role**: Instance Subscript

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

**Other overloads**:

```swift
subscript(index: Int) -> MLDataValue { get }
```

```swift
subscript(mask: MLUntypedColumn) -> MLUntypedColumn { get }
```

```swift
subscript(slice: Range<Int>) -> MLUntypedColumn { get }
```

```swift
subscript<R>(slice: R) -> MLUntypedColumn where R : RangeExpression, R.Bound == Int { get }
```

#### Return Value

A new column.

## Parameters

- `mask`: A Boolean column indicating whether elements should be kept (`true`) or removed (`false`) in the derived column.

## See Also

### Masking elements to generate an untyped column
- [subscript(_:)](./subscript%28_%29.md)
  Accesses the element at the given position.
- [subscript(MLUntypedColumn) -> MLUntypedColumn](./subscript%28_%29-9hr32.md)
  Creates a subset of the column by masking its elements with another untyped column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/subscript(_:)-8ot43)*