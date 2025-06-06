# NFCISO7816Tag

**Framework**: Core NFC  
**Kind**: protocol

An interface for interacting with an ISO 7816 tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol NFCISO7816Tag : NFCNDEFTag, __NFCTag
```

#### Overview

The [`NFCTagReaderSessionDelegate`](nfctagreadersessiondelegate-2joku.md) receives an object that conforms to the [`NFCISO7816Tag`](nfciso7816tag.md) protocol when the [`NFCTagReaderSession`](nfctagreadersession.md) detects an ISO 7816-compatible tag. For the delegate to receive the tag object, your app must include:

- The [`Near Field Communication Tag Reader Session Formats Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.nfc.readersession.formats).
- A list of supported application identifiers in the [`com.apple.developer.nfc.readersession.iso7816.select-identifiers`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/com.apple.developer.nfc.readersession.iso7816.select-identifiers)_ _information property list key.

When the session discovers a compatible ISO 7816 tag, the session performs a `SELECT` command for each application identifier provided in [`com.apple.developer.nfc.readersession.iso7816.select-identifiers`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/com.apple.developer.nfc.readersession.iso7816.select-identifiers). The `SELECT` command searches for the identifiers in the order in which they appear in the array. The session calls the [`tagReaderSession:didDetectTags:`](nfctagreadersessiondelegate-5gxiw/tagreadersession:diddetecttags:.md) delegate method after the first successful `SELECT` command. The [`initialSelectedAID`](nfciso7816tag/initialselectedaid.md) property of the found tag contains the selected identifier.

For the reader session to read and write data to the tag, it must be available to the reader session. Use the [`isAvailable`](nfctag-swift.enum/isavailable.md) property to check the tag’s availability.

## Topics

### Specifying Application Identifiers
- [com.apple.developer.nfc.readersession.iso7816.select-identifiers](../BundleResources/Information-Property-List/com.apple.developer.nfc.readersession.iso7816.select-identifiers.md)
  A list of application identifiers that the app supports.
### Getting Tag Information
- [var initialSelectedAID: String](nfciso7816tag/initialselectedaid.md)
  A hexadecimal string of the application identifier for the tag selected by the reader session when discovering new tags.
- [var identifier: Data](nfciso7816tag/identifier.md)
  The unique hardware identifier of the tag.
- [var historicalBytes: Data?](nfciso7816tag/historicalbytes.md)
  The historical bytes extracted from the Type A Answer To Select response.
- [var applicationData: Data?](nfciso7816tag/applicationdata.md)
  The application data bytes extracted from the Type B Answer To Request response.
- [var proprietaryApplicationDataCoding: Bool](nfciso7816tag/proprietaryapplicationdatacoding.md)
  A Boolean value that indicates whether the application data follows proprietary data coding.
### Sending a Command
- [func sendCommand(apdu: NFCISO7816APDU, resultHandler: (Result<NFCISO7816ResponseAPDU, any Error>) -> Void)](nfciso7816tag/sendcommand(apdu:resulthandler:).md)
  Sends an application protocol data unit (APDU) to the tag and receives a response APDU.
- [func sendCommand(apdu: NFCISO7816APDU, completionHandler: (Data, UInt8, UInt8, (any Error)?) -> Void)](nfciso7816tag/sendcommand(apdu:completionhandler:).md)
  Sends an application protocol data unit (APDU) to the tag and receives a response APDU.
- [class NFCISO7816APDU](nfciso7816apdu.md)
  An object representing an ISO 7816 application protocol data unit (APDU).
- [struct NFCISO7816ResponseAPDU](nfciso7816responseapdu.md)
  An object containing the response from the tag.

## Relationships

### Inherits From
- [NFCNDEFTag](nfcndeftag.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Creating NFC Tags from Your iPhone](creating-nfc-tags-from-your-iphone.md)
  Save data to tags, and interact with them using native tag protocols.
- [protocol NFCISO15693Tag](nfciso15693tag.md)
  An interface for interacting with an ISO 15693 tag.
- [protocol NFCFeliCaTag](nfcfelicatag.md)
  An interface for interacting with a FeliCa™ tag.
- [protocol NFCMiFareTag](nfcmifaretag.md)
  An interface for interacting with a MIFARE® tag.
- [protocol NFCNDEFTag](nfcndeftag.md)
  An interface for interacting with an NDEF tag.
- [enum NFCTag](nfctag-swift.enum.md)
  An object that represents an NFC tag object.
- [class NFCTagCommandConfiguration](nfctagcommandconfiguration.md)
  A set of parameters you use to define the configuration of an NFC tag command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816tag)*