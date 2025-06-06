# sequences

**Framework**: Create ML  
**Kind**: property

A cloned data column of machine learning sequences.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var sequences: MLDataColumn<MLDataValue.SequenceType>? { get }
```

#### Return Value

A new data column if the underlying type of the column is [`MLDataValue.SequenceType`](mldatavalue/sequencetype.md); otherwise `nil`.

#### Discussion

This property is functionally equivalent to passing [`MLDataValue.SequenceType`](mldatavalue/sequencetype.md) `.self` to [`column(type:)`](mluntypedcolumn/column(type:).md). Typically you ensure [`type`](mluntypedcolumn/type.md) is equal to [`MLDataValue.ValueType.sequence`](mldatavalue/valuetype/sequence.md) before getting this property.

## See Also

- [var type: MLDataValue.ValueType](mluntypedcolumn/type.md)
  The underlying type of the column.
- [var ints: MLDataColumn<Int>?](mluntypedcolumn/ints.md)
  A cloned data column of integers.
- [var doubles: MLDataColumn<Double>?](mluntypedcolumn/doubles.md)
  A cloned data column of doubles.
- [var strings: MLDataColumn<String>?](mluntypedcolumn/strings.md)
  A cloned data column of strings.
- [var dictionaries: MLDataColumn<MLDataValue.DictionaryType>?](mluntypedcolumn/dictionaries.md)
  A cloned data column of machine learning dictionaries.
- [var multiArrays: MLDataColumn<MLDataValue.MultiArrayType>?](mluntypedcolumn/multiarrays.md)
  A cloned data column of machine learning multi-arrays.
- [func column<T>(type: T.Type) -> MLDataColumn<T>?](mluntypedcolumn/column(type:).md)
  Clones the column to a data column of the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/sequences)*