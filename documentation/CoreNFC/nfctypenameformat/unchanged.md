# NFCTypeNameFormat.unchanged

**Framework**: Core NFC  
**Kind**: case

A type indicating that the payload is part of a series of records containing chunked data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case unchanged
```

#### Discussion

The first record in a series of chunked data records indicates the type name format for the series. The remaining records have a type name format of [`NFCTypeNameFormat.unchanged`](nfctypenameformat/unchanged.md).

## See Also

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
- [NFCTypeNameFormat.unknown](nfctypenameformat/unknown.md)
  A type indicating that the payload data type is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctypenameformat/unchanged)*