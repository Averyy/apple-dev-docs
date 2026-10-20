# init(uniqueKeysWithValues:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init<S>(uniqueKeysWithValues keysAndValues: S) where S : Sequence, S.Element == (MLDataValue, MLDataValue)
```

## See Also

### Creating a dictionary type
- [init([MLDataValue : MLDataValue])](./init%28_%29.md)
- [MLDataValue.DictionaryType.Key](./key.md)
- [MLDataValue.DictionaryType.Value](./value.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/init(uniquekeyswithvalues:))*