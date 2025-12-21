# NFCPaymentTagReaderSession

**Framework**: Core NFC  
**Kind**: class

A reader session that supports the use of payment tags.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class NFCPaymentTagReaderSession
```

#### Overview

This subclass of [`NFCTagReaderSession`](nfctagreadersession.md) adds support for payment tags, when someone uses your app in certain regions. To support payment tags in your app, intialize this class with a [`NFCTagReaderSessionDelegate`](nfctagreadersessiondelegate-2joku.md). The delegate receives an object that conforms to the [`NFCISO7816Tag`](nfciso7816tag.md) protocol when the [`NFCTagReaderSession`](nfctagreadersession.md) detects an ISO 7816-compatible tag. For the delegate to receive the tag object, your app must include:

- The [`Near Field Communication Tag Reader Session Formats Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.nfc.readersession.formats)
- A list of supported application identifiers in the [`ISO7816 application identifiers for NFC Tag Reader Session`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.nfc.readersession.iso7816.select-identifiers) information property list key

When the session discovers an ISO 7816-compatible tag, the session performs a `SELECT` command for each application identifier provided in [`ISO7816 application identifiers for NFC Tag Reader Session`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.nfc.readersession.iso7816.select-identifiers). The `SELECT` command searches for the identifiers in the order in which they appear in the array. The session calls the [`tagReaderSession:didDetectTags:`](nfctagreadersessiondelegate-5gxiw/tagreadersession:diddetecttags:.md) delegate method after the first successful `SELECT` command. The [`initialSelectedAID`](nfciso7816tag/initialselectedaid.md) property of the found tag contains the selected identifier.

The tag must be available to the reader session, so it can read and write data to the tag. Use the [`isAvailable`](nfctag-swift.enum/isavailable.md) property to check the tag’s availability. To connect to an available tag, call the superclass’s [`connect(to:completionHandler:)`](nfctagreadersession/connect(to:completionhandler:).md) method.

The system only supports one active [`NFCReaderSession`](nfcreadersession-swift.class.md) at a time. The system queues and processes subsequently opened sessions in first-in-first-out order.

> ❗ **Important**: The system supports use of `NFCPaymentTagReaderSession` only within the European Union (EU). People using your app must have an account registered in the EU, and their device must be located within the EU. These registration and device location requirements also apply to developing and testing apps that use this API. If the device isn’t currently eligible to use `NFCPaymentTagReaderSession`, the `NFCPaymentTagReaderSession.readingAvailable` property is false.

## Topics

### Creating a tag reader session
- [convenience init(delegate: any NFCTagReaderSessionDelegate, queue: DispatchQueue?)](nfcpaymenttagreadersession/init(delegate:queue:).md)
  Creates a new session instance for processing NFC payment tags.
- [protocol NFCTagReaderSessionDelegate](nfctagreadersessiondelegate-2joku.md)
  A protocol that an object implements to receive callbacks sent from an NFC tag reader session.

## Relationships

### Inherits From
- [NFCTagReaderSession](nfctagreadersession.md)
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
- [class NFCReaderSession](nfcreadersession-swift.class.md)
  The abstract base class that represents a reader session for detecting NFC tags.
- [protocol NFCReaderSessionProtocol](nfcreadersessionprotocol.md)
  A general interface for interacting with a reader session.
- [Near Field Communication Tag Reader Session Formats Entitlement](../BundleResources/Entitlements/com.apple.developer.nfc.readersession.formats.md)
  The Near Field Communication data formats an app can read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcpaymenttagreadersession)*