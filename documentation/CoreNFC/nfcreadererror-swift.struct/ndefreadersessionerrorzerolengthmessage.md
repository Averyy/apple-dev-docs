# ndefReaderSessionErrorZeroLengthMessage

**Framework**: Core NFC  
**Kind**: property  
**Role**: Type Property

The NDEF tag doesn’t contain an NDEF message.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static var ndefReaderSessionErrorZeroLengthMessage: NFCReaderError.Code { get }
```

## See Also

### NDEF Tag Errors
- [static var ndefReaderSessionErrorTagNotWritable: NFCReaderError.Code](./ndefreadersessionerrortagnotwritable.md)
  The NDEF tag isn’t writable.
- [static var ndefReaderSessionErrorTagSizeTooSmall: NFCReaderError.Code](./ndefreadersessionerrortagsizetoosmall.md)
  The NDEF tag memory size is too small to store the data.
- [static var ndefReaderSessionErrorTagUpdateFailure: NFCReaderError.Code](./ndefreadersessionerrortagupdatefailure.md)
  The reader session failed to update the NDEF tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/ndefreadersessionerrorzerolengthmessage)*