# NFCTagReaderSessionConfiguration

**Framework**: Core NFC  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```objc
@interface NFCTagReaderSessionConfiguration : NSObject
```

## Topics

### Instance Properties
- [felicaSystemCodes](./nfctagreadersessionconfiguration/felicasystemcodes.md)
  System codes (subset of entries defined in “com.apple.developer.nfc.readersession.felica.systemcodes”) used during FeliCa tag discovery.
- [iso7816SelectIdentifiers](./nfctagreadersessionconfiguration/iso7816selectidentifiers.md)
  Application identifiers (subset of entries defined in “com.apple.developer.nfc.readersession.iso7816.select-identifiers”) used during ISO7816 tag discovery.
- [polling](./nfctagreadersessionconfiguration/polling.md)
  Configures the RF polling of the reader session; multiple options can be OR’ed together.  This option affects the possible NFC tag type discover.
### Instance Methods
- [- initWithPollingOption:iso7816SelectIdentifiers:felicaSystemCodes:](./nfctagreadersessionconfiguration/initwithpollingoption_iso7816selectidentifiers_felicasystemcodes_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersessionconfiguration)*