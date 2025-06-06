# SKAdNetworkItems

**Framework**: Bundle Resources  
**Kind**: dictionary

An array of dictionaries containing a list of ad network IDs.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

#### Discussion

Apps that display ads and initiate install-validation information to share with ad networks need to include the ad network IDs in this key.

Each dictionary contains one [`SKAdNetworkIdentifier`](information-property-list/skadnetworkitems/skadnetworkidentifier.md). Provide one dictionary for each ad network that you work with.

> ❗ **Important**:  Ad network IDs are case-sensitive and are in lowercase.

 Ad network IDs are case-sensitive and are in lowercase.

For more information, see [`Configuring a source app`](https://developer.apple.com/documentation/StoreKit/configuring-a-source-app).

## Topics

### Ad network identifiers
- [SKAdNetworkIdentifier](information-property-list/skadnetworkitems/skadnetworkidentifier.md)
  A string that contains an ad network ID.

## See Also

- [SKExternalLinkAccount](information-property-list/skexternallinkaccount.md)
  A dictionary that contains localized URLs to an external website for account creation or management.
- [SKExternalPurchase](information-property-list/skexternalpurchase.md)
  A string array of country codes that indicates your app supports external purchases.
- [SKExternalPurchaseCustomLinkRegions](information-property-list/skexternalpurchasecustomlinkregions.md)
  An array of country code strings that indicate the regions where your app supports custom links for external purchases.
- [SKExternalPurchaseLink](information-property-list/skexternalpurchaselink.md)
  A dictionary that contains URLs to websites where people using your app can make external purchases for supported regions.
- [SKExternalPurchaseMultiLink](information-property-list/skexternalpurchasemultilink.md)
  A dictionary that contains an array of URLs to websites where people using your app can make external purchases.
- [SKIncludeConsumableInAppPurchaseHistory](information-property-list/skincludeconsumableinapppurchasehistory.md)
  A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/skadnetworkitems)*