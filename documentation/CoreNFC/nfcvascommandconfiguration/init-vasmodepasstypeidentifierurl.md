# init(vasMode:passTypeIdentifier:url:)

**Framework**: Core NFC  
**Kind**: init

Creates a VAS command configuration object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(vasMode mode: NFCVASCommandConfiguration.Mode, passTypeIdentifier: String, url: URL?)
```

#### Return Value

A newly initialized VAS command configuration object.

## Parameters

- `mode`: A VAS operation mode.
- `passTypeIdentifier`: A type identifier for the Wallet pass.
- `url`: A URL when   is  ; otherwise set to  . The maximum length of the URL is 64 characters, including the schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvascommandconfiguration/init(vasmode:passtypeidentifier:url:))*