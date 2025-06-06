# readerTransceiveErrorPacketTooLong

**Framework**: Core NFC  
**Kind**: property

The packet length exceeds the limit supported by the tag.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static var readerTransceiveErrorPacketTooLong: NFCReaderError.Code { get }
```

## See Also

- [static var readerTransceiveErrorRetryExceeded: NFCReaderError.Code](nfcreadererror-swift.struct/readertransceiveerrorretryexceeded.md)
  Too many retries have occurred.
- [static var readerTransceiveErrorTagConnectionLost: NFCReaderError.Code](nfcreadererror-swift.struct/readertransceiveerrortagconnectionlost.md)
  The reader lost the connection to the tag.
- [static var readerTransceiveErrorTagNotConnected: NFCReaderError.Code](nfcreadererror-swift.struct/readertransceiveerrortagnotconnected.md)
  The tag isn’t in the connected state.
- [static var readerTransceiveErrorTagResponseError: NFCReaderError.Code](nfcreadererror-swift.struct/readertransceiveerrortagresponseerror.md)
  The tag has responded with an error.
- [static var readerTransceiveErrorSessionInvalidated: NFCReaderError.Code](nfcreadererror-swift.struct/readertransceiveerrorsessioninvalidated.md)
  The reader session is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/readertransceiveerrorpackettoolong)*