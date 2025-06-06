# NFCNDEFPayload

**Framework**: Core NFC  
**Kind**: class

A payload record in an NFC NDEF message.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class NFCNDEFPayload
```

## Mentions

- [Adding Support for Background Tag Reading](adding-support-for-background-tag-reading.md)

#### Overview

An NDEF message payload consists of the Type Name Format field (as defined by the NDEF specification), type, identifier, and data.

## Topics

### Creating a Payload Record
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
- [class func wellKnowTypeTextPayload(string: String, locale: Locale) -> Self?](nfcndefpayload/wellknowtypetextpayload(string:locale:).md)
  Creates a payload record with text.
### Getting Information About a Payload Record
- [var identifier: Data](nfcndefpayload/identifier.md)
  The identifier of the payload, as defined by the NDEF specification.
- [var payload: Data](nfcndefpayload/payload.md)
  The payload, as defined by the NDEF specification.
- [var type: Data](nfcndefpayload/type.md)
  The type of the payload, as defined by the NDEF specification.
- [var typeNameFormat: NFCTypeNameFormat](nfcndefpayload/typenameformat.md)
  The Type Name Format field of the payload, as defined by the NDEF specification.
- [enum NFCTypeNameFormat](nfctypenameformat.md)
  The Type Name Format values that specify the content type for the payload data in an NFC NDEF message.
### Getting the URI from a Payload Record
- [func wellKnownTypeURIPayload() -> URL?](nfcndefpayload/wellknowntypeuripayload.md)
  Returns the URL of a valid Well Known Type URI payload.
### Getting Text from a Payload Record
- [func wellKnownTypeTextPayload() -> (String?, Locale?)](nfcndefpayload/wellknowntypetextpayload.md)
  Returns the text and locale of a valid Well Known Type Text payload.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NFCNDEFMessage](nfcndefmessage.md)
  An NFC NDEF message consisting of an array of payload records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefpayload)*