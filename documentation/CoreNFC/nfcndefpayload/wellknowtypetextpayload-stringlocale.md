# wellKnowTypeTextPayload(string:locale:)

**Framework**: Core NFC  
**Kind**: method

Creates a payload record with text.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class func wellKnowTypeTextPayload(string text: String, locale: Locale) -> Self?
```

#### Return Value

An NDEF payload record.

## See Also

- [class func wellKnownTypeURIPayload(url: URL) -> Self?](nfcndefpayload/wellknowntypeuripayload(url:).md)
  Creates a payload record with a URI specified as a URL.
- [class func wellKnownTypeURIPayload(string: String) -> Self?](nfcndefpayload/wellknowntypeuripayload(string:).md)
  Creates a payload record with a URI specified as a string.
- [class func wellKnownTypeTextPayload(string: String, locale: Locale) -> Self?](nfcndefpayload/wellknowntypetextpayload(string:locale:).md)
  Creates a payload record with text.
- [init(format: NFCTypeNameFormat, type: Data, identifier: Data, payload: Data)](nfcndefpayload/init(format:type:identifier:payload:).md)
  Creates a payload record with the specified format, type, identifier, and payload data.
- [init(format: NFCTypeNameFormat, type: Data, identifier: Data, payload: Data, chunkSize: Int)](nfcndefpayload/init(format:type:identifier:payload:chunksize:).md)
  Creates a payload record with the specified format, type, identifier, payload data, and data chunk size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefpayload/wellknowtypetextpayload(string:locale:))*