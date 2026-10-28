# readerSession:didInvalidateWithError:

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

Provides information about the error that invalidated the reader session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```objc
- (void) readerSession:(NFCReaderSession *) session didInvalidateWithError:(NSError *) error;
```

## Discussion

This method is called when the reader session becomes invalid, at which time the client should discard the returned reader session object.

## Parameters

- `session`: The reader session that is invalid.
- `error`: A value that indicates the reason for invalidation.

## See Also

### Getting the Status of a Reader Session
- [- readerSession:didDetectTags:](./readersession_diddetecttags_.md)
  Provides an array of tags detected by the reader session.
- [- readerSessionDidBecomeActive:](./readersessiondidbecomeactive_.md)
  Tells you when radio-frequency polling is enabled and the reader session has become active and is scanning for tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadersessiondelegate/readersession:didinvalidatewitherror:)*