# CustomerEngagementSession.Configuration

**Framework**: ProximityReader  
**Kind**: struct

A set of configuration options for a customer engagement session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct Configuration
```

## Topics

### Initializers
- [init(currency: Locale.Currency, region: Locale.Region, privacyPolicyURL: URL, websiteURL: URL?, storeName: String?, deviceName: String?, passTypeIdentifiers: [String])](customerengagementsession/configuration-swift.struct/init(currency:region:privacypolicyurl:websiteurl:storename:devicename:passtypeidentifiers:).md)
### Instance Properties
- [var currency: Locale.Currency](customerengagementsession/configuration-swift.struct/currency.md)
  The currency to localize the amounts in the shopping cart.
- [var deviceName: String?](customerengagementsession/configuration-swift.struct/devicename.md)
  The device name or sales staff name to identify the merchant device.
- [var passTypeIdentifiers: [String]](customerengagementsession/configuration-swift.struct/passtypeidentifiers.md)
  An array of pass type identifiers for the your passes.
- [var privacyPolicyURL: URL](customerengagementsession/configuration-swift.struct/privacypolicyurl.md)
  A URL for your privacy policy.
- [var region: Locale.Region](customerengagementsession/configuration-swift.struct/region.md)
  The region to localize the amounts in the shopping cart.
- [var storeName: String?](customerengagementsession/configuration-swift.struct/storename.md)
  The store name or location to identify the specific store.
- [var websiteURL: URL?](customerengagementsession/configuration-swift.struct/websiteurl.md)
  The merchant website URL.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let configuration: CustomerEngagementSession.Configuration](customerengagementsession/configuration-swift.property.md)
  Configuration for this session.
- [func open(using: CustomerEngagement.Token?) async throws](customerengagementsession/open(using:).md)
  Opens the engagement session.
- [func close() async throws](customerengagementsession/close.md)
  Closes the engagement session.
- [CustomerEngagementSession.Token](customerengagementsession/token-swift.struct.md)
  A session token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/configuration-swift.struct)*