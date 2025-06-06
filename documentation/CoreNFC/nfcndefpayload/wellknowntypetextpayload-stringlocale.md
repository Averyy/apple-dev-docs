# wellKnownTypeTextPayload(string:locale:)

**Framework**: Core NFC  
**Kind**: method

Creates a payload record with text.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class func wellKnownTypeTextPayload(string text: String, locale: Locale) -> Self?
```

#### Return Value

An NDEF payload record.

## Parameters

- `text`: Text to include in the payload.
- `locale`: A locale object. This method saves the IANA language code, specified by the locale, to the payload.

## See Also

- [class func wellKnownTypeURIPayload(url: URL) -> Self?](nfcndefpayload/wellknowntypeuripayload(url:).md)
  Creates a payload record with a URI specified as a URL.
- [class func wellKnownTypeURIPayload(string: String) -> Self?](nfcndefpayload/wellknowntypeuripayload(string:).md)
  Creates a payload record with a URI specified as a string.
- [init(format: NFCTypeNameFormat, type: Data, identifier: Data, payload: Data)](nfcndefpayload/init(format:type:identifier:payload:).md)
  Creates a payload record with the specified format, type, identifier, and payload data.
- [init(format: NFCTypeNameFormat, type: Data, identifier: Data, payload: Data, chunkSize: Int)](nfcndefpayload/init(format:type:identifier:payload:chunksize:).md)
  Creates a payload record with the specified format, type, identifier, payload data, and data chunk size.
- [class func wellKnowTypeTextPayload(string: String, locale: Locale) -> Self?](nfcndefpayload/wellknowtypetextpayload(string:locale:).md)
  Creates a payload record with text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefpayload/wellknowntypetextpayload(string:locale:))*