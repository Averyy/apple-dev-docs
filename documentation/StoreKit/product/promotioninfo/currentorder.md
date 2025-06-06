# currentOrder

**Framework**: Storekit  
**Kind**: property

Gets the customized order of the promotion info objects the represent promoted products.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+

## Declaration

```swift
static var currentOrder: [Product.PromotionInfo] { get async throws }
```

## Mentions

- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md)

#### Discussion

This asynchronous array returns a list of [`Product.PromotionInfo`](product/promotioninfo.md) objects in the custom order they appear in on the device.

> **Note**:  This list is empty if you don’t override the order, and the App Store displays the products in their default order.

For information about setting the default order using App Store Connect, see [`Promote in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/promote-in-app-purchases).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/promotioninfo/currentorder)*