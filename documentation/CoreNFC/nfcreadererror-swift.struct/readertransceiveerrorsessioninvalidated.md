# readerTransceiveErrorSessionInvalidated

**Framework**: Core NFC  
**Kind**: property

The reader session is invalid.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static var readerTransceiveErrorSessionInvalidated: NFCReaderError.Code { get }
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
- [static var readerTransceiveErrorPacketTooLong: NFCReaderError.Code](nfcreadererror-swift.struct/readertransceiveerrorpackettoolong.md)
  The packet length exceeds the limit supported by the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/readertransceiveerrorsessioninvalidated)*