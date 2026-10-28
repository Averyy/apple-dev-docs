# isEligible

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates at runtime whether the app can use this API for external purchases.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- tvOS 18.1+
- visionOS 2.1+
- watchOS 11.1+

## Declaration

```swift
static var isEligible: Bool { get async }
```

## Mentions

- [Testing transactions that use custom link tokens](../testing-transactions-that-use-custom-link-tokens.md)

## Discussion

Check this value if your app configures any of the following entitlements:

- [`StoreKit external purchases or offers entitlement`](../../BundleResources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions.md)
- [`com.apple.developer.storekit.external-purchase-link`](../../BundleResources/entitlements/com.apple.developer.storekit.external-purchase-link.md)
- [`com.apple.developer.storekit.external-purchase-link-streaming`](../../BundleResources/entitlements/com.apple.developer.storekit.external-purchase-link-streaming.md)

If [`isEligible`](./iseligible.md) is `true`, your app can use the [`ExternalPurchaseCustomLink`](../externalpurchasecustomlink.md) API.

This value is `true` if all the following conditions are met:

- The current App Store storefront allows external purchases and the person can make purchases.
- Your app configures any of the entitlements listed above.
- Your app configures the current App Store storefront in the property list key associated with the entitlement, [`SKExternalPurchaseCustomLinkRegions`](../../BundleResources/information-property-list/skexternalpurchasecustomlinkregions.md) or [`SKExternalPurchaseLinkStreamingRegions`](../../BundleResources/information-property-list/skexternalpurchaselinkstreamingregions.md), or has an entitlement that includes the current App Store storefront.

If [`isEligible`](./iseligible.md) is `false`, don’t use the [`ExternalPurchaseCustomLink`](../externalpurchasecustomlink.md) API. The methods of the [`ExternalPurchaseCustomLink`](../externalpurchasecustomlink.md) API throw errors at runtime when [`isEligible`](./iseligible.md) is `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/iseligible)*