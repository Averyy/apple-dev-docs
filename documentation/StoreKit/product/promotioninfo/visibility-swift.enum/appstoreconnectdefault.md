# Product.PromotionInfo.Visibility.appStoreConnectDefault

**Framework**: StoreKit  
**Kind**: case

A visibility value for a promoted Apple In-App Purchase that uses the visibility setting from App Store Connect.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
case appStoreConnectDefault
```

## Mentions

- [Supporting promoted Apple In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md)

#### Discussion

When a promoted Apple In-App Purchase has a visibility value of [`Product.PromotionInfo.Visibility.appStoreConnectDefault`](product/promotioninfo/visibility-swift.enum/appstoreconnectdefault.md), the Apple In-App Purchase is:

- Visible if the setting in App Store Connect makes it visible
- Hidden if the setting in App Store Connect makes it hidden

Use this value to control the visibility for promoted Apple In-App Purchases in App Store Connect, globally, for all users. For example, if you have a product to promote on a holiday, start by manually setting it as hidden using App Store Connect. On the holiday, change the setting to make the promotion visible. If the promotion visibility in the app is the default ([`Product.PromotionInfo.Visibility.appStoreConnectDefault`](product/promotioninfo/visibility-swift.enum/appstoreconnectdefault.md)), it becomes visible for all users automatically.

For more information about the visibility settings in App Store Connect, see [`Promote Apple In-App Purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/promote-in-app-purchases).

## See Also

- [Product.PromotionInfo.Visibility.hidden](product/promotioninfo/visibility-swift.enum/hidden.md)
  A visibility value that hides a promoted Apple In-App Purchase on the App Store on a user’s device.
- [Product.PromotionInfo.Visibility.visible](product/promotioninfo/visibility-swift.enum/visible.md)
  A visibility value that makes a promoted Apple In-App Purchase visible on the App Store on a user’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/promotioninfo/visibility-swift.enum/appstoreconnectdefault)*