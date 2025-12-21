# Core NFC

**Framework**: Core NFC  
**Kind**: module

Detect NFC tags, read messages that contain NDEF data, and save data to writable tags.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

#### Overview

Your app can read tags to give users more information about their physical environment and the real-world objects in it. Using Core NFC, you can read Near Field Communication (NFC) tags of types 1 through 5 that contain data in the NFC Data Exchange Format (NDEF). For example, your app might give users information about products they find in a store or exhibits they visit in a museum.

Your app can also write data to tags, and interact with protocol-specific tags such as ISO 7816, ISO 15693, FeliCa™, and MIFARE® tags.

Core NFC isn’t available for use in app extensions, and it requires a device that supports Near Field Communication. To determine if support is available, check the [`readingAvailable`](nfcreadersession-swift.class/readingavailable.md) class property before starting a reader session.

## Topics

### Essentials
- [Building an NFC Tag-Reader App](building-an-nfc-tag-reader-app.md)
  Read NFC tags with NDEF messages in your app.
- [Adding Support for Background Tag Reading](adding-support-for-background-tag-reading.md)
  Allow users to scan NFC tags without an app using background tag reading.
- [NFCReaderUsageDescription](../BundleResources/Information-Property-List/NFCReaderUsageDescription.md)
  A message that tells people why the app is requesting access to the device’s NFC hardware.
### Reader sessions
- [class NFCNDEFReaderSession](nfcndefreadersession.md)
  A reader session for detecting NFC Data Exchange Format (NDEF) tags.
- [class NFCTagReaderSession](nfctagreadersession.md)
  A reader session for detecting ISO7816, ISO15693, FeliCa, and MIFARE tags.
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
### Tag types
- [Creating NFC Tags from Your iPhone](creating-nfc-tags-from-your-iphone.md)
  Save data to tags, and interact with them using native tag protocols.
- [protocol NFCISO7816Tag](nfciso7816tag.md)
  An interface for interacting with an ISO 7816 tag.
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
### NDEF messages and payloads
- [class NFCNDEFMessage](nfcndefmessage.md)
  An NFC NDEF message consisting of an array of payload records.
- [class NFCNDEFPayload](nfcndefpayload.md)
  A payload record in an NFC NDEF message.
### Card sessions
- [class CardSession](cardsession.md)
  An ISO 7816 card emulation session.
- [class NFCPresentmentIntentAssertion](nfcpresentmentintentassertion.md)
  An object that signals your app’s intention to make exclusive use of the device’s contactless features.
### NFC window scenes
- [protocol NFCWindowSceneDelegate](nfcwindowscenedelegate.md)
  A protocol to notify your app’s user interface about NFC-related events.
- [enum NFCWindowSceneEvent](nfcwindowsceneevent.md)
  An NFC-related event that your app uses to update its user interface.
### Errors
- [NFCReaderError.Code](nfcreadererror-swift.struct/code.md)
  Reader session and tag error codes.
- [struct NFCReaderError](nfcreadererror-swift.struct.md)
  An error type that indicates problems with reader sessions or tags.
- [let NFCErrorDomain: String](nfcerrordomain.md)
  The domain for errors associated with Core NFC APIs.
- [let NFCTagResponseUnexpectedLengthErrorKey: String](nfctagresponseunexpectedlengtherrorkey.md)
  A user-information dictionary key that indicates an invalid received response packet length.
### Reference
- [CoreNFC Enumerations](corenfc-enumerations.md)
### Classes
- [class NFCISO15693CustomCommandConfiguration](nfciso15693customcommandconfiguration.md)
- [class NFCISO15693ReadMultipleBlocksConfiguration](nfciso15693readmultipleblocksconfiguration.md)
### Structures
- [struct NFCFeliCaPollingResponse](nfcfelicapollingresponse.md)
- [struct NFCFeliCaRequestSpecificationVersionResponse](nfcfelicarequestspecificationversionresponse.md)
- [struct NFCFeliCaRequsetServiceV2Response](nfcfelicarequsetservicev2response.md)
- [struct NFCFeliCaStatusFlag](nfcfelicastatusflag.md)
- [struct NFCISO15693MultipleBlockSecurityStatus](nfciso15693multipleblocksecuritystatus.md)
- [struct NFCISO15693SystemInfo](nfciso15693systeminfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreNFC)*