# SKExternalPurchaseLink

**Framework**: Bundle Resources  
**Kind**: dictionary

A dictionary that contains URLs to websites where people using your app can make external purchases for supported regions.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

#### Discussion

Use this information property list key if your app has the [`com.apple.developer.storekit.external-purchase-link`](entitlements/com.apple.developer.storekit.external-purchase-link.md) entitlement.

The keys for this dictionary are lowercased ISO 3166-1 alpha-2 country codes. Valid country codes include those for the European Union: Austria (`at`), Belgium (`be`), Bulgaria (`bg`), Croatia (`hr`), Cyprus (`cy`), Czechia (`cz`), Denmark (`dk`), Estonia (`ee`), Finland (`fi`), France (`fr`), Germany (`de`), Greece (`gr`), Hungary (`hu`), Ireland (`ie`), Italy (`it`), Latvia (`lv`), Lithuania (`lt`), Luxembourg (`lu`), Malta (`mt`), Netherlands (`nl`), Poland (`pl`), Portugal (`pt`), Romania (`ro`), Slovakia (`sk`), Slovenia (`si`), Spain (`es`), Sweden (`se`); and Iceland (`is`), Norway (`no`), and Russia (`ru`).

Include one key entry for each country code where your app supports an external purchase link. Provide a destination URL (link to your website) for your app to open when the country code in the key matches the device’s App Store storefront. If you support multiple country codes, you may provide the same or different destination URLs for each country code.

> ❗ **Important**:  At all times, the destination URLs that you provide in the property list key must match the values in your app binary that you submit to App Review.

Make sure the destination URL meets all of the following conditions:

- Uses the HTTPS scheme
- Forms a valid, absolute URL
- Contains no query parameters
- Contains 1,000 or fewer ASCII characters.

The following code example shows a property list entry with a single country code key, for the Netherlands (`nl`). Replace the string “`https://example.com`” below with your link:

```xml
<plist>
<dict>
    <key>SKExternalPurchaseLink</key>
    <dict>
        <key>nl</key>
        <string>https://example.com</string>
    </dict>
</dict>
</plist>
```

The following code example shows a property list entry with keys for more than one country code. Replace the “`https://example.com`” strings with your links:

```xml
<plist>
<dict>
    <key>SKExternalPurchaseLink</key>
    <dict>
        <key>at</key>
        <string>https://ex1.example.com</string>
        <key>nl</key>
        <string>https://ex2.example.com</string>
        <key>it</key>
        <string>https://ex2.example.com</string>
    </dict>
</dict>
</plist>
```

For more information, see [`External Purchase`](https://developer.apple.com/documentation/StoreKit/external-purchase).

## See Also

- [SKAdNetworkItems](information-property-list/skadnetworkitems.md)
  An array of dictionaries containing a list of ad network IDs.
- [SKExternalLinkAccount](information-property-list/skexternallinkaccount.md)
  A dictionary that contains localized URLs to an external website for account creation or management.
- [SKExternalPurchase](information-property-list/skexternalpurchase.md)
  A string array of country codes that indicates your app supports external purchases.
- [SKExternalPurchaseCustomLinkRegions](information-property-list/skexternalpurchasecustomlinkregions.md)
  An array of country code strings that indicate the regions where your app supports custom links for the communication and promotion of offers.
- [SKExternalPurchaseMultiLink](information-property-list/skexternalpurchasemultilink.md)
  A dictionary that contains an array of URLs to websites where people using your app can make external purchases.
- [SKIncludeConsumableInAppPurchaseHistory](information-property-list/skincludeconsumableinapppurchasehistory.md)
  A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.
- [SKExternalPurchaseLinkStreamingRegions](information-property-list/skexternalpurchaselinkstreamingregions.md)
  A list of country codes that indicate the regions where your music-streaming app communicates and promotes offers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/skexternalpurchaselink)*