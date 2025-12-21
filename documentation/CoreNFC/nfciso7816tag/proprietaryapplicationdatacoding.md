# proprietaryApplicationDataCoding

**Framework**: Core NFC  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the application data follows proprietary data coding.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var proprietaryApplicationDataCoding: Bool { get }
```

#### Discussion

If the value is [`false`](https://developer.apple.com/documentation/Swift/false), data in the [`applicationData`](nfciso7816tag/applicationdata.md) property follows the ISO14443-3 specification.

## See Also

- [var initialSelectedAID: String](nfciso7816tag/initialselectedaid.md)
  A hexadecimal string of the application identifier for the tag selected by the reader session when discovering new tags.
- [var identifier: Data](nfciso7816tag/identifier.md)
  The unique hardware identifier of the tag.
- [var historicalBytes: Data?](nfciso7816tag/historicalbytes.md)
  The historical bytes extracted from the Type A Answer To Select response.
- [var applicationData: Data?](nfciso7816tag/applicationdata.md)
  The application data bytes extracted from the Type B Answer To Request response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816tag/proprietaryapplicationdatacoding)*