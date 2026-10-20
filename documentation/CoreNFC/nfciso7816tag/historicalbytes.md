# historicalBytes

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The historical bytes extracted from the Type A Answer To Select response.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var historicalBytes: Data? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSData * historicalBytes;
```

## See Also

### Getting Tag Information
- [var initialSelectedAID: String](./initialselectedaid.md)
  A hexadecimal string of the application identifier for the tag selected by the reader session when discovering new tags.
- [var identifier: Data](./identifier.md)
  The unique hardware identifier of the tag.
- [var applicationData: Data?](./applicationdata.md)
  The application data bytes extracted from the Type B Answer To Request response.
- [var proprietaryApplicationDataCoding: Bool](./proprietaryapplicationdatacoding.md)
  A Boolean value that indicates whether the application data follows proprietary data coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816tag/historicalbytes)*