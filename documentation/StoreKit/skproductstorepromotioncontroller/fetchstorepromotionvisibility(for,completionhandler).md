# fetchStorePromotionVisibility(for:completionHandler:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Reads the visibility setting of a promoted product in the App Store for this device.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0
- iPadOS 11.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 11.0+ - Deprecated in 18.0

> **Deprecated**: Get visibility from Product.PromotionInfo.currentOrder.

## Declaration

```swift
func fetchStorePromotionVisibility(for product: SKProduct, completionHandler: (@Sendable (SKProductStorePromotionVisibility, (any Error)?) -> Void)? = nil)
```

```swift
func promotionVisibility(for product: SKProduct) async throws -> SKProductStorePromotionVisibility
```

```objc
- (void) fetchStorePromotionVisibilityForProduct:(SKProduct *) product completionHandler:(void (^)(SKProductStorePromotionVisibility storePromotionVisibility, NSError *error)) completionHandler;
```

## Mentions

- [Promoting Apple In-App Purchases](../promoting-in-app-purchases.md)

#### Discussion

The default visibility for a promoted product is set in App Store Connect. Call [`fetchStorePromotionVisibility(for:completionHandler:)`](./fetchstorepromotionvisibility%28for,completionhandler%29.md) to determine if a product’s visibility is set to the default value or if it has been overridden to be hidden or shown.

## See Also

### Managing promoted product visibility
- [func update(storePromotionVisibility: SKProductStorePromotionVisibility, for: SKProduct, completionHandler: (((any Error)?) -> Void)?)](./update%28storepromotionvisibility,for,completionhandler%29.md)
  Updates the visibility of the product on the App Store, per device.
- [enum SKProductStorePromotionVisibility](../skproductstorepromotionvisibility.md)
  The visibility settings that determine if an Apple In-App Purchase is visible on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/fetchstorepromotionvisibility(for:completionhandler:))*