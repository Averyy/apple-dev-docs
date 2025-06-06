# multiArrays

**Framework**: Create ML  
**Kind**: property

A cloned data column of machine learning multi-arrays.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var multiArrays: MLDataColumn<MLDataValue.MultiArrayType>? { get }
```

#### Return Value

A new data column if the underlying type of the column is [`MLDataValue.MultiArrayType`](mldatavalue/multiarraytype.md); otherwise `nil`.

#### Discussion

This property is functionally equivalent to passing [`MLDataValue.MultiArrayType`](mldatavalue/multiarraytype.md) `.self` to [`column(type:)`](mluntypedcolumn/column(type:).md). Typically you ensure [`type`](mluntypedcolumn/type.md) is equal to [`MLDataValue.ValueType.multiArray`](mldatavalue/valuetype/multiarray.md) before getting this property.

## See Also

- [var type: MLDataValue.ValueType](mluntypedcolumn/type.md)
  The underlying type of the column.
- [var ints: MLDataColumn<Int>?](mluntypedcolumn/ints.md)
  A cloned data column of integers.
- [var doubles: MLDataColumn<Double>?](mluntypedcolumn/doubles.md)
  A cloned data column of doubles.
- [var strings: MLDataColumn<String>?](mluntypedcolumn/strings.md)
  A cloned data column of strings.
- [var sequences: MLDataColumn<MLDataValue.SequenceType>?](mluntypedcolumn/sequences.md)
  A cloned data column of machine learning sequences.
- [var dictionaries: MLDataColumn<MLDataValue.DictionaryType>?](mluntypedcolumn/dictionaries.md)
  A cloned data column of machine learning dictionaries.
- [func column<T>(type: T.Type) -> MLDataColumn<T>?](mluntypedcolumn/column(type:).md)
  Clones the column to a data column of the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/multiarrays)*