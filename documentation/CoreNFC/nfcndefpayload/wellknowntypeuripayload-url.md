# wellKnownTypeURIPayload(url:)

**Framework**: Core NFC  
**Kind**: method

Creates a payload record with a URI specified as a URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class func wellKnownTypeURIPayload(url: URL) -> Self?
```

#### Return Value

An NDEF payload record.

## Parameters

- `url`: A URL object.

## See Also

- [class func wellKnownTypeURIPayload(string: String) -> Self?](nfcndefpayload/wellknowntypeuripayload(string:).md)
  Creates a payload record with a URI specified as a string.
- [class func wellKnownTypeTextPayload(string: String, locale: Locale) -> Self?](nfcndefpayload/wellknowntypetextpayload(string:locale:).md)
  Creates a payload record with text.
- [init(format: NFCTypeNameFormat, type: Data, identifier: Data, payload: Data)](nfcndefpayload/init(format:type:identifier:payload:).md)
  Creates a payload record with the specified format, type, identifier, and payload data.
- [init(format: NFCTypeNameFormat, type: Data, identifier: Data, payload: Data, chunkSize: Int)](nfcndefpayload/init(format:type:identifier:payload:chunksize:).md)
  Creates a payload record with the specified format, type, identifier, payload data, and data chunk size.
- [class func wellKnowTypeTextPayload(string: String, locale: Locale) -> Self?](nfcndefpayload/wellknowtypetextpayload(string:locale:).md)
  Creates a payload record with text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefpayload/wellknowntypeuripayload(url:))*