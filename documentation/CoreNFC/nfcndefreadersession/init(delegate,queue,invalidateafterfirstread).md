# init(delegate:queue:invalidateAfterFirstRead:)

**Framework**: Core NFC  
**Kind**: init  
**Role**: Initializer

Creates and initializes a new NFC NDEF reader session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(delegate: any NFCNDEFReaderSessionDelegate, queue: dispatch_queue_t?, invalidateAfterFirstRead: Bool)
```

```objc
- (instancetype) initWithDelegate:(id<NFCNDEFReaderSessionDelegate>) delegate queue:(dispatch_queue_t) queue invalidateAfterFirstRead:(BOOL) invalidateAfterFirstRead;
```

#### Discussion

When `invalidateAfterFirstRead` is [`false`](../../Swift/false.md), the reader session can read multiple NFC tags. For each successful read, the delegate’s [`readerSession(_:didDetectNDEFs:)`](../nfcndefreadersessiondelegate/readersession%28_,diddetectndefs%29.md) method delivers the message. A reader session that can read multiple tags terminates when the session times out or when the session is canceled by the client app (by calling [`invalidate()`](../nfcreadersessionprotocol/invalidate%28%29.md)) or the user (via the user interface).

> **Note**:  When creating the reader session that your app uses to write an NDEF message to a tag, set `invalidateAfterFirstRead` to [`false`](../../Swift/false.md). This keeps the session active so that your app can write a message to the tag.

When `invalidateAfterFirstRead` is [`true`](../../Swift/true.md), the reader session automatically terminates after the first NFC tag is successfully read. In this scenario, the delegate receives the [`NFCReaderError.Code.readerSessionInvalidationErrorFirstNDEFTagRead`](../nfcreadererror-swift.struct/code/readersessioninvalidationerrorfirstndeftagread.md) status in [`readerSession(_:didInvalidateWithError:)`](../nfcndefreadersessiondelegate/readersession%28_,didinvalidatewitherror%29.md).

## Parameters

- `delegate`: The NFC NDEF delegate that handles reader session callbacks.
- `queue`: A queue onto which delegate callbacks are dispatched (the session retains the queue). When `queue` is `nil`, an internal serial dispatch queue is created for the session.
- `invalidateAfterFirstRead`: A Boolean value that indicates whether the session automatically invalidates after the first NDEF tag is successfully read.

## See Also

### Creating a Session
- [protocol NFCNDEFReaderSessionDelegate](../nfcndefreadersessiondelegate.md)
  A protocol that an object implements to serve as an NDEF reader session delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefreadersession/init(delegate:queue:invalidateafterfirstread:))*