# init(delegate:queue:)

**Framework**: Core NFC  
**Kind**: init

Creates a new NFCPaymentTagReaderSession instance for processing NFC payment tags supporting NFCTag.iso7816.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
@nonobjc
convenience init(delegate: any NFCTagReaderSessionDelegate, queue: DispatchQueue? = nil)
```

#### Discussion

- Discussions: This session requires the “com.apple.developer.nfc.readersession.formats” entitlement in your process. In addition your application’s Info.plist must contain a non-empty usage description string.  `NFCReaderErrorSecurityViolation` will be returned from `NFCTagReaderSessionDelegate.tagReaderSession(_:didInvalidateWithError:)` if the required entitlement is missing when session is started. When the reader discovers a compatible ISO7816 tag it automatically performs a SELECT command (by DF name) using the values provided in “com.apple.developer.nfc.readersession.iso7816.select-identifiers” in the specified array order.  The tag is returned from the `NFCTagReaderSessionDelegate.tagReaderSession(_:didDetect:)` call on the first successful SELECT command. The `NFCISO7816Tag.initialSelectedAID` property returns the application identifier of the selected application.  Tag will not be returned to the `NFCTagReaderSessionDelegate` if no application described in “com.apple.developer.nfc.readersession.iso7816.select-identifiers” is found.

## Parameters

- `delegate`: The session will hold a weak ARC reference to this   object.
- `queue`: A dispatch queue where   delegate callbacks will be dispatched to.  A nil value will   cause the creation of a serial dispatch queue internally for the session.  The session object will retain the provided dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcpaymenttagreadersession/init(delegate:queue:))*