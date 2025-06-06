# NFCNDEFReaderSessionDelegate

**Framework**: Core NFC  
**Kind**: protocol

A protocol that an object implements to serve as an NDEF reader session delegate.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol NFCNDEFReaderSessionDelegate : NSObjectProtocol
```

## Topics

### Handling Session Activation
- [func readerSessionDidBecomeActive(NFCNDEFReaderSession)](nfcndefreadersessiondelegate/readersessiondidbecomeactive(_:).md)
  Tells the delegate that the reader session is active.
### Finding NDEF Messages and Tags
- [func readerSession(NFCNDEFReaderSession, didDetectNDEFs: [NFCNDEFMessage])](nfcndefreadersessiondelegate/readersession(_:diddetectndefs:).md)
  Tells the delegate that the session detected NFC tags with NDEF messages.
- [func readerSession(NFCNDEFReaderSession, didDetect: [any NFCNDEFTag])](nfcndefreadersessiondelegate/readersession(_:diddetect:).md)
  Tells the delegate that the session detected NFC tags with NDEF messages and enables read-write capability for the session.
### Handling an Invalidated Session
- [func readerSession(NFCNDEFReaderSession, didInvalidateWithError: any Error)](nfcndefreadersessiondelegate/readersession(_:didinvalidatewitherror:).md)
  Tells the delegate the reason for invalidating a reader session.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [init(delegate: any NFCNDEFReaderSessionDelegate, queue: dispatch_queue_t?, invalidateAfterFirstRead: Bool)](nfcndefreadersession/init(delegate:queue:invalidateafterfirstread:).md)
  Creates and initializes a new NFC NDEF reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefreadersessiondelegate)*