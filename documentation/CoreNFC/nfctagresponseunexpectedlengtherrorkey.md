# NFCTagResponseUnexpectedLengthErrorKey

**Framework**: Core NFC  
**Kind**: var

A user-information dictionary key that indicates an invalid received response packet length.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
let NFCTagResponseUnexpectedLengthErrorKey: String
```

#### Discussion

If an error object’s [`userInfo`](https://developer.apple.com/documentation/Foundation/NSError/userInfo) dictionary contains this key, the received response packet length is invalid.

## See Also

- [NFCReaderError.Code](nfcreadererror-swift.struct/code.md)
  Reader session and tag error codes.
- [struct NFCReaderError](nfcreadererror-swift.struct.md)
  An error type that indicates problems with reader sessions or tags.
- [let NFCErrorDomain: String](nfcerrordomain.md)
  The domain for errors associated with Core NFC APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagresponseunexpectedlengtherrorkey)*