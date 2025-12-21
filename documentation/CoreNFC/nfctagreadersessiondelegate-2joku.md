# NFCTagReaderSessionDelegate

**Framework**: Core NFC  
**Kind**: protocol

A protocol that an object implements to receive callbacks sent from an NFC tag reader session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+

## Declaration

```swift
protocol NFCTagReaderSessionDelegate : NSObjectProtocol
```

## Topics

### Handling Session Activation
- [func tagReaderSessionDidBecomeActive(NFCTagReaderSession)](nfctagreadersessiondelegate-2joku/tagreadersessiondidbecomeactive(_:).md)
  Tells the delegate that the reader session is active.
### Finding NFC Tags
- [func tagReaderSession(NFCTagReaderSession, didDetect: [NFCTag])](nfctagreadersessiondelegate-2joku/tagreadersession(_:diddetect:).md)
  Tells the delegate that the session detected NFC tags.
### Handling an Invalidated Session
- [func tagReaderSession(NFCTagReaderSession, didInvalidateWithError: any Error)](nfctagreadersessiondelegate-2joku/tagreadersession(_:didinvalidatewitherror:).md)
  Tells the delegate the reason for invalidating a reader session.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init(delegate: any NFCTagReaderSessionDelegate, queue: DispatchQueue?)](nfcpaymenttagreadersession/init(delegate:queue:).md)
  Creates a new session instance for processing NFC payment tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersessiondelegate-2joku)*