# initWithDelegate:queue:

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+ - Deprecated in 17.0
- iPadOS 11.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0

## Declaration

```objc
- (instancetype) initWithDelegate:(id<NFCReaderSessionDelegate>) delegate queue:(dispatch_queue_t) queue;
```

#### Return Value

A new NFCISO15693ReaderSession instance.

## Parameters

- `delegate`: The session will hold a weak ARC reference to this @link NFCReaderSessionDelegate @link/ object.
- `queue`: A dispatch queue where NFCReaderSessionDelegate delegate callbacks will be dispatched to.  A nil value will cause the creation of a serial dispatch queue internally for the session.  The session object will retain the provided dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693readersession/initwithdelegate:queue:)*