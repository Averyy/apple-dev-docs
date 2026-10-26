# initWithPollingOption:delegate:queue:

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

Intializes an NFC tag reader session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```objc
- (instancetype) initWithPollingOption:(NFCPollingOption) pollingOption delegate:(id<NFCTagReaderSessionDelegate>) delegate queue:(dispatch_queue_t) queue;
```

#### Return Value

A newly initialized NFC tag reader session.

## Parameters

- `pollingOption`: One or more options specifying the type of tags that the reader session scans for and detects.
- `delegate`: An object that handles callbacks from the reader session.
- `queue`: A dispatch queue that the reader session uses when making callbacks to the delegate. When `queue` is `nil`, the session creates and uses a serial dispatch queue.

## See Also

### Creating a Tag Reader Session
- [NFCTagReaderSession.PollingOption](./pollingoption.md)
  Options that determine the type of tags that a reader session should detect during a polling sequence.
- [NFCTagReaderSessionDelegate](../nfctagreadersessiondelegate-5gxiw.md)
  A protocol that an object implements to receive callbacks sent from an NFC tag reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersession/initwithpollingoption:delegate:queue:)*