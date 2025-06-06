# currentSystemCode

**Framework**: Core NFC  
**Kind**: property  
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

#### Discussion

The system code matches one of the entries in the array for the [`com.apple.developer.nfc.readersession.felica.systemcodes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/com.apple.developer.nfc.readersession.felica.systemcodes) information property list key.

## See Also

- [var currentIDm: Data](nfcfelicatag/currentidm.md)
  The manufacturer identifier for the system currently selected by the reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/currentsystemcode)*