# VASMode

**Framework**: Core NFC  
**Kind**: typealias  
**Role**: Type Alias

Constants that indicate the VAS protocol mode.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0 (renamed: NFCVASMode)
- iPadOS 13.0+ - Deprecated in 14.0 (renamed: NFCVASMode)
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: NFCVASMode)

## Declaration

```swift
typealias VASMode = NFCVASCommandConfiguration.Mode
```

```c
typedef NFCVASMode VASMode;
```

## Topics

### Modes
- [static var VASModeNormal: NFCVASCommandConfiguration.Mode](./nfcvascommandconfiguration/mode-swift.enum/vasmodenormal.md)
  A constant that indicates the Full VAS Protocol mode.

## See Also

### Setting Configuration Items
- [var mode: NFCVASCommandConfiguration.Mode](./nfcvascommandconfiguration/mode-swift.property.md)
  A VAS protocol mode.
- [var passTypeIdentifier: String](./nfcvascommandconfiguration/passtypeidentifier.md)
  A type identifier for the Wallet Pass.
- [var url: URL?](./nfcvascommandconfiguration/url.md)
  A merchant URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/vasmode)*