# initWithPollingOption:iso7816SelectIdentifiers:felicaSystemCodes:

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```objc
- (instancetype) initWithPollingOption:(NFCPollingOption) option iso7816SelectIdentifiers:(NSArray<NSString *> *) iso7816SelectIdentifiers felicaSystemCodes:(NSArray<NSString *> *) felicaSystemCodes;
```

## Parameters

- `option`: RF polling types to perform tag discovery.
- `iso7816SelectIdentifiers`: List of ISO7816 Application Identifiers to be used in tag detection when NFCTagReaderSession is configured with NFCPollingISO14443 and/or NFCPollingPACE option. Entries must be specified in “com.apple.developer.nfc.readersession.iso7816.select-identifiers” in Info.plist; all unknown / not matched entries will be dropped. An empty NSArray indicates all applications specified in Info.plist will be used.  Repeated entries will get filter out via NSOrderedSet conversion.
- `felicaSystemCodes`: List of FeliCa System Codes to be used in tag detection when NFCTagReaderSession is configured with NFCPollingISO18092 option. Entries must be specified in “com.apple.developer.nfc.readersession.felica.systemcodes” in Info.plist; all unknown / not matched entries will be dropped. An empty NSArray indicates all applications specified in Info.plist will be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersessionconfiguration/initwithpollingoption:iso7816selectidentifiers:felicasystemcodes:)*