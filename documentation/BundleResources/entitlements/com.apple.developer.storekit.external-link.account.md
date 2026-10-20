# com.apple.developer.storekit.external-link.account

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether your app can link to an external website for account creation or management.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- tvOS 16.4+

## Details

- **Name**: `com.apple.developer.storekit.external-link.account`
- **Type**: boolean

#### Discussion

If your developer account has this entitlement, add it to your app by opening the project’s entitlements file in Xcode. Add the following key and set the corresponding value to `true`:

```xml
<plist>
<dict>
    <key>com.apple.developer.storekit.external-link.account</key>
    <true/>
</dict>
</plist>
```

## See Also

### StoreKit
- [StoreKit external purchases or offers entitlement](./com.apple.developer.storekit.custom-purchase-link.allowed-regions.md)
  An entitlement that enables a qualifying app to offer external purchases within app or at a website, in specific regions.
- [com.apple.developer.storekit.external-purchase](./com.apple.developer.storekit.external-purchase.md)
  A Boolean value that indicates whether your app can offer external purchases.
- [com.apple.developer.storekit.external-purchase-link](./com.apple.developer.storekit.external-purchase-link.md)
  A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
- [com.apple.developer.storekit.external-purchase-link-streaming](./com.apple.developer.storekit.external-purchase-link-streaming.md)
  An entitlement that grants a qualifying music-streaming app the ability to communicate and promote offers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-link.account)*