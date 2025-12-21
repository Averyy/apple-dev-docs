# com.apple.developer.storekit.external-purchase-link-streaming

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that grants a qualifying music-streaming app the ability to communicate and promote offers.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

#### Discussion

This entitlement enables qualifying music-streaming apps to communicate and promote offers.

If your account receives this entitlement, you can add it to your app by opening the project’s `.entitlements` file in Xcode. Then add the following key and set the corresponding value to `true`:

```None
<plist>
<dict>
    <key>com.apple.developer.storekit.external-purchase-link-streaming</key>
    <true/>
</dict>
</plist>
```

For more information, see [`External Purchase`](https://developer.apple.com/documentation/StoreKit/external-purchase).

## See Also

- [com.apple.developer.storekit.custom-purchase-link.allowed-regions](entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions.md)
  An entitlement that enables a qualifying app to offer external purchases within app or at a website, in specific regions.
- [com.apple.developer.storekit.external-link.account](entitlements/com.apple.developer.storekit.external-link.account.md)
  A Boolean value that indicates whether your app can link to an external website for account creation or management.
- [com.apple.developer.storekit.external-purchase](entitlements/com.apple.developer.storekit.external-purchase.md)
  A Boolean value that indicates whether your app can offer external purchases.
- [com.apple.developer.storekit.external-purchase-link](entitlements/com.apple.developer.storekit.external-purchase-link.md)
  A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link-streaming)*