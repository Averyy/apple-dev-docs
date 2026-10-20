# readerTransceiveErrorPacketTooLong

**Framework**: Core NFC  
**Kind**: property  
**Role**: Type Property

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

### Transceive Errors
- [static var readerTransceiveErrorRetryExceeded: NFCReaderError.Code](./readertransceiveerrorretryexceeded.md)
  Too many retries have occurred.
- [static var readerTransceiveErrorTagConnectionLost: NFCReaderError.Code](./readertransceiveerrortagconnectionlost.md)
  The reader lost the connection to the tag.
- [static var readerTransceiveErrorTagNotConnected: NFCReaderError.Code](./readertransceiveerrortagnotconnected.md)
  The tag isn’t in the connected state.
- [static var readerTransceiveErrorTagResponseError: NFCReaderError.Code](./readertransceiveerrortagresponseerror.md)
  The tag has responded with an error.
- [static var readerTransceiveErrorSessionInvalidated: NFCReaderError.Code](./readertransceiveerrorsessioninvalidated.md)
  The reader session is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/readertransceiveerrorpackettoolong)*