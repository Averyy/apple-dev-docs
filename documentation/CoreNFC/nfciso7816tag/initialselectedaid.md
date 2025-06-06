# initialSelectedAID

**Framework**: Core NFC  
**Kind**: property  
**Required**: Yes

A hexadecimal string of the application identifier for the tag selected by the reader session when discovering new tags.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var initialSelectedAID: String { get }
```

#### Discussion

The value matches one of the entries in the [`com.apple.developer.nfc.readersession.iso7816.select-identifiers`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/com.apple.developer.nfc.readersession.iso7816.select-identifiers) information property list key.

## See Also

- [var identifier: Data](nfciso7816tag/identifier.md)
  The unique hardware identifier of the tag.
- [var historicalBytes: Data?](nfciso7816tag/historicalbytes.md)
  The historical bytes extracted from the Type A Answer To Select response.
- [var applicationData: Data?](nfciso7816tag/applicationdata.md)
  The application data bytes extracted from the Type B Answer To Request response.
- [var proprietaryApplicationDataCoding: Bool](nfciso7816tag/proprietaryapplicationdatacoding.md)
  A Boolean value that indicates whether the application data follows proprietary data coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816tag/initialselectedaid)*