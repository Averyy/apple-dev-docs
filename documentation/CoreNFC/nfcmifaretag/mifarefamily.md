# mifareFamily

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The MIFARE product family identifier for the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var mifareFamily: NFCMiFareFamily { get }
```

```objc
@property (nonatomic, assign, readonly) NFCMiFareFamily mifareFamily;
```

## See Also

### Getting Tag Information
- [enum NFCMiFareFamily](../nfcmifarefamily.md)
  Identifiers for the MIFARE product families.
- [var identifier: Data](./identifier.md)
  The unique hardware identifier of the tag.
- [var historicalBytes: Data?](./historicalbytes.md)
  The historical bytes extracted from an Answer To Select response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcmifaretag/mifarefamily)*