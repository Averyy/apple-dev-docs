# NFCVASCommandConfiguration

**Framework**: Core NFC  
**Kind**: class

An object providing the configuration for a GET VAS DATA command.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class NFCVASCommandConfiguration
```

## Topics

### Creating a Command Configuration
- [init(vasMode: NFCVASCommandConfiguration.Mode, passTypeIdentifier: String, url: URL?)](nfcvascommandconfiguration/init(vasmode:passtypeidentifier:url:).md)
  Creates a VAS command configuration object.
### Setting Configuration Items
- [var mode: NFCVASCommandConfiguration.Mode](nfcvascommandconfiguration/mode-swift.property.md)
  A VAS protocol mode.
- [typealias VASMode](vasmode.md)
  Constants that indicate the VAS protocol mode.
- [var passTypeIdentifier: String](nfcvascommandconfiguration/passtypeidentifier.md)
  A type identifier for the Wallet Pass.
- [var url: URL?](nfcvascommandconfiguration/url.md)
  A merchant URL.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [init(vasCommandConfigurations: [NFCVASCommandConfiguration], delegate: any NFCVASReaderSessionDelegate, queue: dispatch_queue_t?)](nfcvasreadersession/init(vascommandconfigurations:delegate:queue:).md)
  Creates a VAS reader session.
- [protocol NFCVASReaderSessionDelegate](nfcvasreadersessiondelegate.md)
  A protocol that an object implements to receive callbacks from a VAS reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvascommandconfiguration)*