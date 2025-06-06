# +(_:_:)

**Framework**: Create ML  
**Kind**: op

Creates a column of integers by adding each element of the given column to the given integer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func + (a: MLDataColumn<Int>, b: Int) -> MLDataColumn<Int>
```

#### Return Value

A new column of integers.

## Parameters

- `a`: A column of integers.
- `b`: An integer.

## See Also

- [static func + (MLDataColumn<Double>, Double) -> MLDataColumn<Double>](mldatacolumn/+(_:_:)-4se2l.md)
  Creates a column of doubles by adding each element of the given column to the given double.
- [static func - (MLDataColumn<Int>, Int) -> MLDataColumn<Int>](mldatacolumn/-(_:_:)-2sddu.md)
  Creates a column of integers by subtracting the given integer from each element of the given column.
- [static func - (MLDataColumn<Double>, Double) -> MLDataColumn<Double>](mldatacolumn/-(_:_:)-9smok.md)
  Creates a column of doubles by subtracting the given double from each element of the given column.
- [static func * (MLDataColumn<Int>, Int) -> MLDataColumn<Int>](mldatacolumn/*(_:_:)-2zih0.md)
  Creates a column of integers by multiplying each element of the given column by the given integer.
- [static func * (MLDataColumn<Double>, Double) -> MLDataColumn<Double>](mldatacolumn/*(_:_:)-4ilhj.md)
  Creates a column of doubles by multiplying each element of the given column by the given double.
- [static func / (MLDataColumn<Int>, Int) -> MLDataColumn<Int>](mldatacolumn/_(_:_:)-3ea6t.md)
  Creates a column of integers by dividing each element of the given column by the given integer.
- [static func / (MLDataColumn<Double>, Double) -> MLDataColumn<Double>](mldatacolumn/_(_:_:)-8k8ao.md)
  Creates a column of doubles by dividing each element of the given column by the given double.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/+(_:_:)-7tghu)*