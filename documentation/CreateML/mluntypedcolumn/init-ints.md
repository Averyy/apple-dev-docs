# init(ints:)

**Framework**: Create ML  
**Kind**: init

Creates a new column of integers by converting the elements of another column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(ints: MLUntypedColumn)
```

#### Return Value

A new untyped column of integers; otherwise an invalid column if any element of the given column cannot be converted to [`Int`](https://developer.apple.com/documentation/Swift/Int).

#### Discussion

Use this initializer to create a column of integers from another column. As an example, to create a column with this initializer, first start with a column that is convertible to integers.

```swift
let stringColumn = MLUntypedColumn(["1", "2", "3", "4", "5"])
print(stringColumn)
/* Prints...
 ValueType: String
 Values:        [1, 2, 3, 4, 5]
 */
```

Then use [`init(ints:)`](mluntypedcolumn/init(ints:).md) to convert the column to a column of integers.

```swift
let intsColumn = MLUntypedColumn(ints: stringColumn)
print(intsColumn)
/* Prints...
 ValueType: Int
 Values:        [1, 2, 3, 4, 5]
 */
```

## Parameters

- `ints`: A column with elements that are convertible to integers.

## See Also

- [init(doubles: MLUntypedColumn)](mluntypedcolumn/init(doubles:).md)
  Creates a new column of doubles by converting the elements of another column.
- [init(strings: MLUntypedColumn)](mluntypedcolumn/init(strings:).md)
  Creates a new column of strings by converting the elements of another column.
- [init(sequences: MLUntypedColumn)](mluntypedcolumn/init(sequences:).md)
  Creates a new column of machine learning sequences by converting the elements of another column.
- [init(dictionaries: MLUntypedColumn)](mluntypedcolumn/init(dictionaries:).md)
  Creates a new column of machine learning dictionaries by converting the elements of another column.
- [init(multiArrays: MLUntypedColumn)](mluntypedcolumn/init(multiarrays:).md)
  Creates a MLUntypedColumn of type MLMultiArray from the specified MLUntypedColumn if the values of the given MLUntypedColumn are convertible to MLDataValue.MultiArrayType.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/init(ints:))*