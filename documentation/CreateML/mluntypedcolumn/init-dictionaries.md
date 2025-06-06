# init(dictionaries:)

**Framework**: Create ML  
**Kind**: init

Creates a new column of machine learning dictionaries by converting the elements of another column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(dictionaries: MLUntypedColumn)
```

#### Return Value

A new untyped column of doubles; otherwise an invalid column if any element of the given column cannot be converted to [`MLDataValue.DictionaryType`](mldatavalue/dictionarytype.md).

#### Discussion

Use this initializer to create a column of dictionaries from another column. As an example, to create a column with this initializer, first start with a column that is convertible to dictionaries.

```swift
let intDictionaryString = "{1:\"one\", 2:\"two\", 3:\"three\"}"
let intDictionaryString2 = "{4:\"four\", 5:\"five\", 6:\"six\"}"
let stringsColumn = MLUntypedColumn([intDictionaryString, intDictionaryString2])

print(stringsColumn)
/* Prints...
 ValueType: String
Values: [{1:"one", 2:"two", 3:"three"}, {4:"four", 5:"five", 6:"six"}]
 */
```

Then use [`init(dictionaries:)`](mluntypedcolumn/init(dictionaries:).md) to convert the column to a column of dictionaries.

```swift
let dictionaryColumn = MLUntypedColumn(dictionaries: stringsColumn)
print(dictionaryColumn)
/* Prints...
 ValueType: Dictionary
 Values:        [[1: one, 3: three, 2: two], [4: four, 5: five, 6: six]]
 */
```

## Parameters

- `dictionaries`: A column with elements that are convertible to Create ML dictionaries.

## See Also

- [init(ints: MLUntypedColumn)](mluntypedcolumn/init(ints:).md)
  Creates a new column of integers by converting the elements of another column.
- [init(doubles: MLUntypedColumn)](mluntypedcolumn/init(doubles:).md)
  Creates a new column of doubles by converting the elements of another column.
- [init(strings: MLUntypedColumn)](mluntypedcolumn/init(strings:).md)
  Creates a new column of strings by converting the elements of another column.
- [init(sequences: MLUntypedColumn)](mluntypedcolumn/init(sequences:).md)
  Creates a new column of machine learning sequences by converting the elements of another column.
- [init(multiArrays: MLUntypedColumn)](mluntypedcolumn/init(multiarrays:).md)
  Creates a MLUntypedColumn of type MLMultiArray from the specified MLUntypedColumn if the values of the given MLUntypedColumn are convertible to MLDataValue.MultiArrayType.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/init(dictionaries:))*