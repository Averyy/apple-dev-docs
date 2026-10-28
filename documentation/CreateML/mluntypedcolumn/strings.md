# strings

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

A cloned data column of strings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var strings: MLDataColumn<String>? { get }
```

## Return Value

A new data column if the underlying type of the column is [`String`](../../Swift/string.md); otherwise `nil`.

## Discussion

This property is functionally equivalent to passing [`String`](../../Swift/string.md)`.self` to [`column(type:)`](./column%28type%29.md). Typically you ensure [`type`](./type.md) is equal to [`MLDataValue.ValueType.string`](../mldatavalue/valuetype/string.md) before getting this property.

## See Also

### Exposing the underlying type to generate a data column
- [var type: MLDataValue.ValueType](./type.md)
  The underlying type of the column.
- [var ints: MLDataColumn<Int>?](./ints.md)
  A cloned data column of integers.
- [var doubles: MLDataColumn<Double>?](./doubles.md)
  A cloned data column of doubles.
- [var sequences: MLDataColumn<MLDataValue.SequenceType>?](./sequences.md)
  A cloned data column of machine learning sequences.
- [var dictionaries: MLDataColumn<MLDataValue.DictionaryType>?](./dictionaries.md)
  A cloned data column of machine learning dictionaries.
- [var multiArrays: MLDataColumn<MLDataValue.MultiArrayType>?](./multiarrays.md)
  A cloned data column of machine learning multi-arrays.
- [func column<T>(type: T.Type) -> MLDataColumn<T>?](./column%28type%29.md)
  Clones the column to a data column of the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/strings)*