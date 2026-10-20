# currentSystemCode

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The system code most recently selected by the reader session during a polling sequence.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var currentSystemCode: Data { get }
```

```objc
@property (nonatomic, retain, readonly) NSData * currentSystemCode;
```

#### Discussion

The system code matches one of the entries in the array for the [`ISO18092 system codes for NFC Tag Reader Session`](../../BundleResources/entitlements/com.apple.developer.nfc.readersession.felica.systemcodes.md) information property list key.

## See Also

### Getting Current Information
- [var currentIDm: Data](./currentidm.md)
  The manufacturer identifier for the system currently selected by the reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/currentsystemcode)*