# passTypeIdentifier

**Framework**: Core NFC  
**Kind**: property

A type identifier for the Wallet Pass.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var passTypeIdentifier: String { get set }
```

#### Discussion

The reader session uses the string value to calculate the merchant ID value for the `GET VAS DATA` command.

## See Also

- [var mode: NFCVASCommandConfiguration.Mode](nfcvascommandconfiguration/mode-swift.property.md)
  A VAS protocol mode.
- [typealias VASMode](vasmode.md)
  Constants that indicate the VAS protocol mode.
- [var url: URL?](nfcvascommandconfiguration/url.md)
  A merchant URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvascommandconfiguration/passtypeidentifier)*