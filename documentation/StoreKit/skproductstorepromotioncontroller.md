# SKProductStorePromotionController

**Framework**: StoreKit  
**Kind**: class

A product promotion controller for customizing the order and visibility of In-App Purchases per device.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 11.0+

## Declaration

```swift
class SKProductStorePromotionController
```

## Mentions

- [Promoting In-App Purchases](promoting-in-app-purchases.md)

#### Overview

For information about promoting In-App Purchases, see [`Promoting In-App Purchases`](promoting-in-app-purchases.md).

> **Note**:  [`SKProductStorePromotionController`](skproductstorepromotioncontroller.md) and promoted In-App Purchases aren’t available to compatible iPad and iPhone apps running in visionOS.

 [`SKProductStorePromotionController`](skproductstorepromotioncontroller.md) and promoted In-App Purchases aren’t available to compatible iPad and iPhone apps running in visionOS.

## Topics

### Managing promoted product order
- [func fetchStorePromotionOrder(completionHandler: (([SKProduct], (any Error)?) -> Void)?)](skproductstorepromotioncontroller/fetchstorepromotionorder(completionhandler:).md)
  Reads the product order override that determines the promoted product order on this device.
- [func update(storePromotionOrder: [SKProduct], completionHandler: (((any Error)?) -> Void)?)](skproductstorepromotioncontroller/update(storepromotionorder:completionhandler:).md)
  Overrides the promoted product order on this device.
### Managing promoted product visibility
- [func fetchStorePromotionVisibility(for: SKProduct, completionHandler: ((SKProductStorePromotionVisibility, (any Error)?) -> Void)?)](skproductstorepromotioncontroller/fetchstorepromotionvisibility(for:completionhandler:).md)
  Reads the visibility setting of a promoted product in the App Store for this device.
- [func update(storePromotionVisibility: SKProductStorePromotionVisibility, for: SKProduct, completionHandler: (((any Error)?) -> Void)?)](skproductstorepromotioncontroller/update(storepromotionvisibility:for:completionhandler:).md)
  Updates the visibility of the product on the App Store, per device.
- [enum SKProductStorePromotionVisibility](skproductstorepromotionvisibility.md)
  The visibility settings that determine if an in-app purchase is visible on a device.
### Getting the controller
- [class func `default`() -> Self](skproductstorepromotioncontroller/default.md)
  Returns the default product store promotion controller.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Promoting In-App Purchases](promoting-in-app-purchases.md)
  Show promoted In-App Purchases on your product page and handle purchases that customers initiate on the App Store.
- [Testing promoted In-App Purchases](testing-promoted-in-app-purchases.md)
  Test your In-App Purchases before making your app available in the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller)*