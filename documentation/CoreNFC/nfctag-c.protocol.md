# NFCTag

**Framework**: Core NFC  
**Kind**: protocol  
**Role**: Protocol

An interface for interacting with an NFC or RFID tag.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```objc
@protocol NFCTag <NSObject, NSSecureCoding, NSCopying>
```

#### Overview

When an NFC reader session detects a tag, it returns an object that conforms to this protocol.

## Topics

### Getting Information About a Tag
- [available](./nfctag-c.protocol/available.md)
  A Boolean value that indicates whether a detected tag is available.
- [session](./nfctag-c.protocol/session.md)
  The reader session that provides the tag.
### Getting the Tag Type
- [type](./nfctag-c.protocol/type.md)
  The tag type.
- [- asNFCISO15693Tag](./nfctag-c.protocol/asnfciso15693tag.md)
  Returns the tag as an ISO 15693 tag object.
- [- asNFCISO7816Tag](./nfctag-c.protocol/asnfciso7816tag.md)
  Returns the tag as an ISO 7816 tag object.
- [- asNFCFeliCaTag](./nfctag-c.protocol/asnfcfelicatag.md)
  Returns the tag as a FeliCa tag object.
- [- asNFCMiFareTag](./nfctag-c.protocol/asnfcmifaretag.md)
  Returns the tag as a MIFARE tag object.
- [NFCTagType](./nfctagtype.md)
  Constants that identify the type of an NFC tag.

## Relationships

### Inherits From
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
- [protocol NFCNDEFTag](./nfcndeftag.md)
  An interface for interacting with an NDEF tag.
- [class NFCTagCommandConfiguration](./nfctagcommandconfiguration.md)
  A set of parameters you use to define the configuration of an NFC tag command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctag-c.protocol)*