# readerSessionInvalidationErrorSessionTimeout

**Framework**: Core NFC  
**Kind**: property  
**Role**: Type Property

The reader session timed out.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static var readerSessionInvalidationErrorSessionTimeout: NFCReaderError.Code { get }
```

## See Also

### Session Errors
- [static var readerSessionInvalidationErrorFirstNDEFTagRead: NFCReaderError.Code](./readersessioninvalidationerrorfirstndeftagread.md)
  The first NDEF tag read by this session is invalid.
- [static var readerSessionInvalidationErrorSessionTerminatedUnexpectedly: NFCReaderError.Code](./readersessioninvalidationerrorsessionterminatedunexpectedly.md)
  The reader session terminated unexpectedly.
- [static var readerSessionInvalidationErrorSystemIsBusy: NFCReaderError.Code](./readersessioninvalidationerrorsystemisbusy.md)
  The reader session failed because the system is busy.
- [static var readerSessionInvalidationErrorUserCanceled: NFCReaderError.Code](./readersessioninvalidationerrorusercanceled.md)
  The user canceled the reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/readersessioninvalidationerrorsessiontimeout)*