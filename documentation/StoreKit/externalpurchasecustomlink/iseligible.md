# isEligible

**Framework**: StoreKit  
**Kind**: property

A Boolean value that indicates at runtime whether the app can use this API to offer custom links for external purchases.

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

#### Discussion

Check this value if your app configures the [`SKExternalPurchaseCustomLinkRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions) property list key. If [`isEligible`](externalpurchasecustomlink/iseligible.md) is `true`, your app can use the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API. This value is `true` if all the following conditions are met:

- The current App Store storefront allows custom links for external purchases and the person can make purchases.
- Your app configures the [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link) entitlement.
- Your app configures the current App Store storefront in the [`SKExternalPurchaseCustomLinkRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions) property list key.

If [`isEligible`](externalpurchasecustomlink/iseligible.md) is `false`, don’t use the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API. The methods of the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API throw errors at runtime when [`isEligible`](externalpurchasecustomlink/iseligible.md) is `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/iseligible)*