# <(_:_:)

**Framework**: Create ML  
**Kind**: op

Creates a column of Booleans by testing whether each element in the given column is less than the given value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func < (a: MLDataColumn<Element>, b: Element) -> MLDataColumn<Bool>
```

#### Return Value

A new column of Booleans.

## Parameters

- `a`: A column.
- `b`: A value of the same type as the elements of the column.

## See Also

- [static func == (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](mldatacolumn/==(_:_:)-7clbs.md)
  Creates a column of Booleans by testing whether each element in the given column is equal to the given value.
- [static func != (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](mldatacolumn/!=(_:_:)-4jp0y.md)
  Creates a column of Booleans by testing whether each element in the given column is not equal to the given value.
- [static func <= (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](mldatacolumn/_=(_:_:)-86x3a.md)
  Creates a column of Booleans by testing whether each element in the given column is less than or equal to the given value.
- [static func > (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](mldatacolumn/_(_:_:)-ebgq.md)
  Creates a column of Booleans by testing whether each element in the given column is greater than the given value.
- [static func >= (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](mldatacolumn/_=(_:_:)-1ctuz.md)
  Creates a column of Booleans by testing whether each element in the given column is greater than or equal to the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/_(_:_:)-4ujss)*