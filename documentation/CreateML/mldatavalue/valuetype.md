# MLDataValue.ValueType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

An enumeration describing the supported underlying types that an `MLDataValue wraps`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum ValueType
```

## Topics

### Supported values
- [MLDataValue.ValueType.int](./valuetype/int.md)
  An integer type.
- [MLDataValue.ValueType.double](./valuetype/double.md)
  A double type.
- [MLDataValue.ValueType.string](./valuetype/string.md)
  A string type.
- [MLDataValue.ValueType.dictionary](./valuetype/dictionary.md)
  A dictionary type.
- [MLDataValue.ValueType.sequence](./valuetype/sequence.md)
  A sequence type.
- [MLDataValue.ValueType.multiArray](./valuetype/multiarray.md)
  A multidimensional type.
- [MLDataValue.ValueType.invalid](./valuetype/invalid.md)
  An invalid type.
### Describing a data value type
- [var description: String](./valuetype/description.md)
  A text representation of the data value type.
- [var debugDescription: String](./valuetype/debugdescription.md)
  A text representation of the data value type that’s suitable for output during debugging.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./valuetype/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./valuetype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Inspecting the type
- [var type: MLDataValue.ValueType](./type.md)
  The kind of the underlying value that the data value wraps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/valuetype)*