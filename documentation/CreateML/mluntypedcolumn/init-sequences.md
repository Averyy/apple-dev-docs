# init(sequences:)

**Framework**: Create ML  
**Kind**: init

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

#### Return Value

A new untyped column of doubles; otherwise an invalid column if any element of the given column cannot be converted to [`MLDataValue.SequenceType`](mldatavalue/sequencetype.md).

#### Discussion

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

Then use [`init(sequences:)`](mluntypedcolumn/init(sequences:).md) to convert the column to a column of sequences.

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

- [init(ints: MLUntypedColumn)](mluntypedcolumn/init(ints:).md)
  Creates a new column of integers by converting the elements of another column.
- [init(doubles: MLUntypedColumn)](mluntypedcolumn/init(doubles:).md)
  Creates a new column of doubles by converting the elements of another column.
- [init(strings: MLUntypedColumn)](mluntypedcolumn/init(strings:).md)
  Creates a new column of strings by converting the elements of another column.
- [init(dictionaries: MLUntypedColumn)](mluntypedcolumn/init(dictionaries:).md)
  Creates a new column of machine learning dictionaries by converting the elements of another column.
- [init(multiArrays: MLUntypedColumn)](mluntypedcolumn/init(multiarrays:).md)
  Creates a MLUntypedColumn of type MLMultiArray from the specified MLUntypedColumn if the values of the given MLUntypedColumn are convertible to MLDataValue.MultiArrayType.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/init(sequences:))*