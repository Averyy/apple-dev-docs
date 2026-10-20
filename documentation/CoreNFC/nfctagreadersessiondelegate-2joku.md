# NFCTagReaderSessionDelegate

**Framework**: Core NFC  
**Kind**: protocol  
**Role**: Protocol

A protocol that an object implements to receive callbacks sent from an NFC tag reader session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+

## Declaration

```swift
protocol NFCTagReaderSessionDelegate : NSObjectProtocol
```

## Topics

### Handling Session Activation
- [func tagReaderSessionDidBecomeActive(NFCTagReaderSession)](./nfctagreadersessiondelegate-2joku/tagreadersessiondidbecomeactive%28_%29.md)
  Tells the delegate that the reader session is active.
### Finding NFC Tags
- [func tagReaderSession(NFCTagReaderSession, didDetect: [NFCTag])](./nfctagreadersessiondelegate-2joku/tagreadersession%28_,diddetect%29.md)
  Tells the delegate that the session detected NFC tags.
### Handling an Invalidated Session
- [func tagReaderSession(NFCTagReaderSession, didInvalidateWithError: any Error)](./nfctagreadersessiondelegate-2joku/tagreadersession%28_,didinvalidatewitherror%29.md)
  Tells the delegate the reason for invalidating a reader session.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a tag reader session
- [convenience init(delegate: any NFCTagReaderSessionDelegate, queue: DispatchQueue?)](./nfcpaymenttagreadersession/init%28delegate,queue%29.md)
  Creates a new session instance for processing NFC payment tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersessiondelegate-2joku)*