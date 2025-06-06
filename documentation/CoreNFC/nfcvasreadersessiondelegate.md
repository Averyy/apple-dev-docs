# NFCVASReaderSessionDelegate

**Framework**: Core NFC  
**Kind**: protocol

A protocol that an object implements to receive callbacks from a VAS reader session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol NFCVASReaderSessionDelegate : NSObjectProtocol
```

## Topics

### Handling Session Activation
- [func readerSessionDidBecomeActive(NFCVASReaderSession)](nfcvasreadersessiondelegate/readersessiondidbecomeactive(_:).md)
  Tells the delegate that the reader session is active.
### Receiving VAS Responses
- [func readerSession(NFCVASReaderSession, didReceive: [NFCVASResponse])](nfcvasreadersessiondelegate/readersession(_:didreceive:).md)
  Tells the delegate that the reader session received a VAS response.
- [class NFCVASResponse](nfcvasresponse.md)
  An object representing the response from a single `GET VAS DATA` command.
### Handling an Invalidated Session
- [func readerSession(NFCVASReaderSession, didInvalidateWithError: any Error)](nfcvasreadersessiondelegate/readersession(_:didinvalidatewitherror:).md)
  Tells the delegate that the session become invalid and provides the reason.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [init(vasCommandConfigurations: [NFCVASCommandConfiguration], delegate: any NFCVASReaderSessionDelegate, queue: dispatch_queue_t?)](nfcvasreadersession/init(vascommandconfigurations:delegate:queue:).md)
  Creates a VAS reader session.
- [class NFCVASCommandConfiguration](nfcvascommandconfiguration.md)
  An object providing the configuration for a GET VAS DATA command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvasreadersessiondelegate)*