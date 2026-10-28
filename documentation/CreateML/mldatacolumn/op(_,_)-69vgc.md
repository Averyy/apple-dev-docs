# /(_:_:)

**Framework**: Create ML  
**Kind**: op  
**Role**: Operator

Creates a column of doubles by dividing each element in the first column by the corresponding element in the second column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func / (a: MLDataColumn<Double>, b: MLDataColumn<Double>) -> MLDataColumn<Double>
```

Available when `Element` is `Double`.

**Other overloads**:

```swift
static func / (a: Double, b: MLDataColumn<Double>) -> MLDataColumn<Double>
```

```swift
static func / (a: Int, b: MLDataColumn<Int>) -> MLDataColumn<Int>
```

```swift
static func / (a: MLDataColumn<Double>, b: Double) -> MLDataColumn<Double>
```

```swift
static func / (a: MLDataColumn<Int>, b: Int) -> MLDataColumn<Int>
```

```swift
static func / (a: MLDataColumn<Int>, b: MLDataColumn<Int>) -> MLDataColumn<Int>
```

## Return Value

A new column of doubles if the columns are the same size; otherwise an invalid column.

## Parameters

- `a`: A column of doubles.
- `b`: A column of doubles.

## See Also

### Combining columns to generate a column
- [static func + (MLDataColumn<Int>, MLDataColumn<Int>) -> MLDataColumn<Int>](./plus%28_,_%29-24g38.md)
  Creates a column of integers by adding each element in the first column to the corresponding element in the second column.
- [static func + (MLDataColumn<Double>, MLDataColumn<Double>) -> MLDataColumn<Double>](./plus%28_,_%29-q5bb.md)
  Creates a column of doubles by adding each element in the first column to the corresponding element in the second column.
- [static func - (MLDataColumn<Int>, MLDataColumn<Int>) -> MLDataColumn<Int>](./minus%28_,_%29-11hbf.md)
  Creates a column of integers by subtracting each element in the second column from the corresponding element in the first column.
- [static func - (MLDataColumn<Double>, MLDataColumn<Double>) -> MLDataColumn<Double>](./minus%28_,_%29-3mwsr.md)
  Creates a column of doubles by subtracting each element in the second column from the corresponding element in the first column.
- [static func * (MLDataColumn<Int>, MLDataColumn<Int>) -> MLDataColumn<Int>](./star%28_,_%29-40smy.md)
  Creates a column of integers by multiplying each element in the first column by the corresponding element in the second column.
- [static func * (MLDataColumn<Double>, MLDataColumn<Double>) -> MLDataColumn<Double>](./star%28_,_%29-lchb.md)
  Creates a column of doubles by multiplying each element in the first column by the corresponding element in the second column.
- [static func / (MLDataColumn<Int>, MLDataColumn<Int>) -> MLDataColumn<Int>](./op%28_,_%29-5uxby.md)
  Creates a column of integers by dividing each element in the first column by the corresponding element in the second column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/_(_:_:)-69vgc)*