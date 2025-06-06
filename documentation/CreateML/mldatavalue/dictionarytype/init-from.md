# init(from:)

**Framework**: Create ML  
**Kind**: init

Creates a data-value dictionary from another dictionary.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init?(from dataValue: MLDataValue)
```

#### Discussion

Use this initializer to create an [`MLDataValue.DictionaryType`](mldatavalue/dictionarytype.md) from another data-value dictionary instance. You can confirm the data value’s underlying type by retrieving a non-`nil` value from [`dictionaryValue`](mldatavalue/dictionaryvalue.md) or by inspecting the [`type`](mldatavalue/type.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/init(from:))*