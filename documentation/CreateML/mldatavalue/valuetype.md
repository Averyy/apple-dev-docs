# MLDataValue.ValueType

**Framework**: Create ML  
**Kind**: enum

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
- [MLDataValue.ValueType.int](mldatavalue/valuetype/int.md)
  An integer type.
- [MLDataValue.ValueType.double](mldatavalue/valuetype/double.md)
  A double type.
- [MLDataValue.ValueType.string](mldatavalue/valuetype/string.md)
  A string type.
- [MLDataValue.ValueType.dictionary](mldatavalue/valuetype/dictionary.md)
  A dictionary type.
- [MLDataValue.ValueType.sequence](mldatavalue/valuetype/sequence.md)
  A sequence type.
- [MLDataValue.ValueType.multiArray](mldatavalue/valuetype/multiarray.md)
  A multidimensional type.
- [MLDataValue.ValueType.invalid](mldatavalue/valuetype/invalid.md)
  An invalid type.
### Describing a data value type
- [var description: String](mldatavalue/valuetype/description.md)
  A text representation of the data value type.
- [var debugDescription: String](mldatavalue/valuetype/debugdescription.md)
  A text representation of the data value type that’s suitable for output during debugging.
### Comparing value types
- [static func != (Self, Self) -> Bool](mldatavalue/valuetype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Operators
- [static func == (MLDataValue.ValueType, MLDataValue.ValueType) -> Bool](mldatavalue/valuetype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mldatavalue/valuetype/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mldatavalue/valuetype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mldatavalue/valuetype/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](mldatavalue/valuetype/customstringconvertible-implementations.md)
- [Equatable Implementations](mldatavalue/valuetype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var type: MLDataValue.ValueType](mldatavalue/type.md)
  The kind of the underlying value that the data value wraps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/valuetype)*