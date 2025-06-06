# HMCharacteristicMetadataFormatTLV8

**Framework**: HomeKit  
**Kind**: var

Indicates that the characteristic has TLV8 values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMCharacteristicMetadataFormatTLV8: String
```

#### Discussion

The value is an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object containing a set of one or more TLV8’s, which are packed type-length-value items with an 8-bit type, 8-bit length, and N-byte value.

## See Also

- [let HMCharacteristicMetadataFormatData: String](hmcharacteristicmetadataformatdata.md)
  Indicates that the characteristic has data blob values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadataformattlv8)*