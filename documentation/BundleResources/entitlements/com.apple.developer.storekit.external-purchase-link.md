# com.apple.developer.storekit.external-purchase-link

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Details

- **Name**: `com.apple.developer.storekit.external-purchase-link`
- **Type**: boolean

## Discussion

The [`com.apple.developer.storekit.external-purchase-link`](./com.apple.developer.storekit.external-purchase-link.md) entitlement enables qualifying apps to include a link that directs people using the app to a website to make an external purchase. For more information, see [External Purchase](../../StoreKit/external-purchase.md).

If your account receives this entitlement, which is also known as the StoreKit External Purchase Link entitlement, you can add it to your app by opening the project’s `.entitlements` file in Xcode. Then add the following key and set the corresponding value to `true`:

```xml
<plist>
<dict>
    <key>com.apple.developer.storekit.external-purchase-link</key>
    <true/>
</dict>
</plist>
```

## See Also

### StoreKit
- [StoreKit external purchases or offers entitlement](./com.apple.developer.storekit.custom-purchase-link.allowed-regions.md)
  An entitlement that enables a qualifying app to offer external purchases within app or at a website, in specific regions.
- [com.apple.developer.storekit.external-link.account](./com.apple.developer.storekit.external-link.account.md)
  A Boolean value that indicates whether your app can link to an external website for account creation or management.
- [com.apple.developer.storekit.external-purchase](./com.apple.developer.storekit.external-purchase.md)
  A Boolean value that indicates whether your app can offer external purchases.
- [com.apple.developer.storekit.external-purchase-link-streaming](./com.apple.developer.storekit.external-purchase-link-streaming.md)
  An entitlement that grants a qualifying music-streaming app the ability to communicate and promote offers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link)*