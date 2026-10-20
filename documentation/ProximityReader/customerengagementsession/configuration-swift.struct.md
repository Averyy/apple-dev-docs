# CustomerEngagementSession.Configuration

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A set of configuration options for a customer engagement session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Initializers
- [init(currency: Locale.Currency, region: Locale.Region, privacyPolicyURL: URL, websiteURL: URL?, storeName: String?, deviceName: String?, passTypeIdentifiers: [String])](./configuration-swift.struct/init%28currency,region,privacypolicyurl,websiteurl,storename,devicename,passtypeidentifiers%29.md)
### Instance Properties
- [var currency: Locale.Currency](./configuration-swift.struct/currency.md)
  The currency to localize the amounts in the shopping cart.
- [var deviceName: String?](./configuration-swift.struct/devicename.md)
  The device name or sales staff name to identify the merchant device.
- [var passTypeIdentifiers: [String]](./configuration-swift.struct/passtypeidentifiers.md)
  An array of pass type identifiers for the your passes.
- [var privacyPolicyURL: URL](./configuration-swift.struct/privacypolicyurl.md)
  A URL for your privacy policy.
- [var region: Locale.Region](./configuration-swift.struct/region.md)
  The region to localize the amounts in the shopping cart.
- [var storeName: String?](./configuration-swift.struct/storename.md)
  The store name or location to identify the specific store.
- [var websiteURL: URL?](./configuration-swift.struct/websiteurl.md)
  The merchant website URL.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring a session
- [let configuration: CustomerEngagementSession.Configuration](./configuration-swift.property.md)
  Configuration for this session.
- [func open(using: CustomerEngagement.Token?) async throws](./open%28using%29.md)
  Opens the engagement session.
- [func close() async throws](./close%28%29.md)
  Closes the engagement session.
- [CustomerEngagementSession.Token](./token-swift.struct.md)
  A session token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/configuration-swift.struct)*