# ndefReaderSessionErrorTagUpdateFailure

**Framework**: Core NFC  
**Kind**: property  
**Role**: Type Property

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

### NDEF Tag Errors
- [static var ndefReaderSessionErrorTagNotWritable: NFCReaderError.Code](./ndefreadersessionerrortagnotwritable.md)
  The NDEF tag isn’t writable.
- [static var ndefReaderSessionErrorTagSizeTooSmall: NFCReaderError.Code](./ndefreadersessionerrortagsizetoosmall.md)
  The NDEF tag memory size is too small to store the data.
- [static var ndefReaderSessionErrorZeroLengthMessage: NFCReaderError.Code](./ndefreadersessionerrorzerolengthmessage.md)
  The NDEF tag doesn’t contain an NDEF message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/ndefreadersessionerrortagupdatefailure)*