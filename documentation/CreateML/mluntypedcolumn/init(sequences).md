# init(sequences:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a new column of machine learning sequences by converting the elements of another column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(sequences: MLUntypedColumn)
```

## Return Value

A new untyped column of doubles; otherwise an invalid column if any element of the given column cannot be converted to [`MLDataValue.SequenceType`](../mldatavalue/sequencetype.md).

## Discussion

Use this initializer to create a column of sequences from another column. As an example, to create a column with this initializer, first start with a column that is convertible to sequences.

```swift
let intSequenceString = "[1, 2, 3]"
let intSequenceString2 = "[4, 5, 6]"
let stringsColumn = MLUntypedColumn([intSequenceString, intSequenceString2])

print(stringsColumn)
/* Prints...
 ValueType: String
 Values:        [[1, 2, 3], [4, 5, 6]]
 */
```

Then use [`init(sequences:)`](./init%28sequences%29.md) to convert the column to a column of sequences.

```swift
let sequenceColumn = MLUntypedColumn(sequences: stringsColumn)
print(sequenceColumn)
/* Prints...
 ValueType: Sequence
 Values:        [[DataValue(1), DataValue(2), DataValue(3)],
                 [DataValue(4), DataValue(5), DataValue(6)]]
 */
```

## Parameters

- `sequences`: A column with elements that are convertible to Create ML sequences.

## See Also

### Creating an untyped column by converting another column
- [init(ints: MLUntypedColumn)](./init%28ints%29.md)
  Creates a new column of integers by converting the elements of another column.
- [init(doubles: MLUntypedColumn)](./init%28doubles%29.md)
  Creates a new column of doubles by converting the elements of another column.
- [init(strings: MLUntypedColumn)](./init%28strings%29.md)
  Creates a new column of strings by converting the elements of another column.
- [init(dictionaries: MLUntypedColumn)](./init%28dictionaries%29.md)
  Creates a new column of machine learning dictionaries by converting the elements of another column.
- [init(multiArrays: MLUntypedColumn)](./init%28multiarrays%29.md)
  Creates a MLUntypedColumn of type MLMultiArray from the specified MLUntypedColumn if the values of the given MLUntypedColumn are convertible to MLDataValue.MultiArrayType.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/init(sequences:))*