# NFCTagType

**Framework**: Core NFC  
**Kind**: enum  
**Role**: Enumeration

Constants that identify the type of an NFC tag.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst

## Declaration

```c
enum NFCTagType : NSUInteger;
```

## Topics

### Types
- [NFCTagTypeISO15693](./nfctagtype/nfctagtypeiso15693.md)
  An NFC tag of type ISO 15693.
- [NFCTagTypeISO7816Compatible](./nfctagtype/nfctagtypeiso7816compatible.md)
  An NFC tag of type ISO 7816.
- [NFCTagTypeFeliCa](./nfctagtype/nfctagtypefelica.md)
  An NFC tag of type FeliCa.
- [NFCTagTypeMiFare](./nfctagtype/nfctagtypemifare.md)
  An NFC tag of type MIFARE.

## See Also

### Getting the Tag Type
- [type](./nfctag-c.protocol/type.md)
  The tag type.
- [- asNFCISO15693Tag](./nfctag-c.protocol/asnfciso15693tag.md)
  Returns the tag as an ISO 15693 tag object.
- [- asNFCISO7816Tag](./nfctag-c.protocol/asnfciso7816tag.md)
  Returns the tag as an ISO 7816 tag object.
- [- asNFCFeliCaTag](./nfctag-c.protocol/asnfcfelicatag.md)
  Returns the tag as a FeliCa tag object.
- [- asNFCMiFareTag](./nfctag-c.protocol/asnfcmifaretag.md)
  Returns the tag as a MIFARE tag object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagtype)*