# url

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property

A merchant URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var url: URL? { get set }
```

```objc
@property (nonatomic, retain, nullable) NSURL * url;
```

#### Discussion

The maximum length of the URL is 64 characters, including the schema. To disable the merchant URL, set [`url`](./url.md) to `nil.`

## See Also

### Setting Configuration Items
- [var mode: NFCVASCommandConfiguration.Mode](./mode-swift.property.md)
  A VAS protocol mode.
- [typealias VASMode](../vasmode.md)
  Constants that indicate the VAS protocol mode.
- [var passTypeIdentifier: String](./passtypeidentifier.md)
  A type identifier for the Wallet Pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvascommandconfiguration/url)*