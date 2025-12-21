# SKExternalPurchaseMultiLink

**Framework**: Bundle Resources  
**Kind**: dictionary

A dictionary that contains an array of URLs to websites where people using your app can make external purchases.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- tvOS 17.5+
- visionOS 1.2+
- watchOS 10.5+

#### Discussion

Use this information property list key if your app has the [`com.apple.developer.storekit.external-purchase-link`](entitlements/com.apple.developer.storekit.external-purchase-link.md) entitlement.

The keys for this dictionary are lowercased ISO 3166-1 alpha-2 country codes. Valid country codes include those for the European Union: Austria (`at`), Belgium (`be`), Bulgaria (`bg`), Croatia (`hr`), Cyprus (`cy`), Czechia (`cz`), Denmark (`dk`), Estonia (`ee`), Finland (`fi`), France (`fr`), Germany (`de`), Greece (`gr`), Hungary (`hu`), Ireland (`ie`), Italy (`it`), Latvia (`lv`), Lithuania (`lt`), Luxembourg (`lu`), Malta (`mt`), Netherlands (`nl`), Poland (`pl`), Portugal (`pt`), Romania (`ro`), Slovakia (`sk`), Slovenia (`si`), Spain (`es`), Sweden (`se`); and Iceland (`is`), Norway (`no`), and Russia (`ru`).

Include a key entry for each country code where your app supports an external purchase link. Provide from one to five destination URLs (links to your website) for your app to choose from for each country code.

> **Note**:  You can provide one or more links if your app qualifies for the StoreKit External Purchase Link entitlement as described in [`Distributing music streaming apps in the EEA that provide an external purchase link`](https://developer.apple.comhttps://developer.apple.com/support/music-streaming-services-entitlement-eea/).  Otherwise, provide one link for each country code.

Your app accesses these URLs through the [`eligibleURLs`](https://developer.apple.com/documentation/StoreKit/ExternalPurchaseLink/eligibleURLs) array in the [`ExternalPurchaseLink`](https://developer.apple.com/documentation/StoreKit/ExternalPurchaseLink) object, and uses the link you select with the [`open(url:)`](https://developer.apple.com/documentation/StoreKit/ExternalPurchaseLink/open(url:)) method in the [`ExternalPurchaseLink`](https://developer.apple.com/documentation/StoreKit/ExternalPurchaseLink) object.

> ❗ **Important**:  At all times, the destination URLs that you provide in the property list key must match the values in your app binary that you submit to App Review.

Make sure each destination URL meets all of the following conditions:

- Uses the HTTPS scheme
- Forms a valid, absolute URL
- Contains no query parameters
- Contains 1,000 or fewer ASCII characters

The following code example shows a property list entry with keys for several country codes, and links for each entry:

```xml
<key>SKExternalPurchaseMultiLink</key>
<dict>
    <key>es</key>
    <array>
        <string>https://www.example.com/es1</string>
        <string>https://www.example.com/new-user-es</string>
        <string>https://www.example.com/seasonal-sale-es</string>
        <string>https://www.example.com/es2</string>
        <string>https://www.example.com/es3</string>
    </array>
    <key>fr</key>
    <array>
        <string>https://www.example.com/fr</string>
        <string>https://www.example.com/global-sale</string>
        <string>https://www.example.com/new-user-fr</string>
    </array>
    <key>it</key>
    <array>
        <string>https://www.example.com/global-sale</string>
    </array>
</dict>
```

The order of the links is not significant.

For more information, see [`External Purchase`](https://developer.apple.com/documentation/StoreKit/external-purchase) and [`ExternalPurchaseLink`](https://developer.apple.com/documentation/StoreKit/ExternalPurchaseLink).

##### Provide Up to the Maximum Number of Links

The following country codes have a maximum of five links for apps that qualify for the StoreKit External Purchase Link entitlement as described in [`Distributing music streaming apps in the EEA that provide an external purchase link`](https://developer.apple.comhttps://developer.apple.com/support/music-streaming-services-entitlement-eea/): Austria (`at`), Belgium (`be`), Bulgaria (`bg`), Croatia (`hr`), Cyprus (`cy`), Czechia (`cz`), Denmark (`dk`), Estonia (`ee`), Finland (`fi`), France (`fr`), Germany (`de`), Greece (`gr`), Hungary (`hu`), Ireland (`ie`), Italy (`it`), Latvia (`lv`), Lithuania (`lt`), Luxembourg (`lu`), Malta (`mt`), Netherlands (`nl`), Poland (`pl`), Portugal (`pt`), Romania (`ro`), Slovakia (`sk`), Slovenia (`si`), Spain (`es`), Sweden (`se`), Iceland (`is`), Norway (`no`). Otherwise, the maximum is one link, for valid country codes.

Count the total number of unique links you provide for each country code by adding together the number of links you provide in the [`SKExternalPurchaseMultiLink`](information-property-list/skexternalpurchasemultilink.md) and [`SKExternalPurchaseLink`](information-property-list/skexternalpurchaselink.md) property list keys.

For example, if a country code has a maximum of five links and you provide five unique links in the [`SKExternalPurchaseMultiLink`](information-property-list/skexternalpurchasemultilink.md) key, then specify one of the same five links in the [`SKExternalPurchaseLink`](information-property-list/skexternalpurchaselink.md) key to avoid exceeding the maximum allowed links.  If a country code has a maximum of one link, the [`SKExternalPurchaseMultiLink`](information-property-list/skexternalpurchasemultilink.md) and [`SKExternalPurchaseLink`](information-property-list/skexternalpurchaselink.md) keys need to specify the same link.

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
- [SKIncludeConsumableInAppPurchaseHistory](information-property-list/skincludeconsumableinapppurchasehistory.md)
  A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.
- [SKExternalPurchaseLinkStreamingRegions](information-property-list/skexternalpurchaselinkstreamingregions.md)
  A list of country codes that indicate the regions where your music-streaming app communicates and promotes offers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/skexternalpurchasemultilink)*