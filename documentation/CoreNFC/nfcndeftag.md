# NFCNDEFTag

**Framework**: Core NFC  
**Kind**: protocol  
**Role**: Protocol

An interface for interacting with an NDEF tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol NFCNDEFTag : NSCopying, NSSecureCoding, NSObjectProtocol
```

```objc
@protocol NFCNDEFTag <NSObject, NSSecureCoding, NSCopying>
```

## Topics

### Getting the Tag Status
- [var isAvailable: Bool](./nfcndeftag/isavailable.md)
  A Boolean value that determines whether the NDEF tag is available in the current reader session.
- [func queryNDEFStatus(completionHandler: (NFCNDEFStatus, Int, (any Error)?) -> Void)](./nfcndeftag/queryndefstatus%28completionhandler%29.md)
  Asks the reader session for the NDEF support status of the tag.
- [enum NFCNDEFStatus](./nfcndefstatus.md)
  Constants that indicate status for an NDEF tag.
### Reading the Tag
- [func readNDEF(completionHandler: (NFCNDEFMessage?, (any Error)?) -> Void)](./nfcndeftag/readndef%28completionhandler%29.md)
  Retrieves an NDEF message from the tag.
### Writing to the Tag
- [func writeNDEF(NFCNDEFMessage, completionHandler: ((any Error)?) -> Void)](./nfcndeftag/writendef%28_,completionhandler%29.md)
  Saves an NDEF message to a writable tag.
- [func writeLock(completionHandler: ((any Error)?) -> Void)](./nfcndeftag/writelock%28completionhandler%29.md)
  Changes the NDEF tag status to read-only, preventing future write operations.

## Relationships

### Inherits From
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
### Inherited By
- [NFCFeliCaTag](./nfcfelicatag.md)
- [NFCISO15693Tag](./nfciso15693tag.md)
- [NFCISO7816Tag](./nfciso7816tag.md)
- [NFCMiFareTag](./nfcmifaretag.md)

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
- [protocol NFCMiFareTag](./nfcmifaretag.md)
  An interface for interacting with a MIFARE® tag.
- [enum NFCTag](./nfctag-swift.enum.md)
  An object that represents an NFC tag object.
- [class NFCTagCommandConfiguration](./nfctagcommandconfiguration.md)
  A set of parameters you use to define the configuration of an NFC tag command.
- [NFCTag](./nfctag-c.protocol.md)
  An interface for interacting with an NFC or RFID tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndeftag)*