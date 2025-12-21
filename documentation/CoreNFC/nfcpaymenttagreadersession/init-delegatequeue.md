# init(delegate:queue:)

**Framework**: Core NFC  
**Kind**: init

Creates a new session instance for processing NFC payment tags.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
@nonobjc
convenience init(delegate: any NFCTagReaderSessionDelegate, queue: DispatchQueue? = nil)
```

#### Discussion

Creating a session requires that your app have the [`Near Field Communication Tag Reader Session Formats Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.nfc.readersession.formats) entitlement; if it’s missing, your delegate receives the callback [`tagReaderSession(_:didInvalidateWithError:)`](nfctagreadersessiondelegate-2joku/tagreadersession(_:didinvalidatewitherror:).md) with the error [`NFCReaderError.Code.readerErrorSecurityViolation`](nfcreadererror-swift.struct/code/readererrorsecurityviolation.md). Additionally, the app’s information property list must contain a non-empty usage description string. If it’s absent, the delegate doesn’t receive tag-discovery callbacks.

When the session discovers an ISO 7816-compatible tag, the session performs a `SELECT` command for each application identifier provided in [`ISO7816 application identifiers for NFC Tag Reader Session`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.nfc.readersession.iso7816.select-identifiers). The `SELECT` command searches for the identifiers in the order in which they appear in the array. The session calls the [`tagReaderSession(_:didDetect:)`](nfctagreadersessiondelegate-2joku/tagreadersession(_:diddetect:).md) delegate method after the first successful `SELECT` command. The [`initialSelectedAID`](nfciso7816tag/initialselectedaid.md) property of the found tag contains the selected identifier.

## Parameters

- `delegate`: A delegate that receives callbacks about discovered tags and session life cycle events. The session holds a weak reference to the delegate.
- `queue`: A dispatch queue on which to perform delegate callbacks. The session object retains the provided dispatch queue. If this value is  , the framework creates an internal serial dispatch queue for the session.

## See Also

- [protocol NFCTagReaderSessionDelegate](nfctagreadersessiondelegate-2joku.md)
  A protocol that an object implements to receive callbacks sent from an NFC tag reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcpaymenttagreadersession/init(delegate:queue:))*