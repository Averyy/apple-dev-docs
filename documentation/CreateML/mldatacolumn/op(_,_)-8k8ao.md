# /(_:_:)

**Framework**: Create ML  
**Kind**: op  
**Role**: Operator

Creates a column of doubles by dividing each element of the given column by the given double.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func / (a: MLDataColumn<Double>, b: Double) -> MLDataColumn<Double>
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
static func / (a: MLDataColumn<Double>, b: MLDataColumn<Double>) -> MLDataColumn<Double>
```

```swift
static func / (a: MLDataColumn<Int>, b: Int) -> MLDataColumn<Int>
```

```swift
static func / (a: MLDataColumn<Int>, b: MLDataColumn<Int>) -> MLDataColumn<Int>
```

#### Return Value

A new column of doubles.

## Parameters

- `a`: A column of doubles.
- `b`: A double.

## See Also

### Combining a column with a value to generate a column
- [static func + (MLDataColumn<Int>, Int) -> MLDataColumn<Int>](./plus%28_,_%29-7tghu.md)
  Creates a column of integers by adding each element of the given column to the given integer.
- [static func + (MLDataColumn<Double>, Double) -> MLDataColumn<Double>](./plus%28_,_%29-4se2l.md)
  Creates a column of doubles by adding each element of the given column to the given double.
- [static func - (MLDataColumn<Int>, Int) -> MLDataColumn<Int>](./minus%28_,_%29-2sddu.md)
  Creates a column of integers by subtracting the given integer from each element of the given column.
- [static func - (MLDataColumn<Double>, Double) -> MLDataColumn<Double>](./minus%28_,_%29-9smok.md)
  Creates a column of doubles by subtracting the given double from each element of the given column.
- [static func * (MLDataColumn<Int>, Int) -> MLDataColumn<Int>](./star%28_,_%29-2zih0.md)
  Creates a column of integers by multiplying each element of the given column by the given integer.
- [static func * (MLDataColumn<Double>, Double) -> MLDataColumn<Double>](./star%28_,_%29-4ilhj.md)
  Creates a column of doubles by multiplying each element of the given column by the given double.
- [static func / (MLDataColumn<Int>, Int) -> MLDataColumn<Int>](./op%28_,_%29-3ea6t.md)
  Creates a column of integers by dividing each element of the given column by the given integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/_(_:_:)-8k8ao)*