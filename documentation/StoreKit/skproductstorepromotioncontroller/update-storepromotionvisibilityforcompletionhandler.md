# update(storePromotionVisibility:for:completionHandler:)

**Framework**: StoreKit  
**Kind**: method

Updates the visibility of the product on the App Store, per device.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 11.0+

## Declaration

```swift
func update(promotionVisibility: SKProductStorePromotionVisibility, for product: SKProduct) async throws
```

#### Discussion

An in-app purchase product’s default visibility setting is set up in App Store Connect.  You can override the default setting, or return it to the default set in App Store Connect using the values in [`SKProductStorePromotionVisibility`](skproductstorepromotionvisibility.md).

Visibility settings apply per device.

## See Also

- [func fetchStorePromotionVisibility(for: SKProduct, completionHandler: ((SKProductStorePromotionVisibility, (any Error)?) -> Void)?)](skproductstorepromotioncontroller/fetchstorepromotionvisibility(for:completionhandler:).md)
  Reads the visibility setting of a promoted product in the App Store for this device.
- [enum SKProductStorePromotionVisibility](skproductstorepromotionvisibility.md)
  The visibility settings that determine if an in-app purchase is visible on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/update(storepromotionvisibility:for:completionhandler:))*