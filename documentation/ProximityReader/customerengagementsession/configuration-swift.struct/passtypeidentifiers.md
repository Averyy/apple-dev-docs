# passTypeIdentifiers

**Framework**: ProximityReader  
**Kind**: property

An array of pass type identifiers for the your passes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var passTypeIdentifiers: [String]
```

#### Discussion

The session queries the Wallet app using this array when you request the pass attribute option in the [`requestCustomerInfo(for:fields:message:)`](customerengagementsession/requestcustomerinfo(for:fields:message:).md). The session also validates this array against `AddPassRequest` to ensure only the merchant supported passes are added to the Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/configuration-swift.struct/passtypeidentifiers)*