# SKProductStorePromotionVisibility

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

The visibility settings that determine if an Apple In-App Purchase is visible on a device.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0
- iPadOS 11.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 11.0+ - Deprecated in 18.0

> **Deprecated**: Use Product.PromotionInfo.Visibility.

## Declaration

```swift
@frozen
enum SKProductStorePromotionVisibility
```

```c
enum SKProductStorePromotionVisibility : NSInteger;
```

## Topics

### Enumeration cases
- [SKProductStorePromotionVisibility.default](./skproductstorepromotionvisibility/default.md)
  Indicates product visibility is the same as the default value set in App Store Connect.
- [SKProductStorePromotionVisibility.hide](./skproductstorepromotionvisibility/hide.md)
  Indicates product is hidden.
- [SKProductStorePromotionVisibility.show](./skproductstorepromotionvisibility/show.md)
  Indicates product is shown.
### Initializers
- [init?(rawValue: Int)](./skproductstorepromotionvisibility/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing promoted product visibility
- [func fetchStorePromotionVisibility(for: SKProduct, completionHandler: ((SKProductStorePromotionVisibility, (any Error)?) -> Void)?)](./skproductstorepromotioncontroller/fetchstorepromotionvisibility%28for,completionhandler%29.md)
  Reads the visibility setting of a promoted product in the App Store for this device.
- [func update(storePromotionVisibility: SKProductStorePromotionVisibility, for: SKProduct, completionHandler: (((any Error)?) -> Void)?)](./skproductstorepromotioncontroller/update%28storepromotionvisibility,for,completionhandler%29.md)
  Updates the visibility of the product on the App Store, per device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductstorepromotionvisibility)*