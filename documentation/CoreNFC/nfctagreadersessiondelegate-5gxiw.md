# NFCTagReaderSessionDelegate

**Framework**: Core NFC  
**Kind**: protocol  
**Role**: Protocol

A protocol that an object implements to receive callbacks sent from an NFC tag reader session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```objc
@protocol NFCTagReaderSessionDelegate <NSObject>
```

## Topics

### Handling Session Activation
- [- tagReaderSessionDidBecomeActive:](./nfctagreadersessiondelegate-5gxiw/tagreadersessiondidbecomeactive_.md)
  Tells the delegate that the reader session is active.
### Finding NFC Tags
- [- tagReaderSession:didDetectTags:](./nfctagreadersessiondelegate-5gxiw/tagreadersession_diddetecttags_.md)
  Tells the delegate that the session detected NFC tags.
### Handling an Invalidated Session
- [- tagReaderSession:didInvalidateWithError:](./nfctagreadersessiondelegate-5gxiw/tagreadersession_didinvalidatewitherror_.md)
  Tells the delegate the reason for invalidating a reader session.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a tag reader session
- [- initWithDelegate:queue:](./nfcpaymenttagreadersession/initwithdelegate_queue_.md)
  Creates a new session instance for processing NFC payment tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersessiondelegate-5gxiw)*