# init(from:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a data-value sequence from another sequence.

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

## Discussion

Use this initializer to create an [`MLDataValue.SequenceType`](../sequencetype.md) from another data-value sequence instance. You can confirm the data value’s underlying type by retrieving a non-`nil` value from [`sequenceValue`](../sequencevalue.md) or by inspecting the [`type`](../type.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/sequencetype/init(from:))*