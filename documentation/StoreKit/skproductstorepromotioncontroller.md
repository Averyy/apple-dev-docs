# SKProductStorePromotionController

**Framework**: StoreKit  
**Kind**: class  
**Role**: Class

A product promotion controller for customizing the order and visibility of Apple In-App Purchases per device.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0
- iPadOS 11.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 11.0+ - Deprecated in 18.0

> **Deprecated**: Use Product.PromotionInfo.

## Declaration

```swift
class SKProductStorePromotionController
```

```objc
@interface SKProductStorePromotionController : NSObject
```

## Mentions

- [Promoting Apple In-App Purchases](./promoting-in-app-purchases.md)

#### Overview

For information about promoting Apple In-App Purchases, see [Promoting Apple In-App Purchases](./promoting-in-app-purchases.md).

> **Note**:  [`SKProductStorePromotionController`](./skproductstorepromotioncontroller.md) and promoted Apple In-App Purchases aren’t available to compatible iPad and iPhone apps running in visionOS.

## Topics

### Managing promoted product order
- [func fetchStorePromotionOrder(completionHandler: (([SKProduct], (any Error)?) -> Void)?)](./skproductstorepromotioncontroller/fetchstorepromotionorder%28completionhandler%29.md)
  Reads the product order override that determines the promoted product order on this device.
- [func update(storePromotionOrder: [SKProduct], completionHandler: (((any Error)?) -> Void)?)](./skproductstorepromotioncontroller/update%28storepromotionorder,completionhandler%29.md)
  Overrides the promoted product order on this device.
### Managing promoted product visibility
- [func fetchStorePromotionVisibility(for: SKProduct, completionHandler: ((SKProductStorePromotionVisibility, (any Error)?) -> Void)?)](./skproductstorepromotioncontroller/fetchstorepromotionvisibility%28for,completionhandler%29.md)
  Reads the visibility setting of a promoted product in the App Store for this device.
- [func update(storePromotionVisibility: SKProductStorePromotionVisibility, for: SKProduct, completionHandler: (((any Error)?) -> Void)?)](./skproductstorepromotioncontroller/update%28storepromotionvisibility,for,completionhandler%29.md)
  Updates the visibility of the product on the App Store, per device.
- [enum SKProductStorePromotionVisibility](./skproductstorepromotionvisibility.md)
  The visibility settings that determine if an Apple In-App Purchase is visible on a device.
### Getting the controller
- [class func `default`() -> Self](./skproductstorepromotioncontroller/default%28%29.md)
  Returns the default product store promotion controller.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Promotions
- [Promoting Apple In-App Purchases](./promoting-in-app-purchases.md)
  Show promoted Apple In-App Purchases on your product page and handle purchases that customers initiate on the App Store.
- [Testing promoted Apple In-App Purchases](./testing-promoted-in-app-purchases.md)
  Test your Apple In-App Purchases before making your app available in the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller)*