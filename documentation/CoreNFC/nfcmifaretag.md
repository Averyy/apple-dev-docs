# NFCMiFareTag

**Framework**: Core NFC  
**Kind**: protocol  
**Role**: Protocol

An interface for interacting with a MIFARE® tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol NFCMiFareTag : NFCNDEFTag, __NFCTag
```

```objc
@protocol NFCMiFareTag <NFCTag, NFCNDEFTag>
```

#### Overview

The [`NFCTagReaderSessionDelegate`](./nfctagreadersessiondelegate-2joku.md) receives an object that conforms to the [`NFCMiFareTag`](./nfcmifaretag.md) protocol when the [`NFCTagReaderSession`](./nfctagreadersession.md) detects a compatible tag. However, if you include the application identifier `D2760000850101`—the identifier for the NDEF application on MIFARE® DESFire® tags (NFC Forum T4T tag platform)—in the [`ISO7816 application identifiers for NFC Tag Reader Session`](../BundleResources/entitlements/com.apple.developer.nfc.readersession.iso7816.select-identifiers.md) array of your `Info.plist` file, the reader session sends the delegate an [`NFCISO7816Tag`](./nfciso7816tag.md) object when it finds a tag matching the identifier. To receive the MIFARE DESFire tag as an [`NFCMiFareTag`](./nfcmifaretag.md) object, don’t include `D2760000850101` in the array.

For the delegate to receive the tag object, your app must include the [`Near Field Communication Tag Reader Session Formats Entitlement`](../BundleResources/entitlements/com.apple.developer.nfc.readersession.formats.md).

For the reader session to read and write data to the tag, it must be available to the reader session. Use the [`isAvailable`](./nfctag-swift.enum/isavailable.md) property to check the tag’s availability.

MIFARE, MIFARE DESFire, MIFARE Ultralight, and MIFARE Plus are registered trademarks of NXP B.V.

## Topics

### Getting Tag Information
- [var mifareFamily: NFCMiFareFamily](./nfcmifaretag/mifarefamily.md)
  The MIFARE product family identifier for the tag.
- [enum NFCMiFareFamily](./nfcmifarefamily.md)
  Identifiers for the MIFARE product families.
- [var identifier: Data](./nfcmifaretag/identifier.md)
  The unique hardware identifier of the tag.
- [var historicalBytes: Data?](./nfcmifaretag/historicalbytes.md)
  The historical bytes extracted from an Answer To Select response.
### Sending Commands
- [func sendMiFareCommand(commandPacket: Data, completionHandler: (Data, (any Error)?) -> Void)](./nfcmifaretag/sendmifarecommand%28commandpacket,completionhandler%29.md)
  Sends a native MIFARE command to the tag.
- [func sendMiFareISO7816Command(NFCISO7816APDU, completionHandler: (Data, UInt8, UInt8, (any Error)?) -> Void)](./nfcmifaretag/sendmifareiso7816command%28_,completionhandler%29.md)
  Sends an ISO 7816 command APDU to the tag and receives a response APDU.
### Instance Methods
- [func sendMiFareCommand(commandPacket: Data, resultHandler: (Result<Data, any Error>) -> Void)](./nfcmifaretag/sendmifarecommand%28commandpacket,resulthandler%29.md)
- [func sendMiFareISO7816Command(NFCISO7816APDU, resultHandler: (Result<NFCISO7816ResponseAPDU, any Error>) -> Void)](./nfcmifaretag/sendmifareiso7816command%28_,resulthandler%29.md)

## Relationships

### Inherits From
- [NFCNDEFTag](./nfcndeftag.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [NFCTag](./nfctag-c.protocol.md)

## See Also

### Tag types
- [Creating NFC Tags from Your iPhone](./creating-nfc-tags-from-your-iphone.md)
  Save data to tags, and interact with them using native tag protocols.
- [protocol NFCISO7816Tag](./nfciso7816tag.md)
  An interface for interacting with an ISO 7816 tag.
- [protocol NFCISO15693Tag](./nfciso15693tag.md)
  An interface for interacting with an ISO 15693 tag.
- [protocol NFCFeliCaTag](./nfcfelicatag.md)
  An interface for interacting with a FeliCa™ tag.
- [protocol NFCNDEFTag](./nfcndeftag.md)
  An interface for interacting with an NDEF tag.
- [enum NFCTag](./nfctag-swift.enum.md)
  An object that represents an NFC tag object.
- [class NFCTagCommandConfiguration](./nfctagcommandconfiguration.md)
  A set of parameters you use to define the configuration of an NFC tag command.
- [NFCTag](./nfctag-c.protocol.md)
  An interface for interacting with an NFC or RFID tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcmifaretag)*