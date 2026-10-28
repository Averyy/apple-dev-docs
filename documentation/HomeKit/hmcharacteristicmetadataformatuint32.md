# HMCharacteristicMetadataFormatUInt32

**Framework**: HomeKit  
**Kind**: var  
**Role**: Global Variable

Indicates that the characteristic has unsigned 32-bit integer values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMCharacteristicMetadataFormatUInt32: String
```

```c
extern NSString * const HMCharacteristicMetadataFormatUInt32;
```

## Discussion

The value is an [`NSNumber`](../Foundation/nsnumber.md) object containing an unsigned 32-bit integer with a range `[0, 4294967295]`.

## See Also

### Unsigned Integers
- [let HMCharacteristicMetadataFormatUInt8: String](./hmcharacteristicmetadataformatuint8.md)
  Indicates that the characteristic has unsigned 8-bit integer values.
- [let HMCharacteristicMetadataFormatUInt16: String](./hmcharacteristicmetadataformatuint16.md)
  Indicates that the characteristic has unsigned 16-bit integer values.
- [let HMCharacteristicMetadataFormatUInt64: String](./hmcharacteristicmetadataformatuint64.md)
  Indicates that the characteristic has unsigned 64-bit integer values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadataformatuint32)*