# readerSession:didDetectTags:

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

Provides an array of tags detected by the reader session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```objc
- (void) readerSession:(NFCReaderSession *) session didDetectTags:(NSArray<__kindof id<NFCTag>> *) tags;
```

## Discussion

This method is called when the reader session detects NFC tags in a polling sequence.

## Parameters

- `session`: The reader session detecting tags.
- `tags`: An array of [`NFCTag`](../nfctag-swift.enum.md) objects that were detected.

## See Also

### Getting the Status of a Reader Session
- [- readerSession:didInvalidateWithError:](./readersession_didinvalidatewitherror_.md)
  Provides information about the error that invalidated the reader session.
- [- readerSessionDidBecomeActive:](./readersessiondidbecomeactive_.md)
  Tells you when radio-frequency polling is enabled and the reader session has become active and is scanning for tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadersessiondelegate/readersession:diddetecttags:)*