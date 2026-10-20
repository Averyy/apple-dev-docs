# <(_:_:)

**Framework**: Create ML  
**Kind**: op  
**Role**: Operator

Creates a column of Booleans by testing whether the given value is less than each element in the given column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func < (a: Element, b: MLDataColumn<Element>) -> MLDataColumn<Bool>
```

Available when `Element` conforms to `MLDataValueConvertible`.

**Other overloads**:

```swift
static func < (a: MLDataColumn<Element>, b: Element) -> MLDataColumn<Bool>
```

```swift
static func < (a: MLDataColumn<Element>, b: MLDataColumn<Element>) -> MLDataColumn<Bool>
```

#### Return Value

A new column of Booleans.

## Parameters

- `a`: A value of the same type as the elements of the column.
- `b`: A column.

## See Also

### Comparing columns
- [static ==(_:_:)](./eqeq%28_,_%29.md)
  Creates a column of Booleans by testing whether the given value is equal to each element in the given column.
- [static !=(_:_:)](./noteq%28_,_%29.md)
  Creates a column of Booleans by testing whether the given value is not equal to each element in the given column.
- [static <=(_:_:)](./opeq%28_,_%29-8eq6v.md)
  Creates a column of Booleans by testing whether the given value is less than or equal to each element in the given column.
- [static >(_:_:)](./op%28_,_%29-g252.md)
  Creates a column of Booleans by testing whether the given value is greater than each element in the given column.
- [static >=(_:_:)](./opeq%28_,_%29-64izf.md)
  Creates a column of Booleans by testing whether the given value is greater than or equal to each element in the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/_(_:_:)-81qel)*