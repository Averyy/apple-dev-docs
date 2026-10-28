# init(strings:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a new column of strings by converting the elements of another column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(strings: MLUntypedColumn)
```

## Return Value

A new untyped column of doubles; otherwise an invalid column if any element of the given column cannot be converted to [`String`](../../Swift/string.md).

## Discussion

Use this initializer to create a column of strings from another column. As an example, to create a column with this initializer, first start with a column that is convertible to strings.

```swift
let doublesColumn = MLUntypedColumn([1.0, 2.718, 3.14, 4.2, 5.1])
print(doublesColumn)
/* Prints...
 ValueType: Double
 Values:        [1.0, 2.718, 3.14, 4.2, 5.1]
 */
```

Then use [`init(strings:)`](./init%28strings%29.md) to convert the column to a column of strings.

```swift
let stringsColumn = MLUntypedColumn(strings: doublesColumn)
print(stringsColumn)
/* Prints...
 ValueType: String
 Values:        [1, 2.718, 3.14, 4.2, 5.1]
 */
```

## Parameters

- `strings`: A column with elements that are convertible to string.

## See Also

### Creating an untyped column by converting another column
- [init(ints: MLUntypedColumn)](./init%28ints%29.md)
  Creates a new column of integers by converting the elements of another column.
- [init(doubles: MLUntypedColumn)](./init%28doubles%29.md)
  Creates a new column of doubles by converting the elements of another column.
- [init(sequences: MLUntypedColumn)](./init%28sequences%29.md)
  Creates a new column of machine learning sequences by converting the elements of another column.
- [init(dictionaries: MLUntypedColumn)](./init%28dictionaries%29.md)
  Creates a new column of machine learning dictionaries by converting the elements of another column.
- [init(multiArrays: MLUntypedColumn)](./init%28multiarrays%29.md)
  Creates a MLUntypedColumn of type MLMultiArray from the specified MLUntypedColumn if the values of the given MLUntypedColumn are convertible to MLDataValue.MultiArrayType.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/init(strings:))*