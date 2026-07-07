# iso7816SelectIdentifiers

**Framework**: Core NFC  
**Kind**: property

List of ISO7816 Application Identifiers to be used in tag detection when NFCTagReaderSession is configured with PollingOption.iso14443 and/or PollingOption.pace option. Entries must be specified in “com.apple.developer.nfc.readersession.iso7816.select-identifiers” in Info.plist; all unknown / not matched entries will be dropped. An empty array indicates all applications specified in Info.plist will be used.  Subsequent duplicate elements will get dropped.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var iso7816SelectIdentifiers: [String]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersession/configuration/iso7816selectidentifiers)*