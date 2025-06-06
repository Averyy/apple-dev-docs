# NFCTagCommandConfiguration

**Framework**: Core NFC  
**Kind**: class

A set of parameters you use to define the configuration of an NFC tag command.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class NFCTagCommandConfiguration
```

## Topics

### Configuring a Tag Command
- [var maximumRetries: Int](nfctagcommandconfiguration/maximumretries.md)
  The maximum number of retries.
- [var retryInterval: TimeInterval](nfctagcommandconfiguration/retryinterval.md)
  The time between retries, in seconds.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NFCISO15693CustomCommandConfiguration](nfciso15693customcommandconfiguration.md)
- [NFCISO15693ReadMultipleBlocksConfiguration](nfciso15693readmultipleblocksconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagcommandconfiguration)*