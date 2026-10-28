# update(storePromotionOrder:completionHandler:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Overrides the promoted product order on this device.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0
- iPadOS 11.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 11.0+ - Deprecated in 18.0

> **Deprecated**: Use Product.PromotionInfo.updateProductOrder(byID:).

## Declaration

```swift
func update(storePromotionOrder promotionOrder: [SKProduct], completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func update(promotionOrder: [SKProduct]) async throws
```

```objc
- (void) updateStorePromotionOrder:(NSArray<SKProduct *> *) promotionOrder completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Mentions

- [Promoting Apple In-App Purchases](../promoting-in-app-purchases.md)

## Discussion

The default order of promoted Apple In-App Purchase products is set in App Store Connect. You can override this order per device. For example, you can promote an Apple In-App Purchase product that unlocks a specific level in your game when a user reaches the level immediately before the specified level.

To override the default product order, put the product information for the subset of products you want to reorder into an array, in the order you want them to appear in. Pass the array to the [`update(storePromotionOrder:completionHandler:)`](./update%28storepromotionorder,completionhandler%29.md) method. The products in the array are shown at the beginning of the list, followed by the remaining Apple In-App Purchase products, which are listed in the same relative order that you set in App Store Connect.

To cancel order overrides, send an empty product array to the [`update(storePromotionOrder:completionHandler:)`](./update%28storepromotionorder,completionhandler%29.md) method.  The Apple In-App Purchase products will be displayed in the default order.

## See Also

### Managing promoted product order
- [func fetchStorePromotionOrder(completionHandler: (([SKProduct], (any Error)?) -> Void)?)](./fetchstorepromotionorder%28completionhandler%29.md)
  Reads the product order override that determines the promoted product order on this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/update(storepromotionorder:completionhandler:))*