# readerSessionDidBecomeActive:

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

Tells you when radio-frequency polling is enabled and the reader session has become active and is scanning for tags.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```objc
- (void) readerSessionDidBecomeActive:(NFCReaderSession *) session;
```

## Parameters

- `session`: The reader session that is active.

## See Also

### Getting the Status of a Reader Session
- [- readerSession:didDetectTags:](./readersession_diddetecttags_.md)
  Provides an array of tags detected by the reader session.
- [- readerSession:didInvalidateWithError:](./readersession_didinvalidatewitherror_.md)
  Provides information about the error that invalidated the reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadersessiondelegate/readersessiondidbecomeactive:)*