# MLDataValue.DictionaryType

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

A dictionary of named data values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct DictionaryType
```

## Topics

### Creating a dictionary type
- [init([MLDataValue : MLDataValue])](./dictionarytype/init%28_%29.md)
- [init<S>(uniqueKeysWithValues: S)](./dictionarytype/init%28uniquekeyswithvalues%29.md)
- [MLDataValue.DictionaryType.Key](./dictionarytype/key.md)
- [MLDataValue.DictionaryType.Value](./dictionarytype/value.md)
### Getting an element
- [subscript(MLDataValue.DictionaryType.Key) -> MLDataValue.DictionaryType.Value?](./dictionarytype/subscript%28_%29.md)
### Default Implementations
- [MLDataValueConvertible Implementations](./dictionarytype/mldatavalueconvertible-implementations.md)

## Relationships

### Conforms To
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [MLDataValueConvertible](../mldatavalueconvertible.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Accessing dictionary values
- [var dictionaryValue: MLDataValue.DictionaryType?](./dictionaryvalue.md)
  The underlying dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype)*