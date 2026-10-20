# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript  
**Role**: Instance Subscript

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

Available when `Element` conforms to `MLDataValueConvertible`.

**Other overloads**:

```swift
subscript(index: Int) -> Element { get }
```

```swift
subscript(mask: MLUntypedColumn) -> MLDataColumn<Element> { get }
```

```swift
subscript(slice: Range<Int>) -> MLDataColumn<Element> { get }
```

```swift
subscript<R>(slice: R) -> MLDataColumn<Element> where R : RangeExpression, R.Bound == Int { get }
```

#### Return Value

A new column.

## Parameters

- `mask`: A Boolean column indicating whether elements should be kept (`true`) or removed (`false`) in the derived column.

## See Also

### Masking elements to generate a column
- [subscript(MLUntypedColumn) -> MLDataColumn<Element>](./subscript%28_%29-1n3x.md)
  Returns a `MLDataColumn` containing only the elements for which the corresponding mask has a nonzero or non-default value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/subscript(_:)-78irf)*