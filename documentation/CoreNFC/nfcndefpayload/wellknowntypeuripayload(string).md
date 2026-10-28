# wellKnownTypeURIPayload(string:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Type Method

Creates a payload record with a URI specified as a string.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class func wellKnownTypeURIPayload(string uri: String) -> Self?
```

```objc
+ (instancetype) wellKnownTypeURIPayloadWithString:(NSString *) uri;
```

## Return Value

An NDEF payload record.

## Discussion

Use this method to create NDEF URI payload records that you can’t create using a URL object, such as a URI containing special characters not represented by 7-bit ASCII encoding such as ä and ö.

## Parameters

- `uri`: A URL string.

## See Also

### Creating a Payload Record
- [class func wellKnownTypeURIPayload(url: URL) -> Self?](./wellknowntypeuripayload%28url%29.md)
  Creates a payload record with a URI specified as a URL.
- [class func wellKnownTypeTextPayload(string: String, locale: Locale) -> Self?](./wellknowntypetextpayload%28string,locale%29.md)
  Creates a payload record with text.
- [init(format: NFCTypeNameFormat, type: Data, identifier: Data, payload: Data)](./init%28format,type,identifier,payload%29.md)
  Creates a payload record with the specified format, type, identifier, and payload data.
- [init(format: NFCTypeNameFormat, type: Data, identifier: Data, payload: Data, chunkSize: Int)](./init%28format,type,identifier,payload,chunksize%29.md)
  Creates a payload record with the specified format, type, identifier, payload data, and data chunk size.
- [class func wellKnowTypeTextPayload(string: String, locale: Locale) -> Self?](./wellknowtypetextpayload%28string,locale%29.md)
  Creates a payload record with text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefpayload/wellknowntypeuripayload(string:))*