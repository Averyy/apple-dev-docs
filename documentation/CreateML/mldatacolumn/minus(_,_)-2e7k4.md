# -(_:_:)

**Framework**: Create ML  
**Kind**: op  
**Role**: Operator

Creates a column of doubles by subtracting each element of the given column from the given double.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func - (a: Double, b: MLDataColumn<Double>) -> MLDataColumn<Double>
```

Available when `Element` is `Double`.

**Other overloads**:

```swift
static func - (a: Int, b: MLDataColumn<Int>) -> MLDataColumn<Int>
```

```swift
static func - (a: MLDataColumn<Double>, b: Double) -> MLDataColumn<Double>
```

```swift
static func - (a: MLDataColumn<Double>, b: MLDataColumn<Double>) -> MLDataColumn<Double>
```

```swift
static func - (a: MLDataColumn<Int>, b: Int) -> MLDataColumn<Int>
```

```swift
static func - (a: MLDataColumn<Int>, b: MLDataColumn<Int>) -> MLDataColumn<Int>
```

#### Return Value

A new column of doubles.

## Parameters

- `a`: A double.
- `b`: A column of doubles.

## See Also

### Combining a value with a column to generate a column
- [static func + (Int, MLDataColumn<Int>) -> MLDataColumn<Int>](./plus%28_,_%29-2zcp.md)
  Creates a column of integers by adding the given integer to each element of the given column.
- [static func + (Double, MLDataColumn<Double>) -> MLDataColumn<Double>](./plus%28_,_%29-9r67n.md)
  Creates a column of doubles by adding the given double to each element of the given column.
- [static func - (Int, MLDataColumn<Int>) -> MLDataColumn<Int>](./minus%28_,_%29-507l8.md)
  Creates a column of integers by subtracting each element of the given column from the given integer.
- [static func * (Int, MLDataColumn<Int>) -> MLDataColumn<Int>](./star%28_,_%29-48xte.md)
  Creates a column of integers by multiplying the given integer by each element of the given column.
- [static func * (Double, MLDataColumn<Double>) -> MLDataColumn<Double>](./star%28_,_%29-9sysp.md)
  Creates a column of doubles by multiplying the given double by each element of the given column.
- [static func / (Int, MLDataColumn<Int>) -> MLDataColumn<Int>](./op%28_,_%29-9ew9w.md)
  Creates a column of integers by dividing the given integer by each element of the given column.
- [static func / (Double, MLDataColumn<Double>) -> MLDataColumn<Double>](./op%28_,_%29-121w8.md)
  Creates a column of doubles by dividing the given double by each element of the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/-(_:_:)-2e7k4)*