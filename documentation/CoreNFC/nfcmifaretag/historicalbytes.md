# historicalBytes

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The historical bytes extracted from an Answer To Select response.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var historicalBytes: Data? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSData * historicalBytes;
```

## See Also

### Getting Tag Information
- [var mifareFamily: NFCMiFareFamily](./mifarefamily.md)
  The MIFARE product family identifier for the tag.
- [enum NFCMiFareFamily](../nfcmifarefamily.md)
  Identifiers for the MIFARE product families.
- [var identifier: Data](./identifier.md)
  The unique hardware identifier of the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcmifaretag/historicalbytes)*