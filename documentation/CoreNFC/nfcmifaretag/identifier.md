# identifier

**Framework**: Core NFC  
**Kind**: property  
**Required**: Yes

The unique hardware identifier of the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var identifier: Data { get }
```

#### Discussion

The [`identifier`](nfcmifaretag/identifier.md) data is in big-endian byte order.

## See Also

- [var mifareFamily: NFCMiFareFamily](nfcmifaretag/mifarefamily.md)
  The MIFARE product family identifier for the tag.
- [enum NFCMiFareFamily](nfcmifarefamily.md)
  Identifiers for the MIFARE product families.
- [var historicalBytes: Data?](nfcmifaretag/historicalbytes.md)
  The historical bytes extracted from an Answer To Select response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcmifaretag/identifier)*