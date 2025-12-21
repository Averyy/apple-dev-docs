# isEligible

**Framework**: StoreKit  
**Kind**: property

A Boolean value that indicates at runtime whether the app can use this API for external purchases.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- macOS 15.1+
- tvOS 18.1+
- visionOS 2.1+
- watchOS 11.1+

## Declaration

```swift
static var isEligible: Bool { get async }
```

## Mentions

- [Testing transactions that use custom link tokens](testing-transactions-that-use-custom-link-tokens.md)

#### Discussion

Check this value if your app configures any of the following entitlements:

- [`com.apple.developer.storekit.custom-purchase-link.allowed-regions`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions)
- doc://com.apple.documentation/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link-streaming.allowed-regions
- [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link)
- [`com.apple.developer.storekit.external-purchase-link-streaming`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link-streaming)

If [`isEligible`](externalpurchasecustomlink/iseligible.md) is `true`, your app can use the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API.

This value is `true` if all the following conditions are met:

- The current App Store storefront allows external purchases and the person can make purchases.
- Your app configures any of the entitlements listed above.
- Your app configures the current App Store storefront in the property list key associated with the entitlement, [`SKExternalPurchaseCustomLinkRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions) or [`SKExternalPurchaseLinkStreamingRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseLinkStreamingRegions), or has an entitlement that includes the current App Store storefront.

If [`isEligible`](externalpurchasecustomlink/iseligible.md) is `false`, don’t use the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API. The methods of the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API throw errors at runtime when [`isEligible`](externalpurchasecustomlink/iseligible.md) is `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/iseligible)*