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
- [init(vasMode: NFCVASCommandConfiguration.Mode, passTypeIdentifier: String, url: URL?)](nfcvascommandconfiguration/init(vasmode:passtypeidentifier:url:)-9bh8w.md)
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
### Initializers
- [init(VASMode: NFCVASCommandConfiguration.Mode, passTypeIdentifier: String, url: URL?)](nfcvascommandconfiguration/init(vasmode:passtypeidentifier:url:)-1dcy0.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [init(vasCommandConfigurations: [NFCVASCommandConfiguration], delegate: any NFCVASReaderSessionDelegate, queue: dispatch_queue_t?)](nfcvasreadersession/init(vascommandconfigurations:delegate:queue:)-23h52.md)
  Creates a VAS reader session.
- [protocol NFCVASReaderSessionDelegate](nfcvasreadersessiondelegate.md)
  A protocol that an object implements to receive callbacks from a VAS reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvascommandconfiguration)*