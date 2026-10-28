# <(_:_:)

**Framework**: Create ML  
**Kind**: op  
**Role**: Operator

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

Available when `Element` conforms to `MLDataValueConvertible`.

**Other overloads**:

```swift
static func < (a: Element, b: MLDataColumn<Element>) -> MLDataColumn<Bool>
```

```swift
static func < (a: MLDataColumn<Element>, b: MLDataColumn<Element>) -> MLDataColumn<Bool>
```

## Return Value

A new column of Booleans.

## Parameters

- `a`: A column.
- `b`: A value of the same type as the elements of the column.

## See Also

### Comparing a column with a value to generate a column of booleans
- [static func == (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](./eqeq%28_,_%29-7clbs.md)
  Creates a column of Booleans by testing whether each element in the given column is equal to the given value.
- [static func != (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](./noteq%28_,_%29-4jp0y.md)
  Creates a column of Booleans by testing whether each element in the given column is not equal to the given value.
- [static func <= (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](./opeq%28_,_%29-86x3a.md)
  Creates a column of Booleans by testing whether each element in the given column is less than or equal to the given value.
- [static func > (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](./op%28_,_%29-ebgq.md)
  Creates a column of Booleans by testing whether each element in the given column is greater than the given value.
- [static func >= (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](./opeq%28_,_%29-1ctuz.md)
  Creates a column of Booleans by testing whether each element in the given column is greater than or equal to the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/_(_:_:)-4ujss)*