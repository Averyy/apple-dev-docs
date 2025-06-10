# SKProductStorePromotionVisibility

**Framework**: StoreKit  
**Kind**: enum

The visibility settings that determine if an in-app purchase is visible on a device.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 11.0+

## Declaration

```swift
@frozen
enum SKProductStorePromotionVisibility
```

## Topics

### Enumeration cases
- [SKProductStorePromotionVisibility.default](skproductstorepromotionvisibility/default.md)
  Indicates product visibility is the same as the default value set in App Store Connect.
- [SKProductStorePromotionVisibility.hide](skproductstorepromotionvisibility/hide.md)
  Indicates product is hidden.
- [SKProductStorePromotionVisibility.show](skproductstorepromotionvisibility/show.md)
  Indicates product is shown.
### Initializers
- [init?(rawValue: Int)](skproductstorepromotionvisibility/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func fetchStorePromotionVisibility(for: SKProduct, completionHandler: ((SKProductStorePromotionVisibility, (any Error)?) -> Void)?)](skproductstorepromotioncontroller/fetchstorepromotionvisibility(for:completionhandler:).md)
  Reads the visibility setting of a promoted product in the App Store for this device.
- [func update(storePromotionVisibility: SKProductStorePromotionVisibility, for: SKProduct, completionHandler: (((any Error)?) -> Void)?)](skproductstorepromotioncontroller/update(storepromotionvisibility:for:completionhandler:).md)
  Updates the visibility of the product on the App Store, per device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductstorepromotionvisibility)*