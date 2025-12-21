# ExternalPurchaseCustomLink.Token

**Framework**: StoreKit  
**Kind**: struct

A token you use with the External Purchase custom link API.

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

#### Overview

StoreKit returns an external purchase token of this type when you call the [`token(for:)`](externalpurchasecustomlink/token(for:).md) function. For more information, see [`Receiving and decoding external purchase tokens`](receiving-and-decoding-external-purchase-tokens.md).

## Topics

### Getting the token value
- [let value: String](externalpurchasecustomlink/token/value.md)
  A Base64URL-encoded JSON string that represents the external purchase token.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum ExternalPurchaseCustomLink](externalpurchasecustomlink.md)
  A value that enables qualifying apps to offer custom links for external purchases and use alternative payment service providers.
- [com.apple.developer.storekit.custom-purchase-link.allowed-regions](../BundleResources/Entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions.md)
  An entitlement that enables a qualifying app to offer external purchases within app or at a website, in specific regions.
- [com.apple.developer.storekit.external-purchase-link](../BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link.md)
  A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
- [SKExternalPurchaseCustomLinkRegions](../BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions.md)
  An array of country code strings that indicate the regions where your app supports custom links for the communication and promotion of offers.
- [Testing transactions that use custom link tokens](testing-transactions-that-use-custom-link-tokens.md)
  Recognize custom link tokens that your app receives in the sandbox testing environment, and use them to test reporting transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/token)*