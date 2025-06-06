# update(storePromotionOrder:completionHandler:)

**Framework**: StoreKit  
**Kind**: method

Overrides the promoted product order on this device.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 11.0+

## Declaration

```swift
func update(promotionOrder: [SKProduct]) async throws
```

## Mentions

- [Promoting In-App Purchases](promoting-in-app-purchases.md)

#### Discussion

The default order of promoted in-app purchase products is set in App Store Connect. You can override this order per device. For example, you can promote an in-app purchase product that unlocks a specific level in your game when a user reaches the level immediately before the specified level.

To override the default product order, put the product information for the subset of products you want to reorder into an array, in the order you want them to appear in. Pass the array to the [`update(storePromotionOrder:completionHandler:)`](skproductstorepromotioncontroller/update(storepromotionorder:completionhandler:).md) method. The products in the array are shown at the beginning of the list, followed by the remaining in-app purchase products, which are listed in the same relative order that you set in App Store Connect.

To cancel order overrides, send an empty product array to the [`update(storePromotionOrder:completionHandler:)`](skproductstorepromotioncontroller/update(storepromotionorder:completionhandler:).md) method.  The in-app purchase products will be displayed in the default order.

## See Also

- [func fetchStorePromotionOrder(completionHandler: (([SKProduct], (any Error)?) -> Void)?)](skproductstorepromotioncontroller/fetchstorepromotionorder(completionhandler:).md)
  Reads the product order override that determines the promoted product order on this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/update(storepromotionorder:completionhandler:))*