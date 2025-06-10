# NFCVASReaderSession

**Framework**: Core NFC  
**Kind**: class

A reader session for processing Value Added Service (VAS) tags.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class NFCVASReaderSession
```

#### Overview

> **Note**:  Using NFCVASReaderSession requires an entitlement from Apple. Updates will include information about the entitlement and a link to the entitlement request form.

## Topics

### Creating a VAS Reader Session
- [init(vasCommandConfigurations: [NFCVASCommandConfiguration], delegate: any NFCVASReaderSessionDelegate, queue: dispatch_queue_t?)](nfcvasreadersession/init(vascommandconfigurations:delegate:queue:).md)
  Creates a VAS reader session.
- [class NFCVASCommandConfiguration](nfcvascommandconfiguration.md)
  An object providing the configuration for a GET VAS DATA command.
- [protocol NFCVASReaderSessionDelegate](nfcvasreadersessiondelegate.md)
  A protocol that an object implements to receive callbacks from a VAS reader session.

## Relationships

### Inherits From
- [NFCReaderSession](nfcreadersession-swift.class.md)
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
- [class NFCReaderSession](nfcreadersession-swift.class.md)
  The abstract base class that represents a reader session for detecting NFC tags.
- [protocol NFCReaderSessionProtocol](nfcreadersessionprotocol.md)
  A general interface for interacting with a reader session.
- [class NFCReaderSession](nfcreadersession-swift.class.md)
  The abstract base class that represents a reader session for detecting NFC tags.
- [Near Field Communication Tag Reader Session Formats Entitlement](../BundleResources/Entitlements/com.apple.developer.nfc.readersession.formats.md)
  The Near Field Communication data formats an app can read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvasreadersession)*