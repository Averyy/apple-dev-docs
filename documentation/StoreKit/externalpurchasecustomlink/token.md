# ExternalPurchaseCustomLink.Token

**Framework**: StoreKit  
**Kind**: struct

An external purchase token for use with custom links.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- macOS 15.1+
- tvOS 18.1+
- visionOS 2.1+
- watchOS 11.1+

## Declaration

```swift
struct Token
```

## Mentions

- [Receiving and decoding external purchase tokens](receiving-and-decoding-external-purchase-tokens.md)

#### Overview

StoreKit returns an external purchase token of this type when you call the [`token(for:)`](externalpurchasecustomlink/token(for:).md) function. Your app gets these tokens if it configures the [`SKExternalPurchaseCustomLinkRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions) property list key and uses the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API.

For more information about tokens, see [`Receiving and decoding external purchase tokens`](receiving-and-decoding-external-purchase-tokens.md).

## Topics

### Getting the token value
- [let value: String](externalpurchasecustomlink/token/value.md)
  A Base64URL-encoded JSON string that represents the external purchase token.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum ExternalPurchaseCustomLink](externalpurchasecustomlink.md)
  Enables qualifying apps to offer custom links for external purchases.
- [com.apple.developer.storekit.external-purchase-link](../BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link.md)
  A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
- [SKExternalPurchaseCustomLinkRegions](../BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions.md)
  An array of country code strings that indicate the regions where your app supports custom links for external purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/token)*