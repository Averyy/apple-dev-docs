# column(type:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Clones the column to a data column of the given type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func column<T>(type: T.Type) -> MLDataColumn<T>? where T : MLDataValueConvertible
```

#### Return Value

A new data column if the underlying type of the column is the same as `type`; otherwise `nil`.

#### Discussion

Use this method to create a typed copy of the column. For example, to create a data column of integers from an untyped column of integers, use [`column(type:)`](./column%28type%29.md) with [`Int`](../../Swift/int.md)`.self` as the argument for the `type` parameter.

## Parameters

- `type`: A metatype used to create a new data column of that type.

## See Also

### Exposing the underlying type to generate a data column
- [var type: MLDataValue.ValueType](./type.md)
  The underlying type of the column.
- [var ints: MLDataColumn<Int>?](./ints.md)
  A cloned data column of integers.
- [var doubles: MLDataColumn<Double>?](./doubles.md)
  A cloned data column of doubles.
- [var strings: MLDataColumn<String>?](./strings.md)
  A cloned data column of strings.
- [var sequences: MLDataColumn<MLDataValue.SequenceType>?](./sequences.md)
  A cloned data column of machine learning sequences.
- [var dictionaries: MLDataColumn<MLDataValue.DictionaryType>?](./dictionaries.md)
  A cloned data column of machine learning dictionaries.
- [var multiArrays: MLDataColumn<MLDataValue.MultiArrayType>?](./multiarrays.md)
  A cloned data column of machine learning multi-arrays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/column(type:))*