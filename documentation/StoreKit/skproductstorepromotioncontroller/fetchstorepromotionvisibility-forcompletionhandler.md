# fetchStorePromotionVisibility(for:completionHandler:)

**Framework**: StoreKit  
**Kind**: method

Reads the visibility setting of a promoted product in the App Store for this device.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 11.0+

## Declaration

```swift
func promotionVisibility(for product: SKProduct) async throws -> SKProductStorePromotionVisibility
```

## Mentions

- [Promoting In-App Purchases](promoting-in-app-purchases.md)

#### Discussion

The default visibility for a promoted product is set in App Store Connect. Call [`fetchStorePromotionVisibility(for:completionHandler:)`](skproductstorepromotioncontroller/fetchstorepromotionvisibility(for:completionhandler:).md) to determine if a product’s visibility is set to the default value or if it has been overridden to be hidden or shown.

## See Also

- [func update(storePromotionVisibility: SKProductStorePromotionVisibility, for: SKProduct, completionHandler: (((any Error)?) -> Void)?)](skproductstorepromotioncontroller/update(storepromotionvisibility:for:completionhandler:).md)
  Updates the visibility of the product on the App Store, per device.
- [enum SKProductStorePromotionVisibility](skproductstorepromotionvisibility.md)
  The visibility settings that determine if an in-app purchase is visible on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/fetchstorepromotionvisibility(for:completionhandler:))*