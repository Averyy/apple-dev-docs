# SKExternalLinkAccount

**Framework**: Bundle Resources  
**Kind**: dictionary

A dictionary that contains localized URLs to an external website for account creation or management.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- tvOS 16.4+

#### Discussion

Use this information property list key if your app has the [`com.apple.developer.storekit.external-link.account`](entitlements/com.apple.developer.storekit.external-link.account.md) entitlement. Each key is a string that is a lowercase ISO 3166-1 alpha-2 country code, the value for which is a URL to the localized version of the external website for that locale. The dictionary must contain a key with the string `*` that maps to a default URL.

The following shows a property list with a default URL and a specific URL for the `jp` locale:

```xml
<plist>
<dict>
    <key>SKExternalLinkAccount</key>
    <dict>
        <key>*</key>
        <string>https://example.com</string>
        <key>jp</key>
        <string>https://example.com/jp</string>
    </dict>
</dict>
</plist>
```

## See Also

- [SKAdNetworkItems](information-property-list/skadnetworkitems.md)
  An array of dictionaries containing a list of ad network IDs.
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

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/skexternallinkaccount)*