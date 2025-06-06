# com.apple.developer.storekit.external-purchase-link

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

#### Discussion

The [`com.apple.developer.storekit.external-purchase-link`](entitlements/com.apple.developer.storekit.external-purchase-link.md) entitlement enables qualifying apps to include a link that directs people using the app to a website to make an external purchase. For more information about qualifying apps and to request this entitlement, see:

- [`Using alternative payment options on the App Store in the European Union`](https://developer.apple.comhttps://developer.apple.com/go/?id=storekit-external-purchase-eu)
- [`Distributing dating apps in the Netherlands`](https://developer.apple.comhttps://developer.apple.com/support/storekit-external-entitlement/)
- [`Distributing apps in Russia that provide an external purchase link`](https://developer.apple.comhttps://developer.apple.com/contact/request/storekit-external-entitlement-ru/)
- [`Distributing music streaming apps in the EEA that provide an external purchase link`](https://developer.apple.comhttps://developer.apple.com/support/music-streaming-services-entitlement-eea/)

If your account receives this entitlement, which is also known as the StoreKit External Purchase Link entitlement, you can add it to your app by opening the project’s `.entitlements` file in Xcode. Then add the following key and set the corresponding value to `true`:

```xml
<plist>
<dict>
    <key>com.apple.developer.storekit.external-purchase-link</key>
    <true/>
</dict>
</plist>
```

For more information, see [`External Purchase`](https://developer.apple.com/documentation/StoreKit/external-purchase).

## See Also

- [com.apple.developer.storekit.external-link.account](entitlements/com.apple.developer.storekit.external-link.account.md)
  A Boolean value that indicates whether your app can link to an external website for account creation or management.
- [com.apple.developer.storekit.external-purchase](entitlements/com.apple.developer.storekit.external-purchase.md)
  A Boolean value that indicates whether your app can offer external purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link)*