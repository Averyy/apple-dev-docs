# init(multiArrays:)

**Framework**: Create ML  
**Kind**: init

Creates a MLUntypedColumn of type MLMultiArray from the specified MLUntypedColumn if the values of the given MLUntypedColumn are convertible to MLDataValue.MultiArrayType.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(multiArrays: MLUntypedColumn)
```

#### Return Value

A MLUntypedColumn of type MultiArray from the specified MLUntypedColumn if the given MLUntypedColumn’s values are convertible to MLDataValue.MultiArrayType. Returns an invalid MLUntypedColumn if the elements in the given MLUntypedColumn are not convertible to MLDataValue.MultiArrayType.

## Parameters

- `multiArrays`: A MLUntypedColumn from which to create a MLUntypedColumn with type   MLDataValue.DictionaryType

## See Also

- [init(ints: MLUntypedColumn)](mluntypedcolumn/init(ints:).md)
  Creates a new column of integers by converting the elements of another column.
- [init(doubles: MLUntypedColumn)](mluntypedcolumn/init(doubles:).md)
  Creates a new column of doubles by converting the elements of another column.
- [init(strings: MLUntypedColumn)](mluntypedcolumn/init(strings:).md)
  Creates a new column of strings by converting the elements of another column.
- [init(sequences: MLUntypedColumn)](mluntypedcolumn/init(sequences:).md)
  Creates a new column of machine learning sequences by converting the elements of another column.
- [init(dictionaries: MLUntypedColumn)](mluntypedcolumn/init(dictionaries:).md)
  Creates a new column of machine learning dictionaries by converting the elements of another column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/init(multiarrays:))*