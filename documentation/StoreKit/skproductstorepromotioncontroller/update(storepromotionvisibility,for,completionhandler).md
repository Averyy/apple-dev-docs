# update(storePromotionVisibility:for:completionHandler:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Updates the visibility of the product on the App Store, per device.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0
- iPadOS 11.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 11.0+ - Deprecated in 18.0

> **Deprecated**: Use Product.PromotionInfo.updateProductVisibility(_:for:).

## Declaration

```swift
func update(storePromotionVisibility promotionVisibility: SKProductStorePromotionVisibility, for product: SKProduct, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func update(promotionVisibility: SKProductStorePromotionVisibility, for product: SKProduct) async throws
```

```objc
- (void) updateStorePromotionVisibility:(SKProductStorePromotionVisibility) promotionVisibility forProduct:(SKProduct *) product completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

An Apple In-App Purchase product’s default visibility setting is set up in App Store Connect.  You can override the default setting, or return it to the default set in App Store Connect using the values in [`SKProductStorePromotionVisibility`](../skproductstorepromotionvisibility.md).

Visibility settings apply per device.

## See Also

### Managing promoted product visibility
- [func fetchStorePromotionVisibility(for: SKProduct, completionHandler: ((SKProductStorePromotionVisibility, (any Error)?) -> Void)?)](./fetchstorepromotionvisibility%28for,completionhandler%29.md)
  Reads the visibility setting of a promoted product in the App Store for this device.
- [enum SKProductStorePromotionVisibility](../skproductstorepromotionvisibility.md)
  The visibility settings that determine if an Apple In-App Purchase is visible on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/update(storepromotionvisibility:for:completionhandler:))*