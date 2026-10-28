# wellKnowTypeTextPayload(string:locale:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Type Method

Creates a payload record with text.

**Availability**:
- iOS 13.0+ - Deprecated in 13.0
- iPadOS 13.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
class func wellKnowTypeTextPayload(string text: String, locale: Locale) -> Self?
```

```objc
+ (instancetype) wellKnowTypeTextPayloadWithString:(NSString *) text locale:(NSLocale *) locale;
```

## Return Value

An NDEF payload record.

## See Also

### Creating a Payload Record
- [class func wellKnownTypeURIPayload(url: URL) -> Self?](./wellknowntypeuripayload%28url%29.md)
  Creates a payload record with a URI specified as a URL.
- [class func wellKnownTypeURIPayload(string: String) -> Self?](./wellknowntypeuripayload%28string%29.md)
  Creates a payload record with a URI specified as a string.
- [class func wellKnownTypeTextPayload(string: String, locale: Locale) -> Self?](./wellknowntypetextpayload%28string,locale%29.md)
  Creates a payload record with text.
- [init(format: NFCTypeNameFormat, type: Data, identifier: Data, payload: Data)](./init%28format,type,identifier,payload%29.md)
  Creates a payload record with the specified format, type, identifier, and payload data.
- [init(format: NFCTypeNameFormat, type: Data, identifier: Data, payload: Data, chunkSize: Int)](./init%28format,type,identifier,payload,chunksize%29.md)
  Creates a payload record with the specified format, type, identifier, payload data, and data chunk size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefpayload/wellknowtypetextpayload(string:locale:))*