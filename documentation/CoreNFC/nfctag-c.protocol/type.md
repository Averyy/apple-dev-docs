# type

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property

The tag type.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```objc
@property (nonatomic, assign, readonly) NFCTagType type;
```

#### Discussion

For a list of possible values, see [`NFCTagType`](../nfctagtype.md).

## See Also

### Getting the Tag Type
- [- asNFCISO15693Tag](./asnfciso15693tag.md)
  Returns the tag as an ISO 15693 tag object.
- [- asNFCISO7816Tag](./asnfciso7816tag.md)
  Returns the tag as an ISO 7816 tag object.
- [- asNFCFeliCaTag](./asnfcfelicatag.md)
  Returns the tag as a FeliCa tag object.
- [- asNFCMiFareTag](./asnfcmifaretag.md)
  Returns the tag as a MIFARE tag object.
- [NFCTagType](../nfctagtype.md)
  Constants that identify the type of an NFC tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctag-c.protocol/type)*