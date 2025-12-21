# SKIncludeConsumableInAppPurchaseHistory

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

#### Discussion

By default, this value is `false`. When it’s `false`, StoreKit doesn’t return finished consumables (unless refunded or revoked) in the transaction information from the following APIs:

- The [`all`](https://developer.apple.com/documentation/StoreKit/Transaction/all) sequence in [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction), which returns the customer’s transaction history for your app
- The [`latest(for:)`](https://developer.apple.com/documentation/StoreKit/Transaction/latest(for:)) in [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction), which returns the customer’s most recent transaction for a specific product
- The [`latestTransaction`](https://developer.apple.com/documentation/StoreKit/Product/latestTransaction) in [`Product`](https://developer.apple.com/documentation/StoreKit/Product), which provides the customer’s most recent transaction for the product

When you set this value to `true`, StoreKit includes all In-App Purchase transactions — including all finished consumables — in the transaction information when you use the [`all`](https://developer.apple.com/documentation/StoreKit/Transaction/all), [`latest(for:)`](https://developer.apple.com/documentation/StoreKit/Transaction/latest(for:)), and [`latestTransaction`](https://developer.apple.com/documentation/StoreKit/Product/latestTransaction) APIs.

> ⚠️ **Warning**:  Before you set [`SKIncludeConsumableInAppPurchaseHistory`](information-property-list/skincludeconsumableinapppurchasehistory.md) to `true`, be sure you have a way to reconcile a customer’s consumable transactions on your server, not only on the device. For example, store a transaction’s unique transaction identifier, [`id`](https://developer.apple.com/documentation/StoreKit/Transaction/id), along with its finish state to avoid unintentionally delivering content multiple times if the customer reinstalls the app. Use [`unfinished`](https://developer.apple.com/documentation/StoreKit/Transaction/unfinished) to get and process unfinished transactions.

## See Also

- [SKAdNetworkItems](information-property-list/skadnetworkitems.md)
  An array of dictionaries containing a list of ad network IDs.
- [SKExternalLinkAccount](information-property-list/skexternallinkaccount.md)
  A dictionary that contains localized URLs to an external website for account creation or management.
- [SKExternalPurchase](information-property-list/skexternalpurchase.md)
  A string array of country codes that indicates your app supports external purchases.
- [SKExternalPurchaseCustomLinkRegions](information-property-list/skexternalpurchasecustomlinkregions.md)
  An array of country code strings that indicate the regions where your app supports custom links for the communication and promotion of offers.
- [SKExternalPurchaseLink](information-property-list/skexternalpurchaselink.md)
  A dictionary that contains URLs to websites where people using your app can make external purchases for supported regions.
- [SKExternalPurchaseMultiLink](information-property-list/skexternalpurchasemultilink.md)
  A dictionary that contains an array of URLs to websites where people using your app can make external purchases.
- [SKExternalPurchaseLinkStreamingRegions](information-property-list/skexternalpurchaselinkstreamingregions.md)
  A list of country codes that indicate the regions where your music-streaming app communicates and promotes offers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/skincludeconsumableinapppurchasehistory)*