# type

**Framework**: Create ML  
**Kind**: property

The underlying type of the column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var type: MLDataValue.ValueType { get }
```

#### Discussion

Use this to determine the underlying type of the column. Then use a corresponding property or method to create an [`MLDataColumn`](mldatacolumn.md) of the untyped column. For example, if [`type`](mluntypedcolumn/type.md) is equal to [`MLDataValue.ValueType.double`](mldatavalue/valuetype/double.md), then use the [`MLUntypedColumn`](mluntypedcolumn.md) [`doubles`](mluntypedcolumn/doubles.md) property.

## See Also

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
- [var multiArrays: MLDataColumn<MLDataValue.MultiArrayType>?](mluntypedcolumn/multiarrays.md)
  A cloned data column of machine learning multi-arrays.
- [func column<T>(type: T.Type) -> MLDataColumn<T>?](mluntypedcolumn/column(type:).md)
  Clones the column to a data column of the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/type)*