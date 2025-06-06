# ndefReaderSessionErrorTagUpdateFailure

**Framework**: Core NFC  
**Kind**: property

The reader session failed to update the NDEF tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static var ndefReaderSessionErrorTagUpdateFailure: NFCReaderError.Code { get }
```

## See Also

- [static var ndefReaderSessionErrorTagNotWritable: NFCReaderError.Code](nfcreadererror-swift.struct/ndefreadersessionerrortagnotwritable.md)
  The NDEF tag isn’t writable.
- [static var ndefReaderSessionErrorTagSizeTooSmall: NFCReaderError.Code](nfcreadererror-swift.struct/ndefreadersessionerrortagsizetoosmall.md)
  The NDEF tag memory size is too small to store the data.
- [static var ndefReaderSessionErrorZeroLengthMessage: NFCReaderError.Code](nfcreadererror-swift.struct/ndefreadersessionerrorzerolengthmessage.md)
  The NDEF tag doesn’t contain an NDEF message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/ndefreadersessionerrortagupdatefailure)*