# fetchStorePromotionOrder(completionHandler:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Reads the product order override that determines the promoted product order on this device.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0
- iPadOS 11.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 11.0+ - Deprecated in 18.0

> **Deprecated**: Use Product.PromotionInfo.currentOrder.

## Declaration

```swift
func fetchStorePromotionOrder(completionHandler: (@Sendable ([SKProduct], (any Error)?) -> Void)? = nil)
```

```swift
func promotionOrder() async throws -> [SKProduct]
```

```objc
- (void) fetchStorePromotionOrderWithCompletionHandler:(void (^)(NSArray<SKProduct *> *promotionOrder, NSError *error)) completionHandler;
```

## Mentions

- [Promoting Apple In-App Purchases](../promoting-in-app-purchases.md)

#### Discussion

This function returns an array of promoted products whose order is overridden on the given device.

If all the products appear in the default order, this method returns an empty array.

## See Also

### Managing promoted product order
- [func update(storePromotionOrder: [SKProduct], completionHandler: (((any Error)?) -> Void)?)](./update%28storepromotionorder,completionhandler%29.md)
  Overrides the promoted product order on this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/fetchstorepromotionorder(completionhandler:))*