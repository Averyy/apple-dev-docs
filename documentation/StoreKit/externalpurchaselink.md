# ExternalPurchaseLink

**Framework**: Storekit  
**Kind**: enum

Enables qualifying apps to offer external purchase links.

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
enum ExternalPurchaseLink
```

#### Overview

This functionality is only available to and required by apps with the [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link) entitlement. For more information, see:

- [`Using alternative payment options on the App Store in the European Union`](https://developer.apple.comhttps://developer.apple.com/go/?id=storekit-external-purchase-eu)
- [`Distributing dating apps in the Netherlands`](https://developer.apple.comhttps://developer.apple.com/support/storekit-external-entitlement/)
- [`Distributing apps in Russia that provide an external purchase link`](https://developer.apple.comhttps://developer.apple.com/contact/request/storekit-external-entitlement-ru/)
- [`Distributing music streaming apps in the EEA that provide an external purchase link`](https://developer.apple.comhttps://developer.apple.com/support/music-streaming-services-entitlement-eea/)

> **Note**:  If your app is running on iOS 15.4 through 17.3 or iPadOS 15.4 through 17.3 and is configured to use the External Purchase API, you must check [`canMakePayments`](appstore/canmakepayments.md) before calling the External Purchase APIs. If [`canMakePayments`](appstore/canmakepayments.md) is `false`, do not call the [`ExternalPurchaseLink`](externalpurchaselink.md) or [`ExternalPurchase`](externalpurchase.md) APIs.

## Topics

### Getting multiple external purchase links
- [SKExternalPurchaseMultiLink](../BundleResources/Information-Property-List/SKExternalPurchaseMultiLink.md)
  A dictionary that contains an array of URLs to websites where people using your app can make external purchases.
- [static var eligibleURLs: [URL]?](externalpurchaselink/eligibleurls.md)
  An array of external purchase links for the current storefront that the app configured and from which it chooses.
- [static func open(url: URL) async throws](externalpurchaselink/open(url:).md)
  Presents a continuation sheet that enables people to choose whether your app shows the indicated URL link for external purchases.
### Getting a single external purchase link
- [SKExternalPurchaseLink](../BundleResources/Information-Property-List/SKExternalPurchaseLink.md)
  A dictionary that contains URLs to websites where people using your app can make external purchases for supported regions.
- [static var canOpen: Bool](externalpurchaselink/canopen.md)
  A Boolean value that indicates whether the app can successfully open the configured external purchase link in the current App Store storefront.
- [static func open() async throws](externalpurchaselink/open.md)
  Presents a continuation sheet that enables people to choose whether your app shows its link for external purchases.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [com.apple.developer.storekit.external-purchase-link](../BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link.md)
  A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
- [SKExternalPurchaseMultiLink](../BundleResources/Information-Property-List/SKExternalPurchaseMultiLink.md)
  A dictionary that contains an array of URLs to websites where people using your app can make external purchases.
- [SKExternalPurchaseLink](../BundleResources/Information-Property-List/SKExternalPurchaseLink.md)
  A dictionary that contains URLs to websites where people using your app can make external purchases for supported regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/StoreKit/externalpurchaselink)*