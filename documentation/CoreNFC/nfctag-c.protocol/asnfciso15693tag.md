# asNFCISO15693Tag

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

Returns the tag as an ISO 15693 tag object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```objc
- (id<NFCISO15693Tag>) asNFCISO15693Tag;
```

#### Return Value

The tag object, if it conforms to the [`NFCISO15693Tag`](../nfciso15693tag.md) protocol; otherwise, returns `nil`.

## See Also

### Getting the Tag Type
- [type](./type.md)
  The tag type.
- [- asNFCISO7816Tag](./asnfciso7816tag.md)
  Returns the tag as an ISO 7816 tag object.
- [- asNFCFeliCaTag](./asnfcfelicatag.md)
  Returns the tag as a FeliCa tag object.
- [- asNFCMiFareTag](./asnfcmifaretag.md)
  Returns the tag as a MIFARE tag object.
- [NFCTagType](../nfctagtype.md)
  Constants that identify the type of an NFC tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctag-c.protocol/asnfciso15693tag)*