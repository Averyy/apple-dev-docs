# initialSelectedAID

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (nonatomic, retain, readonly) NSString * initialSelectedAID;
```

## Discussion

The value matches one of the entries in the [`ISO7816 application identifiers for NFC Tag Reader Session`](../../BundleResources/entitlements/com.apple.developer.nfc.readersession.iso7816.select-identifiers.md) information property list key.

## See Also

### Getting Tag Information
- [var identifier: Data](./identifier.md)
  The unique hardware identifier of the tag.
- [var historicalBytes: Data?](./historicalbytes.md)
  The historical bytes extracted from the Type A Answer To Select response.
- [var applicationData: Data?](./applicationdata.md)
  The application data bytes extracted from the Type B Answer To Request response.
- [var proprietaryApplicationDataCoding: Bool](./proprietaryapplicationdatacoding.md)
  A Boolean value that indicates whether the application data follows proprietary data coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816tag/initialselectedaid)*