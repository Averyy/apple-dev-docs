# NFCMiFareFamily

**Framework**: Core NFC  
**Kind**: enum

Identifiers for the MIFARE product families.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum NFCMiFareFamily
```

## Topics

### Product Families
- [NFCMiFareFamily.unknown](nfcmifarefamily/unknown.md)
  An identifier that indicates a compatible ISO14443 Type A tag.
- [NFCMiFareFamily.ultralight](nfcmifarefamily/ultralight.md)
  An identifier that indicates the MIFARE Ultralight® product family.
- [NFCMiFareFamily.plus](nfcmifarefamily/plus.md)
  An identifier that indicates the MIFARE Plus® product family.
- [NFCMiFareFamily.desfire](nfcmifarefamily/desfire.md)
  An identifier that indicates the MIFARE® DESFire® product family.
### Initializers
- [init?(rawValue: UInt)](nfcmifarefamily/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var mifareFamily: NFCMiFareFamily](nfcmifaretag/mifarefamily.md)
  The MIFARE product family identifier for the tag.
- [var identifier: Data](nfcmifaretag/identifier.md)
  The unique hardware identifier of the tag.
- [var historicalBytes: Data?](nfcmifaretag/historicalbytes.md)
  The historical bytes extracted from an Answer To Select response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcmifarefamily)*