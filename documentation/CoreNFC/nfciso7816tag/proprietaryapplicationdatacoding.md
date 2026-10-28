# proprietaryApplicationDataCoding

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (nonatomic, readonly) BOOL proprietaryApplicationDataCoding;
```

## Discussion

If the value is [`false`](../../Swift/false.md), data in the [`applicationData`](./applicationdata.md) property follows the ISO14443-3 specification.

## See Also

### Getting Tag Information
- [var initialSelectedAID: String](./initialselectedaid.md)
  A hexadecimal string of the application identifier for the tag selected by the reader session when discovering new tags.
- [var identifier: Data](./identifier.md)
  The unique hardware identifier of the tag.
- [var historicalBytes: Data?](./historicalbytes.md)
  The historical bytes extracted from the Type A Answer To Select response.
- [var applicationData: Data?](./applicationdata.md)
  The application data bytes extracted from the Type B Answer To Request response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816tag/proprietaryapplicationdatacoding)*