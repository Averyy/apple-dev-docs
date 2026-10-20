# init(doubles:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a new column of doubles by converting the elements of another column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(doubles: MLUntypedColumn)
```

#### Return Value

A new untyped column of doubles; otherwise an invalid column if any element of the given column cannot be converted to [`Double`](../../Swift/double.md).

#### Discussion

Use this initializer to create a column of doubles from another column. As an example, to create a column with this initializer, first start with a column that is convertible to doubles.

```swift
let stringColumn = MLUntypedColumn(["1.0", "2.0", "3.0", "4.0", "5.0"])
print(stringColumn)
/* Prints...
 ValueType: String
 Values:        [1.0, 2.0, 3.0, 4.0, 5.0]
 */
```

Then use [`init(doubles:)`](./init%28doubles%29.md) to convert the column to a column of doubles.

```swift
let doublesColumn = MLUntypedColumn(doubles: stringColumn)
print(doublesColumn)
/* Prints...
 ValueType: Double
 Values:        [1.0, 2.0, 3.0, 4.0, 5.0]
 */
```

## Parameters

- `doubles`: A column with elements that are convertible to doubles.

## See Also

### Creating an untyped column by converting another column
- [init(ints: MLUntypedColumn)](./init%28ints%29.md)
  Creates a new column of integers by converting the elements of another column.
- [init(strings: MLUntypedColumn)](./init%28strings%29.md)
  Creates a new column of strings by converting the elements of another column.
- [init(sequences: MLUntypedColumn)](./init%28sequences%29.md)
  Creates a new column of machine learning sequences by converting the elements of another column.
- [init(dictionaries: MLUntypedColumn)](./init%28dictionaries%29.md)
  Creates a new column of machine learning dictionaries by converting the elements of another column.
- [init(multiArrays: MLUntypedColumn)](./init%28multiarrays%29.md)
  Creates a MLUntypedColumn of type MLMultiArray from the specified MLUntypedColumn if the values of the given MLUntypedColumn are convertible to MLDataValue.MultiArrayType.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/init(doubles:))*