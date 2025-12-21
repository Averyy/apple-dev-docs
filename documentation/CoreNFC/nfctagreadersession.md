# NFCTagReaderSession

**Framework**: Core NFC  
**Kind**: class

A reader session for detecting ISO7816, ISO15693, FeliCa, and MIFARE tags.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class NFCTagReaderSession
```

#### Overview

Use NFCTagReaderSession to interact with one of the tag types listed in [`NFCTagType`](nfctagtype.md). To use this reader session, you must:

- Include the [`Near Field Communication Tag Reader Session Formats Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.nfc.readersession.formats) in your app.
- Provide a non-empty string for the [`NFCReaderUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NFCReaderUsageDescription) key in your app’s information property list file.

To interact with ISO 7816 tags, add the list of the application identifiers supported in your app to the [`ISO7816 application identifiers for NFC Tag Reader Session`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.nfc.readersession.iso7816.select-identifiers) information property list key. If you include the application identifier `D2760000850101`—the identifier for the NDEF application on MIFARE DESFire tags (NFC Forum T4T tag platform)—and the reader session finds a tag matching this identifier, it sends the delegate an [`NFCISO7816Tag`](nfciso7816tag.md) tag object. To get the MIFARE DESFire tag as an [`NFCMiFareTag`](nfcmifaretag.md) object, don’t include `D2760000850101` in the application identifier list.

Only one reader session of any type can be active in the system at a time. The system puts additional sessions in a queue and processes them in first-in, first-out (FIFO) order.

> ❗ **Important**:  `NFCTagReaderSession` doesn’t support selection of payment-related application IDs. In the European Union (EU), you can use [`NFCPaymentTagReaderSession`](nfcpaymenttagreadersession.md), as described in that class’s documentation.

## Topics

### Creating a Tag Reader Session
- [convenience init?(pollingOption: NFCTagReaderSession.PollingOption, delegate: any NFCTagReaderSessionDelegate, queue: DispatchQueue?)](nfctagreadersession/init(pollingoption:delegate:queue:).md)
  Creates an NFC tag reader session.
- [NFCTagReaderSession.PollingOption](nfctagreadersession/pollingoption.md)
  Options that determine the type of tags that a reader session should detect during a polling sequence.
- [protocol NFCTagReaderSessionDelegate](nfctagreadersessiondelegate-2joku.md)
  A protocol that an object implements to receive callbacks sent from an NFC tag reader session.
### Connecting to a Tag
- [func connect(to: NFCTag, completionHandler: ((any Error)?) -> Void)](nfctagreadersession/connect(to:completionhandler:).md)
  Connects the reader session to a tag and activates that tag.
- [var connectedTag: NFCTag?](nfctagreadersession/connectedtag-3mlqu.md)
  The tag connected to the reader session.
### Restarting the Polling Sequence
- [func restartPolling()](nfctagreadersession/restartpolling.md)
  Restarts the polling sequence so the reader session can discover new tags.
### Instance Methods
- [func connect(to: NFCTag) async throws](nfctagreadersession/connect(to:).md)

## Relationships

### Inherits From
- [NFCReaderSession](nfcreadersession-swift.class.md)
### Inherited By
- [NFCPaymentTagReaderSession](nfcpaymenttagreadersession.md)
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
- [class NFCPaymentTagReaderSession](nfcpaymenttagreadersession.md)
  A reader session that supports the use of payment tags.
- [class NFCVASReaderSession](nfcvasreadersession.md)
  A reader session for processing Value Added Service (VAS) tags.
- [class NFCReaderSession](nfcreadersession-swift.class.md)
  The abstract base class that represents a reader session for detecting NFC tags.
- [protocol NFCReaderSessionProtocol](nfcreadersessionprotocol.md)
  A general interface for interacting with a reader session.
- [Near Field Communication Tag Reader Session Formats Entitlement](../BundleResources/Entitlements/com.apple.developer.nfc.readersession.formats.md)
  The Near Field Communication data formats an app can read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersession)*