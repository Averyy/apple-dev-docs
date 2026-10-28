# canOpen

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the app can successfully open the configured external purchase link in the current App Store storefront.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
static var canOpen: Bool { get async }
```

## Discussion

Use this method if your app configures the [`SKExternalPurchaseLink`](../../BundleResources/information-property-list/skexternalpurchaselink.md) property list key.

Check this property, as shown below, to determine whether your app can successfully call [`open()`](./open%28%29.md).

```swift
await ExternalPurchaseLink.canOpen
```

If the result is `true`, configure any user-interface controls that enable people to open the external purchase link. You configure that link in the [`SKExternalPurchaseLink`](../../BundleResources/information-property-list/skexternalpurchaselink.md) property list key in the `Info.plist` file. There’s no need to call [`canOpen`](./canopen.md) again, unless the App Store storefront changes. For more information about the App Store storefront, see [`Storefront`](../storefront.md).

This property is `true` if all the following conditions are met:

- The current App Store storefront allows external purchase and the person is eligible to make external purchases.
- Your app configures the [`StoreKit external purchases or offers entitlement`](../../BundleResources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions.md) or [`com.apple.developer.storekit.external-purchase-link`](../../BundleResources/entitlements/com.apple.developer.storekit.external-purchase-link.md) entitlement.
- Your app configures a link for the current App Store storefront in [`SKExternalPurchaseLink`](../../BundleResources/information-property-list/skexternalpurchaselink.md).

Otherwise, this property is `false`.

When this property is `false`, check [`canMakePayments`](../appstore/canmakepayments.md) to determine whether your app can offer in-app purchases using the StoreKit [Apple In-App Purchase](../in-app-purchase.md) APIs. For more information, see [`canMakePayments`](../appstore/canmakepayments.md).

## See Also

### Getting a single external purchase link
- [SKExternalPurchaseLink](../../BundleResources/information-property-list/skexternalpurchaselink.md)
  A dictionary that contains URLs to websites where people using your app can make external purchases for supported regions.
- [static func open() async throws](./open%28%29.md)
  Presents a continuation sheet that enables people to choose whether your app shows its link for external purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchaselink/canopen)*