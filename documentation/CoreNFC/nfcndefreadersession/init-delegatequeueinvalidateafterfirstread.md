# init(delegate:queue:invalidateAfterFirstRead:)

**Framework**: Core NFC  
**Kind**: init

Creates and initializes a new NFC NDEF reader session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(delegate: any NFCNDEFReaderSessionDelegate, queue: dispatch_queue_t?, invalidateAfterFirstRead: Bool)
```

#### Discussion

When `invalidateAfterFirstRead` is [`false`](https://developer.apple.com/documentation/swift/false), the reader session can read multiple NFC tags. For each successful read, the delegate’s [`readerSession(_:didDetectNDEFs:)`](nfcndefreadersessiondelegate/readersession(_:diddetectndefs:).md) method delivers the message. A reader session that can read multiple tags terminates when the session times out or when the session is canceled by the client app (by calling [`invalidate()`](nfcreadersessionprotocol/invalidate().md)) or the user (via the user interface).

> **Note**:  When creating the reader session that your app uses to write an NDEF message to a tag, set `invalidateAfterFirstRead` to [`false`](https://developer.apple.com/documentation/swift/false). This keeps the session active so that your app can write a message to the tag.

When `invalidateAfterFirstRead` is [`true`](https://developer.apple.com/documentation/swift/true), the reader session automatically terminates after the first NFC tag is successfully read. In this scenario, the delegate receives the [`NFCReaderError.Code.readerSessionInvalidationErrorFirstNDEFTagRead`](nfcreadererror-swift.struct/code/readersessioninvalidationerrorfirstndeftagread.md) status in [`readerSession(_:didInvalidateWithError:)`](nfcndefreadersessiondelegate/readersession(_:didinvalidatewitherror:).md).

## Parameters

- `delegate`: The NFC NDEF delegate that handles reader session callbacks.
- `queue`: A queue onto which delegate callbacks are dispatched (the session retains the queue). When   is  , an internal serial dispatch queue is created for the session.
- `invalidateAfterFirstRead`: A Boolean value that indicates whether the session automatically invalidates after the first NDEF tag is successfully read.

## See Also

- [protocol NFCNDEFReaderSessionDelegate](nfcndefreadersessiondelegate.md)
  A protocol that an object implements to serve as an NDEF reader session delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefreadersession/init(delegate:queue:invalidateafterfirstread:))*