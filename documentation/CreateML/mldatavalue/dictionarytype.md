# MLDataValue.DictionaryType

**Framework**: Create ML  
**Kind**: struct

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
- [init([MLDataValue : MLDataValue])](mldatavalue/dictionarytype/init(_:).md)
- [init<S>(uniqueKeysWithValues: S)](mldatavalue/dictionarytype/init(uniquekeyswithvalues:).md)
- [MLDataValue.DictionaryType.Key](mldatavalue/dictionarytype/key.md)
- [MLDataValue.DictionaryType.Value](mldatavalue/dictionarytype/value.md)
### Getting an element
- [subscript(MLDataValue.DictionaryType.Key) -> MLDataValue.DictionaryType.Value?](mldatavalue/dictionarytype/subscript(_:).md)
### Default Implementations
- [MLDataValueConvertible Implementations](mldatavalue/dictionarytype/mldatavalueconvertible-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [MLDataValueConvertible](mldatavalueconvertible.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [var dictionaryValue: MLDataValue.DictionaryType?](mldatavalue/dictionaryvalue.md)
  The underlying dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype)*