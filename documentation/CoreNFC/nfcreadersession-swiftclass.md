# NFCReaderSession

**Framework**: Core NFC  
**Kind**: class

The abstract base class that represents a reader session for detecting NFC tags.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class NFCReaderSession
```

#### Overview

You do not create instances of this class. Instead, you create and use an instance of [`NFCNDEFReaderSession`](nfcndefreadersession.md) or [`NFCTagReaderSession`](nfctagreadersession.md). Only one reader session of any type can be active in the system at a time. The system puts additional sessions in a queue and processes them in FIFO order.

## Topics

### Determining Tag Reading Capability
- [class var readingAvailable: Bool](nfcreadersession-swift.class/readingavailable.md)
  A Boolean value that determines whether the device supports NFC tag reading.
### Working with a Session
- [var delegate: AnyObject?](nfcreadersession-swift.class/delegate.md)
  The delegate of the reader session.
- [var sessionQueue: dispatch_queue_t](nfcreadersession-swift.class/sessionqueue.md)
  The queue on which the reader session delegate callbacks and completion block handlers are dispatched.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NFCNDEFReaderSession](nfcndefreadersession.md)
- [NFCTagReaderSession](nfctagreadersession.md)
- [NFCVASReaderSession](nfcvasreadersession.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NFCReaderSessionProtocol](nfcreadersessionprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NFCNDEFReaderSession](nfcndefreadersession.md)
  A reader session for detecting NFC Data Exchange Format (NDEF) tags.
- [class NFCTagReaderSession](nfctagreadersession.md)
  A reader session for detecting ISO7816, ISO15693, FeliCa, and MIFARE tags.
- [class NFCVASReaderSession](nfcvasreadersession.md)
  A reader session for processing Value Added Service (VAS) tags.
- [protocol NFCReaderSessionProtocol](nfcreadersessionprotocol.md)
  A general interface for interacting with a reader session.
- [Near Field Communication Tag Reader Session Formats Entitlement](../BundleResources/Entitlements/com.apple.developer.nfc.readersession.formats.md)
  The Near Field Communication data formats an app can read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadersession-swift.class)*