# eligibleURLs

**Framework**: StoreKit  
**Kind**: property

An array of external purchase links for the current storefront that the app configured and from which it chooses.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- tvOS 17.5+
- visionOS 1.2+
- watchOS 10.5+

## Declaration

```swift
static var eligibleURLs: [URL]? { get async }
```

#### Discussion

Use this property if your app configures the [`SKExternalPurchaseMultiLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseMultiLink) property list key.

Use the [`eligibleURLs`](externalpurchaselink/eligibleurls.md) to get the array of external purchase links for the current storefront that your app has configured in the [`SKExternalPurchaseMultiLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseMultiLink) property list key. Your app can select from any of the eligible URLs. Call [`open(url:)`](externalpurchaselink/open(url:).md) with the URL you choose.

The [`eligibleURLs`](externalpurchaselink/eligibleurls.md) array is `nil` if any of the following is true:

- The current App Store storefront doesn’t allow external purchase or the person isn’t eligible to make external purchases.
- Your app doesn’t configure the [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link) entitlement.
- Your app doesn’t configure any links for the current storefront in the [`SKExternalPurchaseMultiLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseMultiLink) property list key

If this value is `nil` and your app also configures the [`SKExternalPurchaseLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseLink) property list key, check [`canOpen`](externalpurchaselink/canopen.md) to determine whether your app can continue to provide an external purchase link.

Otherwise, if this value is `nil`, check [`canMakePayments`](appstore/canmakepayments.md) to determine whether your app can offer in-app purchases using the StoreKit [`In-App Purchase`](in-app-purchase.md) APIs. For more information, see [`canMakePayments`](appstore/canmakepayments.md).

## See Also

- [SKExternalPurchaseMultiLink](../BundleResources/Information-Property-List/SKExternalPurchaseMultiLink.md)
  A dictionary that contains an array of URLs to websites where people using your app can make external purchases.
- [static func open(url: URL) async throws](externalpurchaselink/open(url:).md)
  Presents a continuation sheet that enables people to choose whether your app shows the indicated URL link for external purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchaselink/eligibleurls)*