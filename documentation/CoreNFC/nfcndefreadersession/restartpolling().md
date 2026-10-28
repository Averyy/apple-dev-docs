# restartPolling()

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

Restarts the polling sequence so the reader session can discover new tags.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func restartPolling()
```

```objc
- (void) restartPolling;
```

## Discussion

After restarting the polling sequence, the reader session sends newly detected tags to the session’s delegate method [`readerSession(_:didDetect:)`](../nfcndefreadersessiondelegate/readersession%28_,diddetect%29.md).

> **Note**:  Tags detected before polling restarts are invalid. Your app should discard any references it has to the invalid tags to free system resources.

Calling [`restartPolling()`](./restartpolling%28%29.md) has no effect when:

- The session is invalid. If you need to restart the reader session, create a new [`NFCNDEFReaderSession`](../nfcndefreadersession.md).
- The session’s delegate doesn’t implement the [`readerSession(_:didDetect:)`](../nfcndefreadersessiondelegate/readersession%28_,diddetect%29.md) method. When this method is missing, the session calls [`readerSession(_:didDetectNDEFs:)`](../nfcndefreadersessiondelegate/readersession%28_,diddetectndefs%29.md) to inform the delegate of new NDEF messages, then restarts the polling sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefreadersession/restartpolling())*