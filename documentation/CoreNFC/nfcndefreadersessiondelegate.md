# NFCNDEFReaderSessionDelegate

**Framework**: Core NFC  
**Kind**: protocol  
**Role**: Protocol

A protocol that an object implements to serve as an NDEF reader session delegate.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol NFCNDEFReaderSessionDelegate : NSObjectProtocol
```

```objc
@protocol NFCNDEFReaderSessionDelegate <NSObject>
```

## Topics

### Handling Session Activation
- [func readerSessionDidBecomeActive(NFCNDEFReaderSession)](./nfcndefreadersessiondelegate/readersessiondidbecomeactive%28_%29.md)
  Tells the delegate that the reader session is active.
### Finding NDEF Messages and Tags
- [func readerSession(NFCNDEFReaderSession, didDetectNDEFs: [NFCNDEFMessage])](./nfcndefreadersessiondelegate/readersession%28_,diddetectndefs%29.md)
  Tells the delegate that the session detected NFC tags with NDEF messages.
- [func readerSession(NFCNDEFReaderSession, didDetect: [any NFCNDEFTag])](./nfcndefreadersessiondelegate/readersession%28_,diddetect%29.md)
  Tells the delegate that the session detected NFC tags with NDEF messages and enables read-write capability for the session.
### Handling an Invalidated Session
- [func readerSession(NFCNDEFReaderSession, didInvalidateWithError: any Error)](./nfcndefreadersessiondelegate/readersession%28_,didinvalidatewitherror%29.md)
  Tells the delegate the reason for invalidating a reader session.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a Session
- [init(delegate: any NFCNDEFReaderSessionDelegate, queue: dispatch_queue_t?, invalidateAfterFirstRead: Bool)](./nfcndefreadersession/init%28delegate,queue,invalidateafterfirstread%29.md)
  Creates and initializes a new NFC NDEF reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefreadersessiondelegate)*