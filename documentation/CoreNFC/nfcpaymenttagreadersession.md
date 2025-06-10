# NFCPaymentTagReaderSession

**Framework**: Core NFC  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
class NFCPaymentTagReaderSession
```

#### Overview

Reader session for processing NFC payment tags supporting the @link NFCTagTypeISO7816Compatible @link/ type. @link [NFCTagReaderSessionDelegate readerSession:didDetectTags:] @link/ will return a @link NFCISO7816Tag @link /. object. This session requires the “com.apple.developer.nfc.readersession.formats” entitlement in your process. In addition your application’s Info.plist must contain a non-empty usage description string.  @link NFCReaderErrorSecurityViolation @link/ will be returned from @link [NFCTagReaderSessionDelegate tagReaderSession:didInvalidateWithError:] @link/ if the required entitlement is missing when session is started.

```None
         When the reader discovers a compatible ISO7816 tag it automatically performs a SELECT command (by DF name) using the values provided in
         "com.apple.developer.nfc.readersession.iso7816.select-identifiers" in the specified array order.  The tag is
         returned from the [NFCTagReaderSessionDelegate readerSession:didDetectTags:] call on the first successful SELECT command.
         The initialSelectedAID property returns the application identifier of the selected application.  Tag will not be returned
         to the NFCTagReaderSessionDelegate if no application described in "com.apple.developer.nfc.readersession.iso7816.select-identifiers"
         is found.
```

NOTE:

- Only one NFCReaderSession can be active at any time in the system. Subsequent opened sessions will get queued up and processed by the system in FIFO order.

## Topics

### Initializers
- [convenience init(delegate: any NFCTagReaderSessionDelegate, queue: DispatchQueue?)](nfcpaymenttagreadersession/init(delegate:queue:).md)
  Creates a new NFCPaymentTagReaderSession instance for processing NFC payment tags supporting NFCTag.iso7816.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcpaymenttagreadersession)*