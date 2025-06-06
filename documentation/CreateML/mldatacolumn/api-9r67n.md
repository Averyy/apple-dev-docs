# +(_:_:)

**Framework**: Create ML  
**Kind**: op

Creates a column of doubles by adding the given double to each element of the given column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func + (a: Double, b: MLDataColumn<Double>) -> MLDataColumn<Double>
```

#### Return Value

A new column of doubles.

## Parameters

- `a`: A double.
- `b`: A column of doubles.

## See Also

- [static func + (Int, MLDataColumn<Int>) -> MLDataColumn<Int>](mldatacolumn/+(_:_:)-2zcp.md)
  Creates a column of integers by adding the given integer to each element of the given column.
- [static func - (Int, MLDataColumn<Int>) -> MLDataColumn<Int>](mldatacolumn/-(_:_:)-507l8.md)
  Creates a column of integers by subtracting each element of the given column from the given integer.
- [static func - (Double, MLDataColumn<Double>) -> MLDataColumn<Double>](mldatacolumn/-(_:_:)-2e7k4.md)
  Creates a column of doubles by subtracting each element of the given column from the given double.
- [static func * (Int, MLDataColumn<Int>) -> MLDataColumn<Int>](mldatacolumn/*(_:_:)-48xte.md)
  Creates a column of integers by multiplying the given integer by each element of the given column.
- [static func * (Double, MLDataColumn<Double>) -> MLDataColumn<Double>](mldatacolumn/*(_:_:)-9sysp.md)
  Creates a column of doubles by multiplying the given double by each element of the given column.
- [static func / (Int, MLDataColumn<Int>) -> MLDataColumn<Int>](mldatacolumn/_(_:_:)-9ew9w.md)
  Creates a column of integers by dividing the given integer by each element of the given column.
- [static func / (Double, MLDataColumn<Double>) -> MLDataColumn<Double>](mldatacolumn/_(_:_:)-121w8.md)
  Creates a column of doubles by dividing the given double by each element of the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/+(_:_:)-9r67n)*