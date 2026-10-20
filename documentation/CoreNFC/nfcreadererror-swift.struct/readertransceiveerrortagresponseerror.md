# readerTransceiveErrorTagResponseError

**Framework**: Core NFC  
**Kind**: property  
**Role**: Type Property

The tag has responded with an error.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static var readerTransceiveErrorTagResponseError: NFCReaderError.Code { get }
```

## See Also

### Transceive Errors
- [static var readerTransceiveErrorRetryExceeded: NFCReaderError.Code](./readertransceiveerrorretryexceeded.md)
  Too many retries have occurred.
- [static var readerTransceiveErrorTagConnectionLost: NFCReaderError.Code](./readertransceiveerrortagconnectionlost.md)
  The reader lost the connection to the tag.
- [static var readerTransceiveErrorTagNotConnected: NFCReaderError.Code](./readertransceiveerrortagnotconnected.md)
  The tag isn’t in the connected state.
- [static var readerTransceiveErrorSessionInvalidated: NFCReaderError.Code](./readertransceiveerrorsessioninvalidated.md)
  The reader session is invalid.
- [static var readerTransceiveErrorPacketTooLong: NFCReaderError.Code](./readertransceiveerrorpackettoolong.md)
  The packet length exceeds the limit supported by the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/readertransceiveerrortagresponseerror)*