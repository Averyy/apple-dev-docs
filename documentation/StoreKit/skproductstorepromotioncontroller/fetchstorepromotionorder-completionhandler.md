# fetchStorePromotionOrder(completionHandler:)

**Framework**: StoreKit  
**Kind**: method

Reads the product order override that determines the promoted product order on this device.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 11.0+

## Declaration

```swift
func promotionOrder() async throws -> [SKProduct]
```

## Mentions

- [Promoting In-App Purchases](promoting-in-app-purchases.md)

#### Discussion

This function returns an array of promoted products whose order is overridden on the given device.

If all the products appear in the default order, this method returns an empty array.

## See Also

- [func update(storePromotionOrder: [SKProduct], completionHandler: (((any Error)?) -> Void)?)](skproductstorepromotioncontroller/update(storepromotionorder:completionhandler:).md)
  Overrides the promoted product order on this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/fetchstorepromotionorder(completionhandler:))*