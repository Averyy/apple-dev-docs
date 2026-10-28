# /(_:_:)

**Framework**: Create ML  
**Kind**: op  
**Role**: Operator

Creates a column of doubles by dividing the given double by each element of the given column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func / (a: Double, b: MLDataColumn<Double>) -> MLDataColumn<Double>
```

Available when `Element` is `Double`.

**Other overloads**:

```swift
static func / (a: Int, b: MLDataColumn<Int>) -> MLDataColumn<Int>
```

```swift
static func / (a: MLDataColumn<Double>, b: Double) -> MLDataColumn<Double>
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

## Return Value

A new column of doubles.

## Parameters

- `a`: A double.
- `b`: A column of doubles.

## See Also

### Combining columns
- [static +(_:_:)](./plus%28_,_%29.md)
  Creates a column of doubles by adding the given double to each element of the given column.
- [static -(_:_:)](./minus%28_,_%29.md)
  Creates a column of doubles by subtracting each element of the given column from the given double.
- [static *(_:_:)](./star%28_,_%29.md)
  Creates a column of doubles by multiplying the given double by each element of the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/_(_:_:)-8hxiv)*