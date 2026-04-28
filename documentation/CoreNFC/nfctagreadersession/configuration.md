# NFCTagReaderSession.Configuration

**Framework**: Core NFC  
**Kind**: struct

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct Configuration
```

## Topics

### Initializers
- [init(pollingOption: NFCTagReaderSession.PollingOption, iso7816SelectIdentifiers: [String], feliCaSystemCodes: [String])](nfctagreadersession/configuration/init(pollingoption:iso7816selectidentifiers:felicasystemcodes:).md)
### Instance Properties
- [var feliCaSystemCodes: [String]](nfctagreadersession/configuration/felicasystemcodes.md)
  List of FeliCa System Codes to be used in tag detection when NFCTagReaderSession is configured with PollingOption.iso18092 option. Entries must be specified in “com.apple.developer.nfc.readersession.felica.systemcodes” in Info.plist; all unknown / not matched entries will be dropped. An empty array indicates all system codes specified in Info.plist will be used.  Subsequent duplicate elements will get dropped.
- [var iso7816SelectIdentifiers: [String]](nfctagreadersession/configuration/iso7816selectidentifiers.md)
  List of ISO7816 Application Identifiers to be used in tag detection when NFCTagReaderSession is configured with PollingOption.iso14443 and/or PollingOption.pace option. Entries must be specified in “com.apple.developer.nfc.readersession.iso7816.select-identifiers” in Info.plist; all unknown / not matched entries will be dropped. An empty array indicates all applications specified in Info.plist will be used.  Subsequent duplicate elements will get dropped.
- [var pollingOption: NFCTagReaderSession.PollingOption](nfctagreadersession/configuration/pollingoption.md)
  RF polling types to perform tag discovery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersession/configuration)*