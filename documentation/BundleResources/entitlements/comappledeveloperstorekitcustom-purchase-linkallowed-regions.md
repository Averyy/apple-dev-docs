# com.apple.developer.storekit.custom-purchase-link.allowed-regions

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that enables a qualifying app to offer external purchases within app or at a website, in specific regions.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- macOS 26.2+
- tvOS 26.2+
- visionOS 26.2+
- watchOS 26.2+

#### Discussion

This entitlement enables a qualifying app to offer external purchases within the app or at a website of its choice, in specific regions.

If your account receives this entitlement, you can add it to your app by opening the project’s `.entitlements` file in Xcode. Then, add a key named `com.apple.developer.storekit.custom-purchase-link.allowed-regions`, followed by an array that enumerates the two-letter ISO-3166-1 country codes for the allowed regions. The example below describes an entitlement that includes Germany and Italy as the allowed regions that the app supports.

```None
<plist>
<dict>
    <key>com.apple.developer.storekit.custom-purchase-link.allowed-regions</key>
    <array>
     <string>it</string>
     <string>de</string>
    </array>
</dict>
</plist>
```

> ❗ **Important**: Provide the regions where you intend to offer this functionality. This must only include regions where Apple has authorized your app to offer alternative payment options.

For more information, see [`External Purchase`](https://developer.apple.com/documentation/StoreKit/external-purchase).

## See Also

- [com.apple.developer.storekit.external-link.account](entitlements/com.apple.developer.storekit.external-link.account.md)
  A Boolean value that indicates whether your app can link to an external website for account creation or management.
- [com.apple.developer.storekit.external-purchase](entitlements/com.apple.developer.storekit.external-purchase.md)
  A Boolean value that indicates whether your app can offer external purchases.
- [com.apple.developer.storekit.external-purchase-link](entitlements/com.apple.developer.storekit.external-purchase-link.md)
  A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
- [com.apple.developer.storekit.external-purchase-link-streaming](entitlements/com.apple.developer.storekit.external-purchase-link-streaming.md)
  An entitlement that grants a qualifying music-streaming app the ability to communicate and promote offers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions)*