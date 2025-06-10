# NFCTypeNameFormat

**Framework**: Core NFC  
**Kind**: enum

The Type Name Format values that specify the content type for the payload data in an NFC NDEF message.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum NFCTypeNameFormat
```

## Topics

### Content Types
- [NFCTypeNameFormat.absoluteURI](nfctypenameformat/absoluteuri.md)
  A type indicating that the payload contains a uniform resource identifier.
- [NFCTypeNameFormat.empty](nfctypenameformat/empty.md)
  A type indicating that the payload contains no data.
- [NFCTypeNameFormat.media](nfctypenameformat/media.md)
  A type indicating that the payload contains media data as defined by RFC 2046.
- [NFCTypeNameFormat.nfcExternal](nfctypenameformat/nfcexternal.md)
  A type indicating that the payload contains NFC external type data.
- [NFCTypeNameFormat.nfcWellKnown](nfctypenameformat/nfcwellknown.md)
  A type indicating that the payload contains well-known NFC record type data.
- [NFCTypeNameFormat.unchanged](nfctypenameformat/unchanged.md)
  A type indicating that the payload is part of a series of records containing chunked data.
- [NFCTypeNameFormat.unknown](nfctypenameformat/unknown.md)
  A type indicating that the payload data type is unknown.
### Initializers
- [init?(rawValue: UInt8)](nfctypenameformat/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var identifier: Data](nfcndefpayload/identifier.md)
  The identifier of the payload, as defined by the NDEF specification.
- [var payload: Data](nfcndefpayload/payload.md)
  The payload, as defined by the NDEF specification.
- [var type: Data](nfcndefpayload/type.md)
  The type of the payload, as defined by the NDEF specification.
- [var typeNameFormat: NFCTypeNameFormat](nfcndefpayload/typenameformat.md)
  The Type Name Format field of the payload, as defined by the NDEF specification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctypenameformat)*