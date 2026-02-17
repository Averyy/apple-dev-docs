# init(rawValue:)

**Framework**: Metal  
**Kind**: init

Creates a data type instance from a raw integer value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
init?(rawValue: UInt)
```

#### Discussion

Use the [`MTLDataType`](mtldatatype.md) structure’s type properties, such as [`MTLDataType.int`](mtldatatype/int.md), instead of this initializer.

## Parameters

- `rawValue`: The underlying integer value that represents a data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldatatype/init(rawvalue:))*