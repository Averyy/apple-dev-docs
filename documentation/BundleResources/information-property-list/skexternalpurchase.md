# SKExternalPurchase

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A string array of country codes that indicates your app supports external purchases.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Details

- **Name**: `SKExternalPurchase`
- **Type**: array of string 

## Discussion

Use this information property list key if your app has the [`com.apple.developer.storekit.external-purchase`](../entitlements/com.apple.developer.storekit.external-purchase.md) entitlement.

To the array, add a string containing the lowercased ISO 3166-1 alpha-2 country code for each country where your app supports external purchases. The following code example shows a property list entry with two strings, for the Netherlands (`nl`) and Italy (`it`):

```xml
<plist>
<dict>
    <key>SKExternalPurchase</key>
    <array>
        <string>nl</string>
        <string>it</string>
    </array>
</dict>
</plist>
```

Use valid country codes for the following allowed countries or regions:

- In the European Union: Austria (`at`), Belgium (`be`), Bulgaria (`bg`), Croatia (`hr`), Cyprus (`cy`), Czechia (`cz`), Denmark (`dk`), Estonia (`ee`), Finland (`fi`), France (`fr`), Germany (`de`), Greece (`gr`), Hungary (`hu`), Ireland (`ie`), Italy (`it`), Latvia (`lv`), Lithuania (`lt`), Luxembourg (`lu`), Malta (`mt`), Netherlands (`nl`), Poland (`pl`), Portugal (`pt`), Romania (`ro`), Slovakia (`sk`), Slovenia (`si`), Spain (`es`), Sweden (`se`)
- South Korea (`kr`)

For more information, see [External Purchase](../../StoreKit/external-purchase.md).

## See Also

### StoreKit
- [SKAdNetworkItems](./skadnetworkitems.md)
  An array of dictionaries containing a list of ad network IDs.
- [SKExternalLinkAccount](./skexternallinkaccount.md)
  A dictionary that contains localized URLs to an external website for account creation or management.
- [SKExternalPurchaseCustomLinkRegions](./skexternalpurchasecustomlinkregions.md)
  An array of country code strings that indicate the regions where your app supports custom links for the communication and promotion of offers.
- [SKExternalPurchaseLink](./skexternalpurchaselink.md)
  A dictionary that contains URLs to websites where people using your app can make external purchases for supported regions.
- [SKExternalPurchaseMultiLink](./skexternalpurchasemultilink.md)
  A dictionary that contains an array of URLs to websites where people using your app can make external purchases.
- [SKIncludeConsumableInAppPurchaseHistory](./skincludeconsumableinapppurchasehistory.md)
  A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.
- [SKExternalPurchaseLinkStreamingRegions](./skexternalpurchaselinkstreamingregions.md)
  A list of country codes that indicate the regions where your music-streaming app communicates and promotes offers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/skexternalpurchase)*