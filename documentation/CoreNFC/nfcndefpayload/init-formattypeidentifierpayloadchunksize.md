# init(format:type:identifier:payload:chunkSize:)

**Framework**: Core NFC  
**Kind**: init

Creates a payload record with the specified format, type, identifier, payload data, and data chunk size.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(format: NFCTypeNameFormat, type: Data, identifier: Data, payload: Data, chunkSize: Int)
```

#### Return Value

A newly initialized payload record object.

## Parameters

- `format`: A NFC type name format value.
- `type`: A data object describing the type of payload. If the data is empty, the method excludes this field from the payload record.
- `identifier`: A URI reference that identifies the payload. If the data is empty, the method excludes this field from the payload record.
- `payload`: A data object containing the payload data. If the data is empty, the method excludes this field from the payload record.
- `chunkSize`: The maximum size of a payload chunk. A value of zero indicates that the payload fits in a single record, that is, no chunking of the payload.

## See Also

- [class func wellKnownTypeURIPayload(url: URL) -> Self?](nfcndefpayload/wellknowntypeuripayload(url:).md)
  Creates a payload record with a URI specified as a URL.
- [class func wellKnownTypeURIPayload(string: String) -> Self?](nfcndefpayload/wellknowntypeuripayload(string:).md)
  Creates a payload record with a URI specified as a string.
- [class func wellKnownTypeTextPayload(string: String, locale: Locale) -> Self?](nfcndefpayload/wellknowntypetextpayload(string:locale:).md)
  Creates a payload record with text.
- [init(format: NFCTypeNameFormat, type: Data, identifier: Data, payload: Data)](nfcndefpayload/init(format:type:identifier:payload:).md)
  Creates a payload record with the specified format, type, identifier, and payload data.
- [class func wellKnowTypeTextPayload(string: String, locale: Locale) -> Self?](nfcndefpayload/wellknowtypetextpayload(string:locale:).md)
  Creates a payload record with text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefpayload/init(format:type:identifier:payload:chunksize:))*