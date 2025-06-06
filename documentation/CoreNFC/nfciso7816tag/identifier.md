# identifier

**Framework**: Core NFC  
**Kind**: property  
**Required**: Yes

The unique hardware identifier of the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var identifier: Data { get }
```

#### Discussion

The [`identifier`](nfciso7816tag/identifier.md) data is in big-endian byte order.

## See Also

- [var initialSelectedAID: String](nfciso7816tag/initialselectedaid.md)
  A hexadecimal string of the application identifier for the tag selected by the reader session when discovering new tags.
- [var historicalBytes: Data?](nfciso7816tag/historicalbytes.md)
  The historical bytes extracted from the Type A Answer To Select response.
- [var applicationData: Data?](nfciso7816tag/applicationdata.md)
  The application data bytes extracted from the Type B Answer To Request response.
- [var proprietaryApplicationDataCoding: Bool](nfciso7816tag/proprietaryapplicationdatacoding.md)
  A Boolean value that indicates whether the application data follows proprietary data coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816tag/identifier)*