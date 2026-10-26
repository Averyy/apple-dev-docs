# NFCNDEFReaderSession

**Framework**: Core NFC  
**Kind**: class  
**Role**: Class

A reader session for detecting NFC Data Exchange Format (NDEF) tags.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class NFCNDEFReaderSession
```

```objc
@interface NFCNDEFReaderSession : NFCReaderSession
```

#### Overview

As with the [`NFCReaderSession`](./nfcreadersession-swift.class.md) base class, only one NFC NDEF reader session can be active in the system at a time. If you create an additional session, the system puts it in a queue and processes it in first-in, first-out (FIFO) order.

## Topics

### Creating a Session
- [init(delegate: any NFCNDEFReaderSessionDelegate, queue: dispatch_queue_t?, invalidateAfterFirstRead: Bool)](./nfcndefreadersession/init%28delegate,queue,invalidateafterfirstread%29.md)
  Creates and initializes a new NFC NDEF reader session.
- [protocol NFCNDEFReaderSessionDelegate](./nfcndefreadersessiondelegate.md)
  A protocol that an object implements to serve as an NDEF reader session delegate.
### Connecting to a Tag
- [func connect(to: any NFCNDEFTag, completionHandler: ((any Error)?) -> Void)](./nfcndefreadersession/connect%28to,completionhandler%29.md)
  Connects the reader session to a tag and activates that tag.
### Restarting the Polling Sequence
- [func restartPolling()](./nfcndefreadersession/restartpolling%28%29.md)
  Restarts the polling sequence so the reader session can discover new tags.

## Relationships

### Inherits From
- [NFCReaderSession](./nfcreadersession-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NFCReaderSessionProtocol](./nfcreadersessionprotocol.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Reader sessions
- [class NFCTagReaderSession](./nfctagreadersession.md)
  A reader session for detecting ISO7816, ISO15693, FeliCa, and MIFARE tags.
- [class NFCPaymentTagReaderSession](./nfcpaymenttagreadersession.md)
  A reader session that supports the use of payment tags.
- [class NFCVASReaderSession](./nfcvasreadersession.md)
  A reader session for processing Value Added Service (VAS) tags.
- [class NFCReaderSession](./nfcreadersession-swift.class.md)
  The abstract base class that represents a reader session for detecting NFC tags.
- [protocol NFCReaderSessionProtocol](./nfcreadersessionprotocol.md)
  A general interface for interacting with a reader session.
- [Near Field Communication Tag Reader Session Formats Entitlement](../BundleResources/entitlements/com.apple.developer.nfc.readersession.formats.md)
  The Near Field Communication data formats an app can read.
- [NFCReaderSessionDelegate](./nfcreadersessiondelegate.md)
  A collection of callbacks that provide information about the status of an NFC reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefreadersession)*