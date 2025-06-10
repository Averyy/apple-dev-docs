# NFCReaderSessionProtocol

**Framework**: Core NFC  
**Kind**: protocol

A general interface for interacting with a reader session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol NFCReaderSessionProtocol : NSObjectProtocol
```

## Topics

### Determining Reader Session Readiness
- [var isReady: Bool](nfcreadersessionprotocol/isready.md)
  A Boolean value that indicates whether the reader session is started and ready to use.
- [var isReady: Bool](nfcreadersessionprotocol/isready.md)
  A Boolean value that indicates whether the reader session is started and ready to use.
### Managing a Reader Session
- [func begin()](nfcreadersessionprotocol/begin.md)
  Starts the reader session.
- [func invalidate()](nfcreadersessionprotocol/invalidate.md)
  Closes the reader session, which prevents it from being reused.
- [func invalidate(errorMessage: String)](nfcreadersessionprotocol/invalidate(errormessage:).md)
  Closes the reader session and displays an error message to the user.
- [var alertMessage: String](nfcreadersessionprotocol/alertmessage.md)
  A custom description that helps users understand how they can use NFC reader mode in your app.
- [func begin()](nfcreadersessionprotocol/begin.md)
  Starts the reader session.
- [func invalidate()](nfcreadersessionprotocol/invalidate.md)
  Closes the reader session, which prevents it from being reused.
- [func invalidate(errorMessage: String)](nfcreadersessionprotocol/invalidate(errormessage:).md)
  Closes the reader session and displays an error message to the user.
- [var alertMessage: String](nfcreadersessionprotocol/alertmessage.md)
  A custom description that helps users understand how they can use NFC reader mode in your app.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NFCNDEFReaderSession](nfcndefreadersession.md)
- [NFCPaymentTagReaderSession](nfcpaymenttagreadersession.md)
- [NFCReaderSession](nfcreadersession-swift.class.md)
- [NFCTagReaderSession](nfctagreadersession.md)
- [NFCVASReaderSession](nfcvasreadersession.md)

## See Also

- [class NFCNDEFReaderSession](nfcndefreadersession.md)
  A reader session for detecting NFC Data Exchange Format (NDEF) tags.
- [class NFCTagReaderSession](nfctagreadersession.md)
  A reader session for detecting ISO7816, ISO15693, FeliCa, and MIFARE tags.
- [class NFCVASReaderSession](nfcvasreadersession.md)
  A reader session for processing Value Added Service (VAS) tags.
- [class NFCReaderSession](nfcreadersession-swift.class.md)
  The abstract base class that represents a reader session for detecting NFC tags.
- [class NFCReaderSession](nfcreadersession-swift.class.md)
  The abstract base class that represents a reader session for detecting NFC tags.
- [Near Field Communication Tag Reader Session Formats Entitlement](../BundleResources/Entitlements/com.apple.developer.nfc.readersession.formats.md)
  The Near Field Communication data formats an app can read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadersessionprotocol)*