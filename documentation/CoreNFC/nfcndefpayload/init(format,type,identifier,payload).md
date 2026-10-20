# init(format:type:identifier:payload:)

**Framework**: Core NFC  
**Kind**: init  
**Role**: Initializer

Creates a payload record with the specified format, type, identifier, and payload data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(format: NFCTypeNameFormat, type: Data, identifier: Data, payload: Data)
```

```objc
- (instancetype) initWithFormat:(NFCTypeNameFormat) format type:(NSData *) type identifier:(NSData *) identifier payload:(NSData *) payload;
```

#### Return Value

A newly initialized payload record object.

#### Discussion

This initializer uses the maximum payload chunk size defined by the NFC NDEF specification, which is 2^32-1 octets. If the payload size is bigger than the maximum size, the initializer splits the record into multiple record chunks.

## Parameters

- `format`: A NFC type name format value.
- `type`: A data object describing the type of payload. If the data is empty, the method excludes this field from the payload record.
- `identifier`: A URI reference that identifies the payload. If the data is empty, the method excludes this field from the payload record.
- `payload`: A data object containing the payload data. If the data is empty, the method excludes this field from the payload record.

## See Also

### Creating a Payload Record
- [class func wellKnownTypeURIPayload(url: URL) -> Self?](./wellknowntypeuripayload%28url%29.md)
  Creates a payload record with a URI specified as a URL.
- [class func wellKnownTypeURIPayload(string: String) -> Self?](./wellknowntypeuripayload%28string%29.md)
  Creates a payload record with a URI specified as a string.
- [class func wellKnownTypeTextPayload(string: String, locale: Locale) -> Self?](./wellknowntypetextpayload%28string,locale%29.md)
  Creates a payload record with text.
- [init(format: NFCTypeNameFormat, type: Data, identifier: Data, payload: Data, chunkSize: Int)](./init%28format,type,identifier,payload,chunksize%29.md)
  Creates a payload record with the specified format, type, identifier, payload data, and data chunk size.
- [class func wellKnowTypeTextPayload(string: String, locale: Locale) -> Self?](./wellknowtypetextpayload%28string,locale%29.md)
  Creates a payload record with text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefpayload/init(format:type:identifier:payload:))*